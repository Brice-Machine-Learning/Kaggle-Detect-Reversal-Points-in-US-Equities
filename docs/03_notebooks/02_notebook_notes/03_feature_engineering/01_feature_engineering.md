## 🛠️ Feature Engineering Roadmap

This section outlines the structured, leakage-aware approach used to construct time-series features for reversal point detection. Feature engineering is performed with a **DuckDB-first workflow** to ensure scalability, reproducibility, and strict temporal integrity across an extremely wide feature space.

The objective is not to maximize feature count, but to **transform sparse, event-based signals into informative, temporally valid predictors** suitable for tree-based and ensemble models.

---

### 1️⃣ Dataset Ingestion & Temporal Ordering

**Objective:**  
Load baseline-clean datasets and establish a strict temporal foundation for all downstream feature construction.

**Key Principles:**
- Operate exclusively on validated baseline datasets
- Enforce ordering by `ticker_id` and time index
- Prevent any cross-ticker or cross-time leakage

**Actions:**
- Register training and test datasets in DuckDB
- Verify monotonic time ordering within each ticker
- Confirm alignment of train/test schemas prior to feature creation

> _All subsequent feature logic assumes correct temporal ordering at this stage._

---

### 2️⃣ Feature Group Definition & Scope Control

**Objective:**  
Explicitly define which classes of features are permitted, ensuring consistency and interpretability.

**Feature groups include:**
- Lagged event indicators
- Rolling window aggregations
- Event-proximity context features
- Cross-signal aggregate measures

**Out of scope:**
- Forward-looking features
- Any feature requiring knowledge of future target labels
- Arbitrary feature interactions without domain justification

This scope definition acts as a guardrail against feature leakage and uncontrolled dimensionality growth.

---

### 3️⃣ Lagged Signal Descriptor Features

**Objective:**  
Transform sparse boolean Signal Descriptor columns into time-aware predictors.

**Rationale:**
Reversal signals often exert influence *after* their occurrence. Lagged features capture this delayed effect without introducing contemporaneous bias.

**Approach:**
- Generate fixed lag intervals (e.g., 1, 3, 5 bars)
- Apply lags independently within each `ticker_id`
- Preserve original signal sparsity characteristics

These features allow models to learn how prior signal activations influence future reversal probabilities.

---

### 4️⃣ Rolling Window Signal Density Features

**Objective:**  
Convert sparse event indicators into continuous measures of recent market activity.

**Rationale:**
Individual signals may be weak predictors in isolation. Their *recent density* often provides stronger contextual information.

**Examples:**
- Rolling sum of signal activations
- Rolling mean of boolean flags (activation frequency)
- Window sizes chosen to balance responsiveness and stability

All rolling computations exclude the current timestep to maintain strict causality.

---

### 5️⃣ Event-Aware Context Features (Leakage-Safe)

**Objective:**  
Incorporate historical target context without accessing future information.

**Permitted constructs:**
- Time elapsed since last observed swing high
- Time elapsed since last observed swing low

**Prohibited constructs:**
- Distance to next event
- Any feature derived from future target values

These features provide regime awareness (trend maturity, consolidation phases) while preserving temporal validity.

---

### 6️⃣ Cross-Signal Aggregate Features

**Objective:**  
Reduce effective dimensionality while preserving informational content.

**Motivation:**
The dataset contains a very large number of boolean signal descriptors. Aggregate features capture overall market signal intensity without requiring models to parse each signal independently.

**Examples:**
- Count of active signals per timestep
- Rolling count of any signal activation
- Rolling proportion of signals firing

These features often serve as robust proxies for market state and volatility regimes.

---

### 7️⃣ Feature Validation & Leakage Audits

**Objective:**  
Ensure engineered features are safe, consistent, and model-ready.

**Validation checks include:**
- Null value inspection at series boundaries
- Verification that rolling and lagged features do not incorporate future data
- Schema parity checks between training and test datasets

No dataset is persisted until all validation criteria are met.

---

### 8️⃣ Persistence & Downstream Compatibility

**Objective:**  
Produce stable, reusable feature datasets for modeling and experimentation.

**Deliverables:**
- `/data/processed/train_features.csv`
- `/data/processed/test_features.csv`

These datasets form the **sole inputs** to all advanced modeling pipelines and are treated as immutable artifacts once generated.

---

### 📌 Design Philosophy Summary

This feature engineering workflow prioritizes:
- Temporal correctness over feature volume
- Interpretability over opaque transformations
- Reproducibility over ad-hoc experimentation

The result is a defensible, scalable feature set suitable for both competition submission and long-term portfolio presentation.
