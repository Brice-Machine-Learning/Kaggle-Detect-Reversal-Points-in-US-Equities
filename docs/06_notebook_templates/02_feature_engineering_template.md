
# ⚙️ 02_feature_engineering_template.md  

>*Notebook Template — Feature Engineering (Competition + Portfolio)*

This notebook builds the **feature engineering pipeline** used by both the baseline model and the advanced models.  
It transforms raw time-series data into meaningful features while avoiding leakage and maintaining chronological integrity.

--

## 🎯 Notebook Purpose

The goal of this notebook is to:

- Build reproducible feature engineering steps  
- Create lag-based, rolling, and volatility features  
- Process boolean descriptors (convert, aggregate, interact)  
- Align processed train/test datasets  
- Export feature-engineered datasets for modeling  

This is a **core notebook** in your pipeline.

---

## 📂 Notebook Structure

## 1. 📌 Title & Introduction

Include:

- Clear title: "Feature Engineering for Reversal Points Detection"
- Short description of notebook purpose  
- Explain dual use for competition and portfolio phases  
- Mention advanced features for portfolio phase

Explain:

- Purpose of FE  
- Why FE is critical for time-series classification  
- Outline the categories of features you will produce  

---

## 2. 🏗️ Imports & Setup

Include:

- Standard imports
- pandas, numpy  
- Feature engineering helpers (if any)  
- Path utilities  
- Seed initialization  
- Only **light** visualization (optional)

---

## 3. 📥 Load Data

Load:

- Raw datasets from `data/raw/`  
- Optional: baseline-processed datasets from Phase 3  

Check:

- Shapes  
- Presence of `class_label` only in train  
- Chronological ordering per ticker  

---

## 4. 🔧 Prepare Data for Feature Engineering

Steps:

- Sort data by `ticker_id` and timestamp  
- Reset index per ticker if necessary  
- Identify categorical vs numeric columns  
- Identify boolean descriptors (0/1 or True/False)  

Document:

- Any assumptions made about data structure
- Feature counts  
- Distribution summary  

---

## 5. 🔁 Lag Features (Time-Based)

Create lagged versions of select columns:

- 1-step lag  
- 3-step lag  
- 5-step lag  
- 10-step lag  

Notes:

- Apply **per ticker**  
- No peeking ahead  
- Drop rows with insufficient history (or pad with NaN and fill)  

---

## 6. 📉 Rolling Window Features

For selected numeric columns, compute:

- Rolling mean (3, 5, 10)  
- Rolling standard deviation  
- Rolling min/max  
- Rolling volatility estimates  
- Rolling range  

Per-ticker, chronological, no leakage.

---

## 7. ⚡ Momentum & Volatility Indicators

Compute basic momentum-like features from anonymized data:

- Differences  
- Percent changes (if valid)  
- Volatility proxies  
- Normalized swings  

These help capture directional structure without raw prices.

---

## 8. 🧱 Boolean Signal Descriptor Processing

For signal descriptor columns:

- Convert to numeric (0/1) if not already  
- Compute rolling frequency windows  
- Compute cumulative counts or runs  
- Create grouped activation features  

These are powerful because descriptors often capture latent patterns.

---

## 9. 🔗 Interaction Features (Optional)

Create 2-way interactions between key feature groups.
Possible interactions:

- Lag × descriptor  
- Descriptor × momentum  
- Volatility × rolling mean  

Keep interactions limited (large feature count already exists).

---

## 10. 🧹 Post-Processing & Dataset Alignment

Steps:

- Ensure identical feature columns in train + test  
- Drop metadata (`t`, `ticker_id`) only after extraction  
- Ensure no leakage  
- Check for NaN introduction  
- Fill NaNs carefully (median, forward fill, per ticker)  

---

## 11. 💾 Export Engineered Datasets

Steps:

- Save processed datasets to CSV:

Save to:

```text
data/processed/train_features.csv
data/processed/test_features.csv
```

Also export:

- Metadata file describing feature groups  
- Logs of feature generation decisions (optional)  

---

## 🚫 What NOT to Include

To keep this notebook focused:
Avoid:

- Model training  
- Validation logic  
- Submission generation  
- SHAP analysis  
- Full correlations on 68k+ features (too heavy)  

This notebook’s focus is cleanly on **creating features**, not using them.

---

## 🧼 Final Notes

End with:

- Summary of engineered features  
- Feature group counts  
- Observations for modeling  
- Notes for future feature expansion  

This notebook forms the **bridge** between data exploration and modeling.

---

## 📄 End of 02_feature_engineering_template
