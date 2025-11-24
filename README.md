# 📈 Detecting Reversal Points in U.S. Equities  

>*Kaggle Competition · Time-Series Classification · Portfolio Project*

![Status: In Progress](https://img.shields.io/badge/Status-In%20Progress-yellow?style=flat-square)
![Category: Time Series](https://img.shields.io/badge/Category-Time%20Series-blue?style=flat-square)
![Primary Metric: Macro F1](https://img.shields.io/badge/Primary%20Metric-Macro%20F1-orange?style=flat-square)
![Models: LightGBM | CatBoost](https://img.shields.io/badge/Models-LightGBM%20%7C%20CatBoost-brightgreen?style=flat-square)

---

## 🧠 Overview  

This repository implements a machine learning system to **detect market reversal points**—local highs (H), local lows (L), and non-reversal points—using anonymized U.S. equities data from the Kaggle competition **Detecting Reversal Points in US Equities**.

Reversal detection is essential for:

- trend identification  
- swing-based trading strategies  
- volatility modeling  
- market structure analysis  

The project is executed in **two tracks**:

### **Track A — Competition Submission (Nov 23–Dec 31, 2025)**  

A fast, clean baseline pipeline optimized to meet the competition deadline.

### **Track B — Portfolio Expansion (Jan 1–Feb 15, 2026)**  

A complete quant-grade system featuring advanced engineered features, SHAP analysis, documentation, and production-oriented ML code structure.

---

## 🎯 Objectives  

- Build a reproducible ML pipeline for detecting reversal points  
- Produce a valid Kaggle submission before the deadline  
- Expand the project into a polished portfolio deliverable  
- Explore engineered time-series features (lags, rolling windows, volatility)  
- Apply and interpret multiple model families  
- Deliver a full final report suitable for recruiters and hiring teams  

---

## 🗂️ Project Structure (Overview)  

This repository uses a **modular, production-quality layout** containing:

- Segregated raw and processed data  
- Notebooks for EDA, baseline modeling, feature engineering, and advanced training  
- A structured `/src` directory for reusable code  
- A `/docs` directory for deep technical and portfolio-grade documentation  
- Saved models and metadata  
- Kaggle submissions and figures  

The **complete, authoritative project directory tree** is maintained at:

👉 **`docs/01_architecture/01_project_structure.md`**

This prevents duplication and ensures the README always stays aligned with the canonical structure.

---

## 🧩 Technical Approach  

### **1. Exploratory Data Analysis**

- Light EDA for Kaggle submission  
- Full EDA (Jan) with:
  - rolling window visualization  
  - volatility signatures  
  - swing class distribution analysis  
  - Signal Descriptor behavior  

### **2. Preprocessing**

- Time-based splitting (no leakage)  
- Conversion of boolean descriptors  
- Selective scaling  
- Consistent feature alignment between train/test  

### **3. Feature Engineering (Portfolio Track)**

- Lag features (1, 3, 5, 10 periods)  
- Rolling mean, std, min, max  
- Momentum and returns  
- Volatility features  
- Signal Descriptor interactions  

### **4. Modeling**

- Baseline: Logistic Regression, LightGBM  
- Advanced: LightGBM, CatBoost, ensembles  
- Time-series cross-validation  
- Macro-F1 optimization  
- Threshold tuning  
- SHAP values + model interpretability  

---

## 🏆 Competition Results  

**Status:** Baseline submission planned before Dec 31  

- **Public Leaderboard Score:** *TBD*  
- **Baseline Model:** LightGBM (raw + simple features)  
- **Portfolio Model:** Scheduled for Jan–Feb 2026  

---

## 📅 Project Timeline

| Phase | Dates | Summary |
|------|--------|---------|
| Phase 1 — Setup | Nov 23–24 | Env + repo initialization |
| Phase 2 — Light EDA | Nov 25–27 | Initial exploration |
| Phase 3 — Baseline Preprocessing | Nov 28–30 | Clean & prepare data |
| Phase 4 — Baseline Modeling | Dec 1–10 | Build + evaluate baseline |
| Phase 5 — Holiday Buffer | Dec 11–26 | Light maintenance |
| Phase 6 — Final Submission | Dec 27–31 | Submit & document |
| Phase 7 — Full EDA | Jan 1–10 | Deep time-series exploration |
| Phase 8 — Feature Engineering | Jan 10–25 | Build advanced features |
| Phase 9 — Advanced Modeling | Jan 25–Feb 5 | Train + interpret |
| Phase 10 — Final Report | Feb 5–Feb 15 | Portfolio packaging |

More detail available in:

👉 `docs/00_overview/reversal_points_project_plan.md`

---

## 🔧 Environment Setup  

### **Conda Environment**

```bash
conda env create -f environment.yml
conda activate reversal_points
```

### Includes

- numpy, pandas, scikit-learn  
- lightgbm, xgboost, catboost  
- optuna + optuna-integration  
- ipywidgets (required for Optuna visualization)  
- matplotlib, seaborn  

### **Kaggle CLI**

```bash
kaggle competitions download -c detecting-reversal-points-in-us-equities
```

---

## 📤 Submissions  

All competition submission files are stored under:

```text
/submissions/
    submission_baseline.csv
    submission_final.csv
```

---

## 📚 Final Report (Coming Feb 2026)

The final report will include:

- Feature engineering breakdown  
- SHAP and importance analysis  
- Modeling performance  
- Error analysis  
- Portfolio narrative and insights  

---

## 🤝 Contributions  

The project is open to collaboration and feedback on:

- feature engineering  
- validation methods  
- time-series modeling  
- code architecture  

---

## 📜 License  

MIT License
See `LICENSE` for details.
