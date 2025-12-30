"""
Generate synthetic bike availability and weather data for testing and demos.

This script creates realistic bike-sharing data that mimics real-world patterns:
- Temporal patterns (commuter vs tourist stations)
- Weather effects (temperature, precipitation, wind)
- Weekday vs weekend differences
- Empty/full station scenarios

Usage:
    python src/generate_sample_data.py
    python src/generate_sample_data.py --output data/raw/custom_sample.csv
    python src/generate_sample_data.py --stations 5 --days 7
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import argparse
from pathlib import Path


def generate_bike_weather_data(
    num_stations=2,
    num_days=3,
    start_date="2024-01-15",
    start_hour=6,
    end_hour=20,
    random_seed=42
):
    """
    Generate synthetic bike availability and weather data.
    
    Parameters
    ----------
    num_stations : int
        Number of bike stations to generate data for
    num_days : int
        Number of days to generate data for
    start_date : str
        Starting date in YYYY-MM-DD format
    start_hour : int
        First hour of day to generate data (0-23)
    end_hour : int
        Last hour of day to generate data (0-23)
    random_seed : int
        Random seed for reproducibility
        
    Returns
    -------
    pd.DataFrame
        DataFrame with synthetic bike and weather data
    """
    np.random.seed(random_seed)
    
    # Define stations with different characteristics
    stations = [
        {
            'id': f'AMS-{str(i+1).zfill(3)}',
            'name': name,
            'lat': lat,
            'lon': lon,
            'capacity': 20,
            'type': station_type
        }
        for i, (name, lat, lon, station_type) in enumerate([
            ('Centraal Station', 52.3791, 4.9003, 'commuter'),
            ('Museumplein', 52.3580, 4.8814, 'tourist'),
            ('Vondelpark', 52.3579, 4.8686, 'leisure'),
            ('Dam Square', 52.3730, 4.8936, 'tourist'),
            ('RAI Station', 52.3387, 4.8907, 'commuter'),
        ])
    ][:num_stations]
    
    # Generate date range
    start = datetime.strptime(start_date, "%Y-%m-%d")
    dates = []
    
    for day_offset in range(num_days):
        current_date = start + timedelta(days=day_offset)
        for hour in range(start_hour, end_hour + 1):
            dates.append(current_date.replace(hour=hour, minute=0, second=0))
    
    # Generate data rows
    data_rows = []
    
    for timestamp in dates:
        # Day characteristics
        hour = timestamp.hour
        day_of_week = timestamp.weekday()  # 0=Monday, 6=Sunday
        is_weekend = 1 if day_of_week >= 5 else 0
        
        # Weather (varies by day, with some randomness)
        day_offset = (timestamp - start).days
        
        # Base temperature (varies by day)
        base_temp = 8 + np.sin(day_offset * 0.5) * 4
        temp_variation = np.sin((hour - 6) / 12 * np.pi) * 3  # Warmer in afternoon
        temperature = base_temp + temp_variation + np.random.normal(0, 0.5)
        
        # Precipitation (some days rainy, some dry)
        if day_offset % 3 == 1:  # Every 3rd day has rain
            precipitation = max(0, 2.0 - abs(hour - 12) * 0.2 + np.random.normal(0, 0.3))
        else:
            precipitation = 0.0
        
        # Wind speed (higher when rainy)
        windspeed = 8 + (precipitation * 2) + np.random.normal(0, 1.5)
        windspeed = max(5, min(20, windspeed))
        
        # Generate data for each station
        for station in stations:
            # Base bike availability depends on station type and time
            if station['type'] == 'commuter':
                # Commuter stations: low in morning, high in evening
                if hour < 9:
                    base_bikes = 15 - (9 - hour) * 2  # Fewer bikes in early morning
                elif hour < 17:
                    base_bikes = 8  # Stable during day
                else:
                    base_bikes = 15 + (hour - 17)  # More bikes return in evening
            
            elif station['type'] == 'tourist':
                # Tourist stations: busy midday, quiet early/late
                if 10 <= hour <= 16:
                    base_bikes = 5  # Low during tourist hours
                else:
                    base_bikes = 14
            
            else:  # leisure
                # Leisure stations: busy on nice weather afternoons
                if is_weekend and 12 <= hour <= 18 and precipitation == 0:
                    base_bikes = 4
                else:
                    base_bikes = 12
            
            # Weather effects
            if precipitation > 0:
                base_bikes += 5  # More bikes available when raining (less usage)
            if temperature < 5:
                base_bikes += 3  # More bikes when cold
            
            # Weekend effects (depends on station type)
            if is_weekend:
                if station['type'] == 'commuter':
                    base_bikes += 4  # Less commuter usage on weekends
                elif station['type'] == 'tourist':
                    base_bikes -= 2  # More tourist usage on weekends
            
            # Add randomness
            bikes_available = base_bikes + np.random.randint(-2, 3)
            bikes_available = max(0, min(station['capacity'], int(bikes_available)))
            
            # Calculate docks
            docks_available = station['capacity'] - bikes_available
            
            # Create row
            data_rows.append({
                'timestamp': timestamp,
                'station_id': station['id'],
                'station_name': station['name'],
                'latitude': station['lat'],
                'longitude': station['lon'],
                'bikes_available': bikes_available,
                'docks_available': docks_available,
                'temperature': round(temperature, 1),
                'precipitation': round(precipitation, 1),
                'windspeed': round(windspeed, 1),
                'hour': hour,
                'day_of_week': day_of_week,
                'is_weekend': is_weekend
            })
    
    # Create DataFrame
    df = pd.DataFrame(data_rows)
    
    # Sort by timestamp and station
    df = df.sort_values(['timestamp', 'station_id']).reset_index(drop=True)
    
    return df


def main():
    """Main function to generate and save sample data."""
    parser = argparse.ArgumentParser(
        description='Generate synthetic bike availability and weather data'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='data/raw/sample_bike_weather.csv',
        help='Output file path (default: data/raw/sample_bike_weather.csv)'
    )
    parser.add_argument(
        '--stations',
        type=int,
        default=2,
        help='Number of stations (default: 2, max: 5)'
    )
    parser.add_argument(
        '--days',
        type=int,
        default=3,
        help='Number of days (default: 3)'
    )
    parser.add_argument(
        '--start-date',
        type=str,
        default='2024-01-15',
        help='Start date in YYYY-MM-DD format (default: 2024-01-15)'
    )
    parser.add_argument(
        '--start-hour',
        type=int,
        default=6,
        help='First hour of day (default: 6)'
    )
    parser.add_argument(
        '--end-hour',
        type=int,
        default=20,
        help='Last hour of day (default: 20)'
    )
    parser.add_argument(
        '--seed',
        type=int,
        default=42,
        help='Random seed for reproducibility (default: 42)'
    )
    
    args = parser.parse_args()
    
    # Validate inputs
    if args.stations < 1 or args.stations > 5:
        print("Error: Number of stations must be between 1 and 5")
        return
    
    if args.days < 1:
        print("Error: Number of days must be at least 1")
        return
    
    # Generate data
    print("🔧 Generating synthetic bike availability data...")
    print(f"   Stations: {args.stations}")
    print(f"   Days: {args.days}")
    print(f"   Start date: {args.start_date}")
    print(f"   Hours: {args.start_hour}:00 - {args.end_hour}:00")
    print()
    
    df = generate_bike_weather_data(
        num_stations=args.stations,
        num_days=args.days,
        start_date=args.start_date,
        start_hour=args.start_hour,
        end_hour=args.end_hour,
        random_seed=args.seed
    )
    
    # Create output directory if it doesn't exist
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Save to CSV
    df.to_csv(output_path, index=False)
    
    print(f"✅ Data generated successfully!")
    print(f"📁 Saved to: {output_path}")
    print(f"📊 Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    print()
    print("Sample data (first 5 rows):")
    print(df.head())
    print()
    print("Statistics:")
    print(df[['bikes_available', 'temperature', 'precipitation', 'windspeed']].describe())


if __name__ == '__main__':
    main()
