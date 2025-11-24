# 🧭 Project Plan — Detecting Reversal Points in US Equities

**Competition Dates:** Started — Ends December 31, 2025  
**Repository:** `Kaggle-Detect-Reversal-Points-in-US-Equities`  
**Goal:** Build, submit, and later expand a machine learning model to detect swing highs and lows in anonymized U.S. equities data.

---

## **Phase 1 — Project Setup & Environment (Nov 23–24)**

**Objectives:**

- Initialize the repository and establish reproducible infrastructure.
- Prepare the development environment and structure for the project.

**Key Tasks:**

- [x] Create repo with `.gitignore`, `environment.yml`, and `requirements.txt`.
- [x] Add `README.md` and `docs/reference.md`.
- [x] Configure Kaggle CLI authentication.
- [x] Establish directory structure (`data/`, `notebooks/`, `src/`, `models/`, `docs/`).
- [x] Add the project plan and initial documentation.

**Deliverables:**

- Repository initialized  
- Fully configured environment  
- Documented directory structure  

---

## **Phase 1.5 — Baseline Pipeline Sanity Check (Nov 24–25)**

**Duration:** 1 day

**Objectives:**
Validate the full pipeline end-to-end with the simplest possible model.

**Key Tasks:**

- [x] Create 00_baseline.ipynb
- [ ] Load raw train/test
- [ ] Minimal preprocessing (drop non-features, align columns)
- [ ] Train a trivial model (LogReg, LightGBM defaults, or majority class)
- [ ] Generate submission_baseline.csv
- [ ] Submit to Kaggle via CLI to confirm workflow
- [ ] Document baseline score in README

**Deliverables:**

- `00_baseline.ipynb`
- `submission_baseline.csv`
- Verified end-to-end submission pipeline

---

## **Phase 2 — Data Understanding & Exploration (Nov 25–27)**

**Objectives:**

- Conduct light exploration of the dataset to prepare for baseline modeling.
- Identify key feature groups, including raw price features and Signal Descriptors.

**Key Tasks:**

- [ ] Load raw training and test datasets.
- [ ] Summarize descriptive statistics and feature types.
- [ ] Visualize key distributions and relationship patterns.
- [ ] Document findings with initial plots in `01_eda.ipynb`.

**Deliverable:**

- Light EDA notebook with figures saved under `/figures/eda/`.

---

## **Phase 3 — Baseline Data Cleaning & Preprocessing (Nov 28–30)**

**Objectives:**

- Prepare data for baseline model development while ensuring no leakage.

**Key Tasks:**

- [ ] Implement time-based train/validation split.
- [ ] Convert boolean Signal Descriptors to 0/1.
- [ ] Scale selected numeric features where relevant.
- [ ] Align train/test feature sets.
- [ ] Export preprocessed datasets to `/data/processed/`.

**Deliverables:**

- `train_baseline.csv`  
- `test_baseline.csv`

---

## **Phase 4 — Baseline Model Development (Dec 1–10)**

**Objective:**  
Develop, validate, and submit a baseline model suitable for the competition deadline.

---

### **Model Training & Baselines**

- [ ] Logistic Regression baseline  
- [ ] LightGBM baseline  
- [ ] Evaluate using Macro F1-score (primary), Balanced Accuracy, and MCC  
- [ ] Simple threshold tuning  
- [ ] Save baseline model and metadata  

### **Documentation**

- [ ] Update modeling notes in `03_model_training.ipynb`
- [ ] Save baseline performance plots (confusion matrices, F1 by class)

**Deliverables:**

- `baseline_model.pkl`  
- `threshold_metadata.json`  
- `submission_baseline.csv`

---

## **Phase 5 — Holiday Buffer (Dec 11–26)**

**Objectives:**

- Maintain momentum during a period of low availability.
- Perform light improvements and housekeeping tasks.

**Key Tasks:**

- [ ] Clean and reorganize notebooks.
- [ ] Evaluate one additional simple model (optional).
- [ ] Update README with competition progress.

No major deliverables expected.

---

## **Phase 6 — Final Submission & Documentation (Dec 27–31)**

**Objectives:**  
Finalize baseline model, produce final submission, and document competition results.

**Key Tasks:**

- [ ] Validate model performance using strict time-based splitting.
- [ ] Generate `submission.csv` in required Kaggle format.
- [ ] Submit final file via Kaggle CLI.
- [ ] Record leaderboard result and update README.
- [ ] Tag repo: `v0.1.0-baseline-submission`.

**Deliverables:**

- `submission.csv`  
- Updated README with leaderboard score  
- Completed baseline modeling summary  

---

## 📘 **TRACK B — Portfolio Build (Post-Competition)**  

**Timeline:** *January 1 – February 15, 2026*  
This section refines the project into a polished, professional, portfolio-grade repository.

---

## **Phase 7 — Full EDA & Time-Series Investigation (Jan 1–Jan 10)**

**Objectives:**

- Perform deep EDA to understand market structure.
- Build foundation for advanced feature engineering.

**Key Tasks:**

- [ ] Visualize rolling windows, volatility, and local extrema.
- [ ] Study patterns in the four swing classes.
- [ ] Document findings thoroughly.

**Deliverable:**

- `01_eda_detailed.ipynb`  

---

## **Phase 8 — Advanced Feature Engineering (Jan 10–Jan 25)**

**Objectives:**

- Build a comprehensive set of time-series features.

**Key Tasks:**

- [ ] Lag features (1, 3, 5, 10 periods)  
- [ ] Rolling mean, std, min, max  
- [ ] Returns, momentum, volatility indicators  
- [ ] Signal Descriptor interactions  
- [ ] Export engineered datasets  

**Deliverable:**

- `train_features.csv`, `test_features.csv`

---

## **Phase 9 — Advanced Model Development (Jan 25–Feb 5)**

**Objectives:**

- Train and evaluate advanced models suitable for final portfolio presentation.

**Key Tasks:**

- [ ] Train LightGBM, CatBoost, and ensembles  
- [ ] Time-series cross-validation  
- [ ] SHAP & feature importance analysis  
- [ ] Optional: GRU or CNN-based models  

**Deliverable:**

- `03_model_training.ipynb`  
- `models/tuned_model.pkl`

---

## **Phase 10 — Final Documentation & Portfolio Packaging (Feb 5–Feb 15)**

**Objectives:**

- Complete final project documentation and prepare the repository for publication.

**Key Tasks:**

- [ ] Final report (`docs/final_report.md`)  
- [ ] Architecture diagrams  
- [ ] Lessons learned section  
- [ ] Final repository cleanup  
- [ ] Tag release: `v1.0.0`  

**Deliverables:**

- Fully polished, portfolio-ready repository  

---

## 📅 **Milestones**

| Date (2025–2026) | Milestone | Deliverable |
|------------------|-----------|-------------|
| Nov 24 | Environment setup complete | Repo initialized |
| Nov 27 | Light EDA completed | `01_eda.ipynb` |
| Nov 30 | Baseline preprocessing completed | Processed data |
| Dec 10 | Baseline model completed | `submission_baseline.csv` |
| Dec 31 | Final competition submission | Updated README |
| Jan 10 | Full EDA completed | Detailed notebook |
| Jan 25 | Feature engineering completed | Engineered datasets |
| Feb 5 | Advanced modeling completed | Tuned model |
| Feb 15 | Portfolio version complete | Final report + repo cleanup |

---

## ⭐ **Optional Enhancements**

- Include MLflow or Weights & Biases experiment tracking  
- Add Dockerfile for reproducibility  
- Build a Streamlit dashboard for model interpretability  
- Add Makefile for automation  
