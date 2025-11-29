
# 🧪 00_baseline_template.md  

>*Notebook Template — Baseline Pipeline Sanity Check*

This template outlines the structure and workflow for the `00_baseline.ipynb` notebook.  
Its purpose is **NOT** modeling, feature engineering, or EDA.  
Its sole purpose is to **validate the pipeline** and generate an initial Kaggle submission.

---

## 📘 **Notebook Purpose**

The baseline notebook is designed to ensure the full workflow operates correctly:

- The data loads without errors  
- Paths are correct and reproducible  
- Kaggle CLI submission works  
- Environment and kernel are stable  
- Train/test columns align  
- A valid submission file can be created  

This is a *system check*, not a data science step.

---

## 📂 **Notebook Structure**

## 1. 📌 Title & Intro

- Title: "00_baseline.ipynb — Baseline Pipeline Sanity Check"
- Brief description of the notebook’s purpose  
- Note that this is a minimal pipeline test, not the real modeling notebook  

---

## 2. 🏗️ Imports & Configuration

Include:

- Standard data science libraries
- pandas / numpy  
- Basic utilities (`Path`, `os`)  
- Seed initialization  
- Path definitions for `data/raw/`  

**No model imports yet.**  
Keep this minimal.

---

## 3. 📥 Load Raw Data

Steps:

- Load `train.csv` and `test.csv` from `data/raw/`  
- Display shapes  
- Display top rows  
- Confirm `class_label` exists only in train  

**Checks to perform:**

- Train/test row count  
- Column mismatches  
- Presence of metadata columns  

---

## 4. 🔍 Minimal Preprocessing

Only the essentials:

- Drop non-feature metadata (`t`, `ticker_id`)  
- Encode categorical features if required  
- Ensure train and test columns match exactly  
- Handle unexpected NaNs if present  

**What NOT to do here:**

- No scaling  
- No time-based splitting  
- No feature engineering  
- No leakage-sensitive ops  

---

## 5. 🤖 Baseline Model (Simple)

Choose one:

- Majority class predictor  
- Logistic Regression with defaults  
- LightGBM with minimal parameters  

Keep it extremely simple — speed > accuracy.

---

## 6. 📊 Generate Predictions

- Predict on the test set  
- Ensure predictions contain only `H`, `L`, `None`  
- Validate class distribution (sanity check)

---

## 7. 📝 Build Kaggle Submission File

Create `submission_baseline.csv`:

- Must contain:  
  `id,class_label`  
- Must have exactly **828** rows  
- No missing values  
- Save to:  
  `submissions/submission_baseline.csv`

---

## 8. 🚀 Kaggle CLI Submission (Optional but recommended)

Steps:

- Ensure Kaggle CLI is configured
- Prepare submission command:

  ```bash
  kaggle competitions submit -c detect-reversal-points-in-us-equities -f submissions/submission_baseline.csv -m "Baseline submission"
  ```

- Use Kaggle CLI to submit the file
- Submit the file via CLI  
- Record the public score  
- Confirm workflow end-to-end  

---

## 9. 📦 Outputs & Artifacts

This notebook should generate:

- `submissions/submission_baseline.csv`

Nothing else.

**No:**

- Models  
- Figures  
- Processed datasets  

---

## 🚫 What NOT To Include in This Notebook

To avoid scope bloat:

- No EDA  
- No feature engineering  
- No time-series logic  
- No model tuning  
- No leakage-checks  
- No feature selection  
- No cross-validation  
- No SHAP or interpretability  

Those belong in later notebooks.

---

## 🧼 Clean-Up Notes

- End the notebook with a short summary (“Baseline submission successfully generated.”)  
- Keep the notebook under 30–40 lines of real work  
- This is NOT a portfolio notebook — just a sanity check  

---
