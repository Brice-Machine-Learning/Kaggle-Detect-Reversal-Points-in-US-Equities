# 📄 Baseline Notebook Summary  
### *Detecting Reversal Points in U.S. Equities — Baseline Pipeline*

---

## 🎯 Purpose of This Notebook

This notebook establishes the **first end-to-end working pipeline** for the Kaggle competition *Detecting Reversal Points in U.S. Equities*.  
The goal is not performance, but **correctness, stability, and reproducibility**.

This baseline confirms:
- the dataset structure (3-class target: `H`, `L`, `None`)
- the correctness of the train/test split
- successful preprocessing and feature alignment
- the ability to generate a valid Kaggle submission
- LightGBM multiclass modeling works as expected

This milestone completes **Phase 1.5 — Baseline Sanity Check**.

---

## 🧹 1. Data Loading

The notebook loads the updated competition dataset from:

```
/data/raw/new_competition_data/
```

DuckDB is used for fast CSV ingestion with `read_csv_auto()` and a large `max_line_size` due to wide feature columns.

Both train and test were verified to match expected shapes:

| Split | Rows | Columns | Notes |
|-------|------|---------|--------|
| Train | 3834 | ~68K | Includes `class_label`, `ticker_id`, `t`, `train_id` |
| Test  | 1151 | ~68K | Includes `id`, `ticker_id`, `t` |

---

## 🏷️ 2. Target Cleaning & Encoding

The dataset uses **3 classes**:

- `H` — High-pattern  
- `L` — Low-pattern  
- `None` — No clear pattern / missing signal  

Steps performed:

- Verified no missing or corrupted labels  
- Applied `LabelEncoder`  
- Target encoded → `[0, 1, 2]`

---

## 🏗️ 3. Preprocessing

### Dropped Metadata Columns

From **train**:
- `class_label`
- `ticker_id`
- `t`
- `train_id`

From **test**:
- `ticker_id`
- `t`
- `id`  

Feature alignment enforced with:  
```python
X_test = X_test[X.columns]
```

---

## ✂️ 4. Dimensionality Reduction

Because the dataset contains **68,000+** feature columns, the baseline uses:

```python
TruncatedSVD(n_components=512, random_state=42)
```

The reduced shapes:

- `X_reduced.shape      → (3834, 512)`
- `X_test_reduced.shape → (1151, 512)`

This drastically reduces memory usage and speeds model training.

---

## 🤖 5. Baseline Model (LightGBM)

The baseline model:

```python
LGBMClassifier(
    objective='multiclass',
    num_class=3,
    n_estimators=600,
    learning_rate=0.05,
    num_leaves=64,
    device='cpu'
)
```

Notes:
- CPU mode is used intentionally (GPU build not required for baseline)
- No class weighting yet (majority-class dominates)
- No time-series CV yet (future phases)

---

## 🧪 6. Predictions & Submission

- Predictions made with `model.predict()`  
- Classes recovered using `inverse_transform`  
- Submission aligned with `sample_submission.csv`  

Submission file generated:

```
/submissions/baseline_submission.csv
```

---

## 🏆 7. Leaderboard Performance

**Baseline Score:** `0.93913`  
**Leaderboard Rank:** `100` (first submission)

This validates:
- correct preprocessing  
- correct model behavior  
- correct submission format  

The baseline is intentionally simple and performs close to the majority baseline due to class imbalance.

---

## 📌 8. Key Takeaways

- The dataset is **3-class**, not 4-class (H, L, None).  
- The correct dataset is in `/new_competition_data`, not `/competition_data`.  
- SVD is mandatory for baseline training due to feature width.  
- The baseline confirms the full pipeline works — the next steps will improve performance.

---

## 🚀 9. Next Steps

Planned improvements:

- Add class weighting (`class_weight='balanced'`)  
- Ticker-aware CV splits  
- Remove SVD and use LightGBM directly (it handles sparse vectors well)  
- Engineer lag + rolling window features  
- Try CatBoost for categorical handling  
- Build a global vs ticker-specific ensemble  

This notebook marks the **successful completion of the Baseline Phase (v0.1.0)**.
