
# 📓 Notebook Descriptions

This document provides a high‑level overview of each Jupyter notebook in the project, including its purpose, workflow, and expected contents.

---

## **00_baseline.ipynb**

### **Baseline Purpose**

A fast, minimal pipeline to produce the first valid Kaggle submission.  
Used to confirm the environment, data paths, and submission process work correctly.

### **Baseline High‑Level Contents**

- Load raw `train.csv` and `test.csv`
- Minimal preprocessing (drop metadata, align columns)
- Simple baseline model (Logistic Regression / LightGBM / majority-class predictor)
- Generate `submission_baseline.csv`
- Validate submission format (row count, labels, missing values)

---

## **01_eda.ipynb**

### **EDA Purpose**

Perform light exploratory data analysis to quickly understand the dataset.

### **EDA High‑Level Contents**

- Inspect dataset shape, types, memory usage
- Analyze class distribution (`H`, `L`, `None`)
- Quick look at metadata (`ticker_id`, `t`)
- Initial high-level feature distribution checks
- Save foundational EDA figures to `figures/eda/`

---

## **01_eda_detailed.ipynb**

### **EDA Detailed Purpose**

Conduct deep, portfolio-grade EDA after the competition phase.

### **EDA Detailed High‑Level Contents**

- Time‑series trend analysis across tickers
- Deep dive into engineered features (correlations, clusters)
- Pattern analysis for H/L/None classes
- Rolling-window time series visualizations
- Save advanced EDA outputs for documentation

---

## **02_feature_engineering.ipynb**

### **Feature Engineering Purpose**

Design and build the full feature engineering pipeline.

### **Feature Engineering High‑Level Contents**

- Create lag features (1, 3, 5, 10 periods)
- Rolling mean/std/min/max
- Volatility & momentum indicators
- Signal descriptor utilities (0/1 conversion)
- Align final engineered train/test datasets
- Export:
  - `train_features.csv`
  - `test_features.csv`

---

## **03_model_training.ipynb**

### **Model Training Purpose**

Train, tune, and validate machine learning models with the engineered dataset.

### **Model Training High‑Level Contents**

- Time‑series aware train/validation split
- Baseline + advanced models (LightGBM, CatBoost, ensembles)
- Compute evaluation metrics:
  - Macro F1
  - Balanced Accuracy
  - MCC
- Hyperparameter tuning (optional)
- Save trained models to `models/`
- Generate model candidate submissions

---

## **04_interpretation.ipynb**

### **Interpretation Purpose**

Explain and interpret model behavior using modern interpretability techniques.

### **Interpretation High‑Level Contents**

- SHAP global + per-class explanations
- Feature importance ranking
- Ticker‑specific behavior insights
- Confusion matrices & error analysis
- Generate interpretability plots for final documentation

---

## 📌 Notebook Workflow Overview

These notebooks follow a clean, linear, reproducible pipeline:

1. **00_baseline.ipynb** → Quick baseline submission  
2. **01_eda.ipynb** → Initial understanding  
3. **01_eda_detailed.ipynb** → Deep dive  
4. **02_feature_engineering.ipynb** → Build feature set  
5. **03_model_training.ipynb** → Train & evaluate models  
6. **04_interpretation.ipynb** → Explain final models  

This structure ensures the project remains organized, professional, and portfolio-ready.

---
