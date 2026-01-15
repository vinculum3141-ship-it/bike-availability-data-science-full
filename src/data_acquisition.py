"""
Data Acquisition Module

This module contains functions for acquiring data from various sources including
bike-sharing APIs, weather APIs, and data storage utilities.

📚 LEARNING PATH GUIDANCE:
    - Module 2: Use this file as REFERENCE MATERIAL while learning in notebooks
    - Module 8: Learn to BUILD and USE production scripts like this
    
    This module demonstrates production-ready patterns. In Module 2, focus on 
    understanding concepts through notebook experimentation. In Module 8, you'll 
    learn to create automated pipelines using these patterns.

Functions:
    fetch_bike_data() - Fetch bike availability data from CityBikes API
    fetch_weather_data() - Fetch weather data from Open-Meteo API
    save_raw_data() - Save raw data to data/raw/ directory
    load_raw_data() - Load raw data from saved files
    validate_data() - Validate data quality and completeness
    merge_bike_weather() - Merge bike and weather datasets

Example usage:
    from src.data_acquisition import fetch_bike_data, fetch_weather_data
    
    # Fetch bike data
    bike_data = fetch_bike_data(network_id='ns-bikes')
    
    # Fetch weather data
    weather_data = fetch_weather_data(
        latitude=52.37, 
        longitude=4.90,
        start_date='2026-01-01',
        end_date='2026-01-31'
    )
    
    # Save data
    save_raw_data(bike_data, 'bike_data.json', format='json')
    save_raw_data(weather_data, 'weather_data.csv', format='csv')
"""

import pandas as pd
import requests
import json
import time
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, Union, List


# ═══════════════════════════════════════════════════════════
# API CONFIGURATION
# ═══════════════════════════════════════════════════════════

CITYBIKES_BASE_URL = "http://api.citybik.es/v2"
OPENMETEO_BASE_URL = "https://archive-api.open-meteo.com/v1/archive"


# ═══════════════════════════════════════════════════════════
# BIKE DATA ACQUISITION
# ═══════════════════════════════════════════════════════════

def fetch_bike_data(network_id: str = 'ns-bikes', timeout: int = 10) -> Optional[Dict]:
    """
    Fetch bike availability data from CityBikes API.
    
    Parameters:
    -----------
    network_id : str
        Network ID (e.g., 'ns-bikes' for Amsterdam)
    timeout : int
        Request timeout in seconds
    
    Returns:
    --------
    dict or None
        JSON response with bike station data if successful, None otherwise
    
    Example:
    --------
    >>> data = fetch_bike_data('ns-bikes')
    >>> if data:
    >>>     stations = data['network']['stations']
    >>>     print(f"Fetched {len(stations)} stations")
    """
    url = f"{CITYBIKES_BASE_URL}/networks/{network_id}"
    
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.Timeout:
        print(f"⏱️ Timeout: Request took longer than {timeout} seconds")
        return None
    
    except requests.exceptions.ConnectionError:
        print("🔌 Connection Error: Could not connect to API")
        return None
    
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")
        return None
    
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Request Error: {e}")
        return None
    
    except json.JSONDecodeError:
        print("📝 JSON Error: Could not parse response")
        return None


def bike_json_to_dataframe(bike_data: Dict) -> pd.DataFrame:
    """
    Convert CityBikes API JSON response to pandas DataFrame.
    
    Parameters:
    -----------
    bike_data : dict
        JSON response from CityBikes API
    
    Returns:
    --------
    pandas.DataFrame
        Bike station data with cleaned column names
    """
    stations = bike_data['network']['stations']
    df = pd.DataFrame(stations)
    
    # Parse timestamp
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Rename columns for clarity
    df = df.rename(columns={
        'free_bikes': 'bikes_available',
        'empty_slots': 'docks_available'
    })
    
    # Add metadata
    df['network_id'] = bike_data['network']['id']
    df['network_name'] = bike_data['network']['name']
    df['city'] = bike_data['network']['location']['city']
    df['country'] = bike_data['network']['location']['country']
    
    # Add derived columns
    if 'bikes_available' in df.columns and 'docks_available' in df.columns:
        df['total_capacity'] = df['bikes_available'] + df['docks_available']
        df['utilization_pct'] = (df['bikes_available'] / df['total_capacity'] * 100).round(2)
    
    return df


# ═══════════════════════════════════════════════════════════
# WEATHER DATA ACQUISITION
# ═══════════════════════════════════════════════════════════

def fetch_weather_data(latitude: float, longitude: float, 
                       start_date: Union[str, datetime], 
                       end_date: Union[str, datetime],
                       variables: Optional[List[str]] = None,
                       timezone: str = 'Europe/Amsterdam',
                       timeout: int = 30) -> Optional[Dict]:
    """
    Fetch historical weather data from Open-Meteo API.
    
    Parameters:
    -----------
    latitude : float
        Location latitude
    longitude : float
        Location longitude
    start_date : str or datetime
        Start date (YYYY-MM-DD)
    end_date : str or datetime
        End date (YYYY-MM-DD)
    variables : list of str, optional
        Weather variables to fetch. Defaults to common variables.
    timezone : str
        Timezone for timestamps
    timeout : int
        Request timeout in seconds
    
    Returns:
    --------
    dict or None
        JSON response with weather data if successful, None otherwise
    
    Example:
    --------
    >>> weather = fetch_weather_data(
    >>>     latitude=52.37,
    >>>     longitude=4.90,
    >>>     start_date='2026-01-01',
    >>>     end_date='2026-01-31'
    >>> )
    """
    # Default weather variables
    if variables is None:
        variables = [
            'temperature_2m',
            'relativehumidity_2m',
            'precipitation',
            'rain',
            'windspeed_10m',
            'winddirection_10m',
            'cloudcover',
            'pressure_msl'
        ]
    
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'start_date': str(start_date),
        'end_date': str(end_date),
        'hourly': ','.join(variables),
        'timezone': timezone
    }
    
    try:
        response = requests.get(OPENMETEO_BASE_URL, params=params, timeout=timeout)
        response.raise_for_status()
        
        data = response.json()
        
        if 'hourly' not in data:
            print("❌ Error: No hourly data in response")
            return None
        
        return data
    
    except requests.exceptions.Timeout:
        print(f"⏱️ Timeout: Request took longer than {timeout} seconds")
        return None
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Request Error: {e}")
        return None
    
    except json.JSONDecodeError:
        print("📝 JSON Error: Could not parse response")
        return None


def weather_json_to_dataframe(weather_data: Dict) -> pd.DataFrame:
    """
    Convert Open-Meteo API JSON response to pandas DataFrame.
    
    Parameters:
    -----------
    weather_data : dict
        JSON response from Open-Meteo API
    
    Returns:
    --------
    pandas.DataFrame
        Weather data with cleaned column names
    """
    df = pd.DataFrame(weather_data['hourly'])
    
    # Parse timestamps
    df['time'] = pd.to_datetime(df['time'])
    df = df.rename(columns={'time': 'timestamp'})
    
    # Add metadata
    df['latitude'] = weather_data['latitude']
    df['longitude'] = weather_data['longitude']
    df['elevation_m'] = weather_data['elevation']
    df['timezone'] = weather_data['timezone']
    
    return df


# ═══════════════════════════════════════════════════════════
# DATA STORAGE
# ═══════════════════════════════════════════════════════════

def save_raw_data(data: Union[pd.DataFrame, Dict], 
                  filename: str, 
                  output_dir: str = 'data/raw',
                  format: str = 'auto',
                  create_metadata: bool = True) -> Path:
    """
    Save raw data to file with optional metadata.
    
    Parameters:
    -----------
    data : pandas.DataFrame or dict
        Data to save
    filename : str
        Output filename (without extension if format='auto')
    output_dir : str
        Output directory path
    format : str
        File format ('csv', 'json', 'parquet', or 'auto')
    create_metadata : bool
        Whether to create accompanying metadata file
    
    Returns:
    --------
    Path
        Path to saved file
    
    Example:
    --------
    >>> df = pd.DataFrame({'col1': [1, 2, 3]})
    >>> filepath = save_raw_data(df, 'my_data.csv', format='csv')
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Auto-detect format from filename or data type
    if format == 'auto':
        if filename.endswith('.json'):
            format = 'json'
        elif filename.endswith('.parquet'):
            format = 'parquet'
        elif filename.endswith('.csv'):
            format = 'csv'
        elif isinstance(data, dict):
            format = 'json'
            if not filename.endswith('.json'):
                filename += '.json'
        else:
            format = 'csv'
            if not filename.endswith('.csv'):
                filename += '.csv'
    
    filepath = output_dir / filename
    
    # Save based on format
    if format == 'json':
        with open(filepath, 'w') as f:
            json.dump(data if isinstance(data, dict) else data.to_dict(orient='records'), 
                     f, indent=2, default=str)
    
    elif format == 'csv':
        if isinstance(data, dict):
            pd.DataFrame([data]).to_csv(filepath, index=False)
        else:
            data.to_csv(filepath, index=False)
    
    elif format == 'parquet':
        if isinstance(data, dict):
            pd.DataFrame([data]).to_parquet(filepath, index=False)
        else:
            data.to_parquet(filepath, index=False)
    
    # Create metadata file
    if create_metadata:
        metadata = {
            'filename': filename,
            'created_date': datetime.now().isoformat(),
            'format': format,
            'size_bytes': filepath.stat().st_size
        }
        
        if isinstance(data, pd.DataFrame):
            metadata['shape'] = {'rows': len(data), 'columns': len(data.columns)}
            metadata['columns'] = list(data.columns)
        
        metadata_file = filepath.with_suffix('.metadata.json')
        with open(metadata_file, 'w') as f:
            json.dump(metadata, f, indent=2)
    
    return filepath


def load_raw_data(filepath: Union[str, Path], 
                  format: str = 'auto',
                  parse_dates: Optional[List[str]] = None) -> Union[pd.DataFrame, Dict]:
    """
    Load raw data from file.
    
    Parameters:
    -----------
    filepath : str or Path
        Path to file to load
    format : str
        File format ('csv', 'json', 'parquet', or 'auto')
    parse_dates : list of str, optional
        Column names to parse as dates
    
    Returns:
    --------
    pandas.DataFrame or dict
        Loaded data
    
    Example:
    --------
    >>> df = load_raw_data('data/raw/my_data.csv', parse_dates=['timestamp'])
    """
    filepath = Path(filepath)
    
    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    
    # Auto-detect format
    if format == 'auto':
        if filepath.suffix == '.json':
            format = 'json'
        elif filepath.suffix == '.parquet':
            format = 'parquet'
        else:
            format = 'csv'
    
    # Load based on format
    if format == 'json':
        with open(filepath, 'r') as f:
            return json.load(f)
    
    elif format == 'csv':
        return pd.read_csv(filepath, parse_dates=parse_dates)
    
    elif format == 'parquet':
        return pd.read_parquet(filepath)
    
    else:
        raise ValueError(f"Unsupported format: {format}")


# ═══════════════════════════════════════════════════════════
# DATA VALIDATION
# ═══════════════════════════════════════════════════════════

def validate_data(df: pd.DataFrame, 
                  required_columns: Optional[List[str]] = None,
                  check_missing: bool = True,
                  check_duplicates: bool = True,
                  value_ranges: Optional[Dict[str, tuple]] = None) -> bool:
    """
    Validate data quality and completeness.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Data to validate
    required_columns : list of str, optional
        Columns that must be present
    check_missing : bool
        Whether to check for missing values
    check_duplicates : bool
        Whether to check for duplicate rows
    value_ranges : dict, optional
        Expected value ranges for columns {column: (min, max)}
    
    Returns:
    --------
    bool
        True if all validations pass, False otherwise
    
    Example:
    --------
    >>> is_valid = validate_data(
    >>>     df,
    >>>     required_columns=['timestamp', 'bikes_available'],
    >>>     value_ranges={'bikes_available': (0, 100)}
    >>> )
    """
    validations = []
    
    # Check required columns
    if required_columns:
        missing_cols = [col for col in required_columns if col not in df.columns]
        if missing_cols:
            print(f"❌ Missing columns: {missing_cols}")
            validations.append(False)
        else:
            validations.append(True)
    
    # Check for missing values
    if check_missing:
        missing_count = df.isna().sum().sum()
        if missing_count > 0:
            print(f"⚠️ Found {missing_count} missing values")
            validations.append(True)  # Warning, not error
        else:
            validations.append(True)
    
    # Check for duplicates
    if check_duplicates:
        dup_count = df.duplicated().sum()
        if dup_count > 0:
            print(f"⚠️ Found {dup_count} duplicate rows")
            validations.append(True)  # Warning, not error
        else:
            validations.append(True)
    
    # Check value ranges
    if value_ranges:
        for col, (min_val, max_val) in value_ranges.items():
            if col in df.columns:
                out_of_range = ((df[col] < min_val) | (df[col] > max_val)).sum()
                if out_of_range > 0:
                    print(f"⚠️ {col}: {out_of_range} values out of range [{min_val}, {max_val}]")
                validations.append(True)
    
    return all(validations) if validations else True


# ═══════════════════════════════════════════════════════════
# DATA MERGING
# ═══════════════════════════════════════════════════════════

def merge_bike_weather(df_bikes: pd.DataFrame, 
                       df_weather: pd.DataFrame,
                       time_col: str = 'timestamp',
                       strategy: str = 'nearest',
                       tolerance: str = '30min') -> pd.DataFrame:
    """
    Merge bike and weather datasets with time alignment.
    
    Parameters:
    -----------
    df_bikes : pandas.DataFrame
        Bike availability data
    df_weather : pandas.DataFrame
        Weather data
    time_col : str
        Name of timestamp column
    strategy : str
        Merge strategy ('nearest', 'forward', 'backward', or 'aggregate')
    tolerance : str
        Maximum time difference to allow for nearest matching
    
    Returns:
    --------
    pandas.DataFrame
        Merged dataset
    
    Example:
    --------
    >>> merged = merge_bike_weather(
    >>>     df_bikes,
    >>>     df_weather,
    >>>     strategy='nearest',
    >>>     tolerance='30min'
    >>> )
    """
    df_bikes = df_bikes.copy()
    df_weather = df_weather.copy()
    
    # Ensure timestamps are datetime
    df_bikes[time_col] = pd.to_datetime(df_bikes[time_col])
    df_weather[time_col] = pd.to_datetime(df_weather[time_col])
    
    # Sort by time
    df_bikes = df_bikes.sort_values(time_col)
    df_weather = df_weather.sort_values(time_col)
    
    if strategy == 'aggregate':
        # Aggregate bikes to hourly
        df_bikes['hour'] = df_bikes[time_col].dt.floor('H')
        
        agg_funcs = {col: 'mean' for col in df_bikes.columns 
                    if col not in [time_col, 'hour', 'station_id', 'id', 'name']}
        
        if 'station_id' in df_bikes.columns:
            df_bikes_agg = df_bikes.groupby(['hour', 'station_id']).agg(agg_funcs).reset_index()
        else:
            df_bikes_agg = df_bikes.groupby('hour').agg(agg_funcs).reset_index()
        
        df_bikes_agg = df_bikes_agg.rename(columns={'hour': time_col})
        
        # Exact match merge
        merged = pd.merge(df_bikes_agg, df_weather, on=time_col, how='inner')
    
    else:
        # Use merge_asof for nearest/forward/backward matching
        merged = pd.merge_asof(
            df_bikes,
            df_weather,
            on=time_col,
            direction=strategy,
            tolerance=pd.Timedelta(tolerance)
        )
    
    return merged
