# 📘 DuckDB Loader --- Usage Guide

This document explains how to use the custom DuckDB data-loading
utilities located in:

    src/data/load_duckdb.py

These utilities provide a clean, reliable way to load the extremely wide
CSV files used in the *Detect Reversal Points in U.S. Equities* Kaggle
competition.

------------------------------------------------------------------------

## 🧠 Purpose of the Loader

DuckDB is excellent for querying large, wide CSVs --- but the
competition dataset contains **thousands of columns**, which can cause:

-   header rows exceeding 4 MB\
-   errors caused by DuckDB's default `max_line_size`\
-   path issues when running notebooks from different directories

This loader module solves all of that by providing:

-   automatic project root detection\
-   automatic `max_line_size` bump\
-   consistent pathing\
-   one-line functions for loading train/test/sample submission\
-   option to return either Pandas DataFrame or DuckDB Relation

------------------------------------------------------------------------

## 📁 Where the Loader Lives

    src/data/load_duckdb.py

Functions exposed:

-   `load_train()`
-   `load_test()`
-   `load_sample_submission()`
-   `load_csv()` (generic loader)

------------------------------------------------------------------------

## 🚀 Quick Start

### **1. Import the loader**

``` python
from src.data.load_duckdb import load_train, load_test
```

### **2. Load the train/test data as Pandas DataFrames**

``` python
df_train = load_train()
df_test = load_test()

df_train.head()
```

------------------------------------------------------------------------

## 🦆 Returning a DuckDB Relation Instead of Pandas

``` python
train_rel = load_train(as_df=False)
train_rel.limit(5)
```

Reasons to use a Relation:

-   SQL queries stay inside DuckDB\
-   faster exploration\
-   ideal for slicing, joining, or feature engineering\
-   lower memory usage

------------------------------------------------------------------------

## 📌 How Paths Are Handled

-   Detects project root by locating `/data`
-   Builds absolute path\
-   Opens DuckDB connection\
-   Sets:

``` sql
SET max_line_size=5000000;
```

------------------------------------------------------------------------

## 📚 Loading Any CSV

``` python
from src.data.load_duckdb import load_csv

df = load_csv("data/raw/new_competition_data/train.csv")
```

Or as a Relation:

``` python
rel = load_csv("data/raw/new_competition_data/train.csv", as_df=False)
rel.describe()
```

------------------------------------------------------------------------

## 📄 Loading Sample Submission

``` python
from src.data.load_duckdb import load_sample_submission

sample = load_sample_submission()
sample.head()
```

------------------------------------------------------------------------

## 🛠️ Summary of Features

  Feature                            Description
  ---------------------------------- -------------------------------
  Automatic project-root detection   Notebooks always work
  Handles huge CSV header rows       Avoids line-size errors
  Pandas or DuckDB                   Flexible workflow
  Clean APIs                         `load_train()`, `load_test()`
  Centralized loader                 Consistent across pipeline

------------------------------------------------------------------------

## 🏁 Recommended Usage in Pipeline

-   **00_baseline.ipynb:** Load pandas\
-   **01_eda.ipynb:** Use DuckDB relations\
-   **02_feature_engineering.ipynb:** SQL-based feature engineering\
-   **03_model_training.ipynb:** Convert back to pandas

------------------------------------------------------------------------
