# 🚀 Data Loading & Analysis Workflow (DuckDB + Pandas Hybrid)

This project uses a hybrid workflow that combines **DuckDB** and **pandas** to efficiently handle an extremely wide dataset (68,000+ columns). This design provides the performance benefits of an analytical database while preserving the flexibility required for machine learning.

---

## 1. DuckDB Connection
A DuckDB in-memory database is initialized for fast SQL access:

```python
conn = duckdb.connect()
```

DuckDB acts as a lightweight analytical engine for metadata inspection, schema analysis, and efficient CSV ingestion.

---

## 2. High-Performance CSV Loading Using DuckDB
CSV files are read using DuckDB’s `read_csv_auto()`, which is significantly faster and more memory-efficient than pandas for wide datasets:

```python
train_df = conn.execute("""
    SELECT * FROM read_csv_auto('train.csv', max_line_size=5000000)
""").df()
```

Using `.df()` converts DuckDB’s internal result into a **pandas DataFrame** for downstream ML workflows.

---

## 3. Register Pandas DataFrames Back Into DuckDB
After loading, the pandas DataFrames are registered as DuckDB tables, enabling SQL access without duplicating data:

```python
duckdb.register('train', train_df)
duckdb.register('test', test_df)
```

DuckDB now treats these DataFrames as SQL tables for fast schema queries.

---

## 4. Use DuckDB for Metadata & Structural EDA
DuckDB efficiently handles high-dimensional metadata queries such as:

- Column prefix grouping  
- Train/test schema alignment  
- Constant-column detection  
- Data type summaries  
- Feature family discovery  

Example: Prefix grouping for 68K columns

```sql
SELECT regexp_extract(column_name, '^[^_]+') AS prefix,
       COUNT(*) AS count
FROM pragma_table_info('train')
GROUP BY prefix
ORDER BY count DESC;
```

DuckDB works off its metadata tables, avoiding expensive scans of all 68,000 columns.

---

## 5. Use Pandas for Modeling & Visual EDA
Once schema exploration is complete, modeling workflows rely on pandas:

- LightGBM / XGBoost  
- Scikit-Learn preprocessing  
- Seaborn / matplotlib / missingno visualizations  
- Feature engineering  

This hybrid workflow keeps **exploration efficient** while preserving **ML compatibility**.

---

## 🎯 Why This Architecture Is Ideal

- **DuckDB** handles extremely wide data with ease  
- **Pandas** is required for modeling frameworks  
- Registration avoids unnecessary memory copies  
- SQL introspection accelerates EDA  
- Clean, simple setup that is easy to document and replicate  

This approach is efficient, professional, and perfectly suited for large, high-dimensional ML competitions.
