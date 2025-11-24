# Project Structure

The project is organized into the following main directories and files:

```plaintext
DETECT_REVERSAL_POINTS_US_EQUITIES/
│
├── data/                               # All data lives here (never commit raw Kaggle data)
│   ├── raw/                            # Original data downloaded from Kaggle
│   │   ├── train.csv       
│   │   ├── test.csv        
│   │   └── sample_submission.csv       
│   └── processed/                      # Cleaned + feature-engineered datasets
│       ├── train_baseline.csv      
│       ├── test_baseline.csv       
│       ├── train_features.csv      
│       └── test_features.csv       
│       
├── docs/                               # Full project documentation (portfolio-ready)
│   ├── 00_overview/
│   │   └── 01_reversal_points_project_plan.md    # Your project roadmap
│   │
│   ├── 01_architecture/
│   │   ├── 00_system_overview.md       # High-level architecture of your project
│   │   ├── 01_project_structure.md     # This file: detailed project structure
│   │   ├── 02_folder_explanations.md   # Descriptions of each folder's purpose
│   │   ├── 03_data_flow.md             # How data moves through your pipeline
│   │   ├── 04_feature_design.md        # Description of time-series features
│   │   └── 05_modeling_pipeline.md     # How models are trained & validated
│   │
│   ├── 02_dataset/
│   │   └── 01_dataset_description.md   # Dataset details & schema
│   │
│   ├── 03_helper_README/
│   │   └── 01_environment_setup.md     # Conda environment, pip installs, ipywidgets notes
│   │
│   ├── 04_final_report/
│   │   ├── 01_executive_summary.md     # Portfolio-facing summary
│   │   ├── 02_model_results.md         # Final metrics & insights
│   │   ├── 03_interpretability.md      # Feature importance, SHAP, charts
│   │   └── 04_lessons_learned.md       # Reflections after Jan-Feb deep dive
│   │
│   └── 05_references/
│       ├── 01_kaggle_competition_link.md
│       ├── 02_time_series_notes.md
│       └── 03_quant_references.md
│
├── figures/                            # Save all charts & plots here
│   ├── eda/
│   ├── features/
│   └── modeling/
│
├── models/                             # Serialized model artifacts
│   ├── baseline_model.pkl
│   ├── tuned_model.pkl
│   └── threshold_metadata.json
│
├── notebooks/                          # Jupyter notebooks in clean, linear order
│   ├── 00_baseline.ipynb               # Quick baseline → Kaggle submission
│   ├── 01_eda.ipynb                    # Light analysis for submission
│   ├── 01_eda_detailed.ipynb           # Deep EDA (Jan–Feb portfolio version)
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_interpretation.ipynb
│
├── src/                                # Python modules (clean, reusable)
│   ├── data/       
│   │   ├── load.py                     # Load Kaggle/raw data safely
│   │   └── preprocess.py               # Basic preprocessing for baseline
│   │       
│   ├── features/       
│   │   ├── make_features.py            # Lag features, rolling stats, momentum
│   │   └── descriptors.py              # Clean utilities for boolean signal descriptors
│   │       
│   ├── models/     
│   │   ├── train_baseline.py           # Baseline model script
│   │   ├── train_advanced.py           # Full feature + cross-val training
│   │   └── evaluation.py               # Macro-F1, MCC, Balanced Acc helpers
│   │       
│   └── utils/      
│       ├── io.py                       # Save/load helpers for datasets & models
│       ├── validation.py               # Time-series split helpers
│       └── seed.py                     # RNG seeding for reproducibility
│       
├── submissions/                        # All Kaggle submission files
│   ├── submission_baseline.csv     
│   └── submission_final.csv        
│       
├── environment.yml                     # Conda environment (w/ ipywidgets + optuna)
├── requirements.txt                    # For pip users or Kaggle notebooks
├── Makefile                            # Optional: shortcuts (train, predict, etc.)
├── .gitignore                          # Ignore data, models, etc.
└── README.md                           # Main project README (competition, submission, results)
```

## Directory Descriptions

- `data/`: Contains all datasets, both raw and processed. Raw data should never be committed to version control.
- `docs/`: Comprehensive documentation for the project, including architecture, data flow, feature design, and final reports.
- `figures/`: Directory for saving all visualizations, charts, and plots generated during analysis.
- `models/`: Serialized model files and related metadata for easy loading and deployment.
- `notebooks/`: Jupyter notebooks used for exploration, feature engineering, model training, and interpretation.
- `src/`: Python modules organized by functionality, including data loading, feature engineering, modeling, and utility functions.
- `submissions/`: Contains all Kaggle submission files generated during the project.
- `environment.yml` and `requirements.txt`: Files for setting up the project environment using Conda or pip.
- `Makefile`: Optional file for automating common tasks like training and prediction.
- `.gitignore`: Specifies files and directories to be ignored by version control.
- `README.md`: The main README file providing an overview of the project, competition details, and results.

This structure ensures a clean, organized, and reproducible workflow for the project, facilitating collaboration and future maintenance.
