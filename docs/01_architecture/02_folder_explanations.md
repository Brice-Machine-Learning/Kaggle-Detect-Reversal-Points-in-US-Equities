# 📘 Folder & File Explanations (Project Scaffolding)

## 🗂️ Top-Level Structure

### `data/`

Stores datasets in a structured manner.

- `raw/` – Original, unmodified Kaggle data.  
- `processed/` – Cleaned or feature‑engineered datasets for modeling.  

---

### `docs/`

Contains all project documentation.

#### `00_overview/`

High‑level project planning and roadmap documentation.

#### `01_architecture/`

Technical documentation describing how the system is organized.

- `00_system_overview.md` – Summary of the project architecture  
- `01_data_flow.md` – Explanation of how data moves through the pipeline  
- `02_feature_design.md` – Time‑series feature descriptions (lags, rolling windows, momentum)  
- `03_modeling_pipeline.md` – Modeling, cross‑validation, and evaluation strategy  

#### `03_helper_README/`

Developer setup resources:

- Conda environment setup  
- ipywidgets requirement  
- Kaggle CLI configuration  

#### `04_final_report/`

Portfolio‑grade final documentation:

- Executive summary  
- Final metrics and results  
- Interpretability and SHAP analysis  
- Lessons learned  

#### `05_references/`

External references, research notes, and competition links.

---

### `figures/`

Stores saved plots and figures organized by workflow stage:

- `eda/`  
- `features/`  
- `modeling/`  

---

### `models/`

Serialized machine‑learning artifacts needed for reproducibility:

- Baseline models  
- Tuned models  
- Metadata for thresholding or ensemble logic  

---

### `notebooks/`

Ordered Jupyter notebooks documenting each stage of the pipeline.

- `00_baseline.ipynb` – Rapid baseline used for initial Kaggle submission  
- `01_eda.ipynb` – Light EDA for early investigation  
- `01_eda_detailed.ipynb` – Comprehensive EDA for portfolio version  
- `02_feature_engineering.ipynb` – Creation of lag features, rolling windows, signal descriptors  
- `03_model_training.ipynb` – Model training and evaluation  
- `04_interpretation.ipynb` – SHAP, feature importance, and interpretation  

---

### `src/`

Reusable Python modules for a clean engineering workflow.

#### `src/data/`

- `load.py` – Standardized dataset loading functions  
- `preprocess.py` – Baseline preprocessing pipeline  

#### `src/features/`

- `make_features.py` – Lag features, rolling statistics, momentum indicators  
- `descriptors.py` – Utility functions for handling boolean signal descriptors  

#### `src/models/`

- `train_baseline.py` – Baseline training script  
- `train_advanced.py` – Full time‑series modeling pipeline  
- `evaluation.py` – Macro‑F1, MCC, and Balanced Accuracy evaluation utilities  

#### `src/utils/`

- `io.py` – Helpers for saving and loading datasets/models  
- `validation.py` – Time‑series split and leakage‑prevention utilities  
- `seed.py` – Consistent random seed initialization across libraries  

---

### `submissions/`

Contains all Kaggle submission files:

- Baseline submission  
- Final submission  

---

### Top‑Level Files

- `environment.yml` – Conda environment specification  
- `requirements.txt` – pip‑based dependency list  
- `Makefile` – Automation commands for training, preprocessing, etc.  
- `.gitignore` – Patterns for excluding unnecessary files  
- `README.md` – Project overview and usage information  
