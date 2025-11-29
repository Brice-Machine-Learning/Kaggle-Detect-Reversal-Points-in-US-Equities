
# Understanding the Full CSV Load Issue (Wide Dataset Handling Notes)

## 🧩 Overview
During the baseline setup, the goal was to load the **full training and test datasets** using DuckDB:

- `train.csv` → 1932 rows × ~68,504 features  
- `test.csv` → 828 rows × ~68,504 features  

Initially, the shapes looked incorrect because only a small number of rows were sampled using LIMIT. When loading without LIMIT, the notebook appeared to hang until Jupyter interrupted the execution.

This document explains **why** that happened and what the improved code does.

---

## 🧨 What Initially Happened

### **1. The dataset is extremely wide**
The data description revealed:

- **68,504 feature columns**
- + metadata columns (`id`, `ticker_id`, `t`, `class_label`)

This structure is extremely unusual compared to typical Kaggle datasets.

### **2. DuckDB struggled with type inference**
The original attempt used:

```
SELECT *
FROM read_csv_auto('train.csv', max_line_size=5000000)
```

Issues:

- `read_csv_auto()` attempts type inference for **all ~68,000 columns**
- DuckDB scans each column to guess types
- Converting the full dataset to Pandas with `.df()` materializes everything at once
- This becomes computationally heavy

**Result:**  
The cell kept running until Jupyter timed out with a `KeyboardInterrupt`.

### **3. Pandas confirmed the dataset structure**
Running pandas:

```
pd.read_csv(...)
```

produced:

```
(1932, 68507)
```

This confirmed that:

- DuckDB parsed the file correctly  
- The dataset truly is extremely wide  
- The issue was resource intensity, not corrupted data  

---

## 🧠 Why the Original Load Failed

### **DuckDB + read_csv_auto + .df() is not ideal for ultra-wide tables**

DuckDB must:

1. Parse each row  
2. Infer types for ~68k columns  
3. Build Arrow column arrays  
4. Convert the entire table into a Pandas DataFrame  

This combination is powerful, but for **very wide** datasets it becomes:

- slow  
- memory-heavy  
- prone to Jupyter timeouts  

The hanging behavior was simply due to the dataset size.

---

# 🛠️ The Improved Approach

To handle the dataset efficiently, we switched to **Arrow-backed loading**, optimized for wide tabular structures.

## ✔ Using Arrow Instead of .df()

```
train_df = conn.execute(
    """
    SELECT *
    FROM read_csv_auto(
        '../data/raw/competition_data/train.csv',
        max_line_size=10000000
    )
    """
).fetch_arrow_table().to_pandas()
```

### Explanation:

#### 🟩 `read_csv_auto(...)`
Still handles parsing and headers, and:

- increases `max_line_size` for wide rows  
- avoids brittle inference issues  

#### 🟩 `fetch_arrow_table()`
This is the key improvement:

- Returns an **Arrow Table**, not a DuckDB → Pandas conversion  
- Arrow stores data column-wise very efficiently  
- Enables faster conversion to Pandas  
- Reduces memory overhead  
- Helps avoid Jupyter timeouts  

#### 🟩 `.to_pandas()`
Performs an optimized Arrow → Pandas conversion.

This is significantly more efficient than using `.df()`.

---

# 👌 Alternative: Pandas with PyArrow Engine

```
train_df = pd.read_csv(
    '../data/raw/competition_data/train.csv',
    engine='pyarrow'
)
```

Benefits:

- Avoids DuckDB’s type inference  
- Uses PyArrow’s optimized CSV reader  
- Often faster for very wide datasets  

---

# 🎯 Summary

- The dataset contains **68k+ features**, which is unusually wide.
- DuckDB parsed correctly, but `.df()` conversion was too resource-intensive.
- The notebook interruption was due to load size, not malformed data.
- Arrow-backed loading or PyArrow-based Pandas loading resolves the issue.
- This enables successful baseline modeling.

---

