# 🐼 Pandas DataFrame Quick Reference

**Module 01 - Quick Reference Guide**

A handy reference for common pandas DataFrame methods and attributes used throughout this course.

---

## 📋 Viewing Data

| Method | Description | Example |
|--------|-------------|---------|
| `df.head(n)` | First n rows (default 5) | `df.head(10)` |
| `df.tail(n)` | Last n rows (default 5) | `df.tail(20)` |
| `df.sample(n)` | Random n rows | `df.sample(5)` |
| `df.sample(frac=0.1)` | Random 10% of rows | `df.sample(frac=0.1)` |
| `df.iloc[start:end]` | Rows by integer position | `df.iloc[10:20]` |
| `df.loc[labels]` | Rows by index label | `df.loc['row_name']` |
| `df[['col1', 'col2']]` | Select specific columns | `df[['station_id', 'bikes_available']]` |

---

## 📐 Shape & Structure

| Method/Attribute | Description | Returns | Example |
|------------------|-------------|---------|---------|
| `df.shape` | Dimensions (rows, cols) | Tuple | `(1000, 13)` |
| `df.info()` | Column types, non-nulls, memory | Summary | Full dataset info |
| `df.dtypes` | Data type of each column | Series | Column → dtype mapping |
| `df.columns` | List of column names | Index | `['timestamp', 'station_id', ...]` |
| `df.index` | Row index information | Index | Row labels/numbers |
| `len(df)` | Number of rows | Integer | `1000` |
| `df.ndim` | Number of dimensions | Integer | `2` (always 2 for DataFrames) |
| `df.size` | Total elements (rows × cols) | Integer | `13000` |

---

## 📊 Statistical Summaries

| Method | Description | What It Shows |
|--------|-------------|---------------|
| `df.describe()` | Statistics for numeric columns | count, mean, std, min, 25%, 50%, 75%, max |
| `df.describe(include='all')` | All columns (numeric + categorical) | Adds unique, top, freq for objects |
| `df.describe(include='object')` | Only categorical columns | count, unique, top, freq |
| `df.mean()` | Mean of each numeric column | Series of means |
| `df.median()` | Median of each numeric column | Series of medians |
| `df.std()` | Standard deviation | Measure of spread |
| `df.var()` | Variance | Squared standard deviation |
| `df.min()` | Minimum values | Series of minimums |
| `df.max()` | Maximum values | Series of maximums |
| `df.sum()` | Sum of each column | Series of sums |
| `df.count()` | Non-null counts per column | Excludes NaN/None |
| `df.nunique()` | Count unique values per column | Number of distinct values |
| `df.corr()` | Correlation matrix | Pairwise correlations |
| `df['col'].value_counts()` | Frequency counts for a column | Most common values |

---

## 🔍 Data Quality Checks

| Method | Description | Returns | Example |
|--------|-------------|---------|---------|
| `df.isnull()` | Boolean mask of null values | DataFrame of True/False | Check for missing data |
| `df.isna()` | Same as `isnull()` | DataFrame of True/False | Alias for isnull() |
| `df.isnull().sum()` | Count of nulls per column | Series | `{'col1': 5, 'col2': 0}` |
| `df.isnull().sum().sum()` | Total nulls in entire DataFrame | Integer | `25` total missing |
| `df.notnull()` | Boolean mask of non-null values | DataFrame of True/False | Opposite of isnull() |
| `df.duplicated()` | Boolean mask of duplicate rows | Series of True/False | Check for duplicates |
| `df.duplicated().sum()` | Count of duplicate rows | Integer | `10` duplicates |
| `df.drop_duplicates()` | Remove duplicate rows | DataFrame | Returns cleaned data |

---

## 💾 Memory & Performance

| Method | Description | When to Use |
|--------|-------------|-------------|
| `df.memory_usage()` | Memory used by each column | Quick check |
| `df.memory_usage(deep=True)` | More accurate memory usage | Includes object overhead |
| `df.memory_usage().sum()` | Total memory | See total footprint |
| `df.info(memory_usage='deep')` | Detailed memory info | Full analysis |

---

## 🎯 Selection & Filtering

| Operation | Description | Example |
|-----------|-------------|---------|
| `df['column']` | Select single column (returns Series) | `df['bikes_available']` |
| `df[['col1', 'col2']]` | Select multiple columns (returns DataFrame) | `df[['station_id', 'hour']]` |
| `df[df['col'] > 5]` | Filter rows by condition | `df[df['bikes_available'] > 10]` |
| `df[(cond1) & (cond2)]` | Multiple conditions (AND) | `df[(df['hour'] > 8) & (df['hour'] < 18)]` |
| `df[(cond1) \| (cond2)]` | Multiple conditions (OR) | `df[(df['hour'] < 8) \| (df['hour'] > 18)]` |
| `df.query('col > 5')` | SQL-like filtering | `df.query('bikes_available > 10')` |
| `df.loc[rows, cols]` | Label-based selection | `df.loc[0:5, ['station_id', 'bikes_available']]` |
| `df.iloc[rows, cols]` | Position-based selection | `df.iloc[0:5, 0:3]` |

---

## 🔄 Data Transformations

| Method | Description | Example |
|--------|-------------|---------|
| `df['new_col'] = ...` | Create new column | `df['is_rush_hour'] = df['hour'].isin([8,9,17,18])` |
| `df.drop(columns=['col'])` | Drop column(s) | `df.drop(columns=['unnecessary_col'])` |
| `df.drop(index=[0,1])` | Drop row(s) | `df.drop(index=[0, 5, 10])` |
| `df.rename(columns={...})` | Rename columns | `df.rename(columns={'old': 'new'})` |
| `df.sort_values('col')` | Sort by column | `df.sort_values('timestamp')` |
| `df.sort_values(['c1','c2'])` | Sort by multiple columns | `df.sort_values(['station_id', 'timestamp'])` |
| `df.reset_index(drop=True)` | Reset index to default | `df.reset_index(drop=True)` |
| `df.set_index('col')` | Set column as index | `df.set_index('timestamp')` |

---

## 🧮 Grouping & Aggregation

| Method | Description | Example |
|--------|-------------|---------|
| `df.groupby('col')` | Group by column | `df.groupby('station_id')` |
| `df.groupby('col').mean()` | Mean by group | `df.groupby('hour')['bikes_available'].mean()` |
| `df.groupby('col').sum()` | Sum by group | `df.groupby('station_id')['bikes_available'].sum()` |
| `df.groupby('col').count()` | Count by group | `df.groupby('day_of_week').count()` |
| `df.groupby('col').agg([...])` | Multiple aggregations | `df.groupby('hour').agg(['mean', 'std', 'count'])` |
| `df.groupby(['c1','c2'])` | Group by multiple columns | `df.groupby(['station_id', 'hour']).mean()` |
| `df.pivot_table()` | Create pivot table | `df.pivot_table(values='bikes', index='hour', columns='station')` |

---

## 🔗 Combining DataFrames

| Method | Description | When to Use |
|--------|-------------|-------------|
| `pd.concat([df1, df2])` | Stack DataFrames vertically | Combining similar datasets |
| `pd.concat([df1, df2], axis=1)` | Stack horizontally | Adding columns |
| `df1.merge(df2, on='key')` | SQL-like join | Combining related data |
| `df1.merge(df2, left_on='a', right_on='b')` | Join on different column names | Mismatched key names |
| `df1.join(df2)` | Join on index | Index-aligned data |

---

## 📅 Working with Dates/Times

| Method | Description | Example |
|--------|-------------|---------|
| `pd.to_datetime(df['col'])` | Convert to datetime | `pd.to_datetime(df['timestamp'])` |
| `df['date'].dt.year` | Extract year | `df['timestamp'].dt.year` |
| `df['date'].dt.month` | Extract month | `df['timestamp'].dt.month` |
| `df['date'].dt.day` | Extract day | `df['timestamp'].dt.day` |
| `df['date'].dt.hour` | Extract hour | `df['timestamp'].dt.hour` |
| `df['date'].dt.dayofweek` | Day of week (0=Mon) | `df['timestamp'].dt.dayofweek` |
| `df['date'].dt.date` | Date only (no time) | `df['timestamp'].dt.date` |

---

## 💡 Pro Tips

### Chaining Methods
```python
# Combine multiple operations
df.head(10).describe().T  # Transpose for better viewing
df[df['bikes_available'] > 0].groupby('hour').mean()
```

### Quick Checks
```python
# One-liner data quality check
print(f"Shape: {df.shape}, Missing: {df.isnull().sum().sum()}, Duplicates: {df.duplicated().sum()}")
```

### Column Selection Shortcuts
```python
# Multiple ways to select
df.column_name          # Attribute access (no spaces in name)
df['column_name']       # Dictionary-style (always works)
df[['col1', 'col2']]    # Multiple columns
```

### Display Options
```python
# Configure pandas display
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.max_rows', 100)      # Show up to 100 rows
pd.set_option('display.precision', 2)       # 2 decimal places
pd.set_option('display.width', None)        # Auto-detect width
```

---

## 🚨 Common Gotchas

1. **`df.head()` needs parentheses** - It's a method, not an attribute
2. **Boolean indexing needs parentheses** - Use `(df['a'] > 5) & (df['b'] < 10)` not `df['a'] > 5 & df['b'] < 10`
3. **Assignment creates a view** - Use `.copy()` to avoid SettingWithCopyWarning
4. **Column names with spaces** - Must use `df['column name']`, not `df.column name`
5. **Chained indexing** - Avoid `df[df['a'] > 5]['b'] = 10`, use `.loc` instead

---

## 📚 Additional Resources

- **Official Pandas Docs**: https://pandas.pydata.org/docs/
- **Pandas Cheat Sheet**: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
- **10 Minutes to Pandas**: https://pandas.pydata.org/docs/user_guide/10min.html

---

**Quick Tip**: Keep this reference handy while working through the notebooks! 📖
