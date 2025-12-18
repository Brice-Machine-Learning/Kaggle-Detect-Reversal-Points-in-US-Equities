# 🧩 Feature Engineering — Progress Summary (Tier 1)

**Notebook:** `02_feature_engineering.ipynb`  
**Scope:** Train set only  
**Status:** Tier 1 features stabilized and checkpointed  
**Hardware Context:** CPU-only, legacy laptop (no GPU)

---

## 🎯 Objective (Tier 1)

The goal of Tier 1 feature engineering is to construct **lightweight, leakage-safe, time-aware baseline features** that:

- Validate signal usefulness before feature explosion
- Respect strict temporal ordering per `ticker_id`
- Are computationally feasible on constrained hardware
- Can be checkpointed and resumed without reprocessing raw data

This phase intentionally avoids:
- Rolling windows
- Heavy SQL window engines
- Feature proliferation
- Test-set processing

---

## 📊 Dataset Context

- **Rows (train):** 2,683  
- **Columns:** ~68,500  
- **Column composition:**
  - ~68,499 boolean signal descriptor columns
  - 1 datetime column (time axis)
  - Identifiers: `ticker_id`
  - Target: `class_label`

The dataset is **extremely wide**, making naive SQL window operations and full DataFrame copies impractical on CPU-only hardware.

---

## 🧠 Key Engineering Decisions

### 1. Tooling Strategy (Revised)

| Task | Tool | Rationale |
|---|---|---|
| Wide boolean aggregation | `pandas` | Vectorized, in-memory, fastest for this operation |
| Simple lag features | `pandas.groupby().shift()` | Touches only a few columns; avoids full-row window materialization |
| SQL / DuckDB | Deferred | Too expensive on full wide table for Tier 1 |
| Persistence | `pickle` | Zero dependencies, restart-safe, fast for wide frames |

This hybrid approach prioritizes **practical performance over ideological purity**.

---

### 2. Temporal Integrity

- Data is **explicitly sorted** by:
  ```text
  ticker_id → time
  ```
- Stable sorting (`mergesort`) was used to preserve deterministic ordering
- Temporal features are derived **only from prior observations**
- No forward-looking leakage is introduced

The final ordering was validated via:
```python
train_df.index.is_monotonic_increasing  # True
```

---

## 🧩 Tier 1 Features Implemented

### Signal Population Features
Computed via vectorized pandas operations:

- `signal_count`
- `signal_density`

### Lagged Features (Leakage-Safe)

- `signal_count_lag1`
- `signal_density_lag1`

---

## 💾 Checkpointing Strategy (Critical)

Stable checkpoint created:

```
data/processed/train_sorted_checkpoint.pkl
```

- Preserves row order
- Restart-safe
- No external dependencies

---

## 🚫 Explicitly Deferred

- Test set feature engineering
- Rolling window features
- Model training
- Feature pruning

---

## ✅ Current State

- ✔ Tier 1 features computed
- ✔ Temporal ordering validated
- ✔ Checkpoint written
- ✔ Ready for next phase
