"""
Utility functions for loading large CSV datasets using DuckDB.

Handles:
- Project root discovery
- Automatic high max_line_size for wide CSVs (competition dataset)
- Clean API: load_train(), load_test(), load_csv()
- Optional return types: DuckDB Relation or Pandas DataFrame
"""

import os
import duckdb
from pathlib import Path


# ------------------------------------------------------------
# Helper: Detect project root (directory containing 'data/')
# ------------------------------------------------------------
def get_project_root() -> Path:
    """Return the absolute path to the project root directory."""
    current = Path(__file__).resolve()

    for parent in current.parents:
        if (parent / "data").exists():
            return parent

    raise RuntimeError("Project root not found (could not locate 'data/' folder).")


# ------------------------------------------------------------
# Helper: Load any CSV file through DuckDB
# ------------------------------------------------------------
def load_csv(relative_path: str, as_df: bool = True, max_line_size: int = 5_000_000):
    """
    Load a CSV using DuckDB with safe defaults for huge, wide files.

    Parameters
    ----------
    relative_path : str
        Path relative to project root (e.g., 'data/raw/.../train.csv')
    as_df : bool
        If True: return a pandas DataFrame
        If False: return a DuckDB Relation
    max_line_size : int
        Max allowed line length (needed for the enormous header row)

    Returns
    -------
    DataFrame or duckdb.Relation
    """
    project_root = get_project_root()
    full_path = project_root / relative_path

    if not full_path.exists():
        raise FileNotFoundError(f"Could not find file at: {full_path}")

    con = duckdb.connect()
    con.execute(f"SET max_line_size={max_line_size}")

    query = f"""
        SELECT *
        FROM read_csv_auto('{full_path.as_posix()}')
    """

    rel = con.sql(query)

    return rel.df() if as_df else rel


# ------------------------------------------------------------
# Public functions: Load train/test data
# ------------------------------------------------------------

def load_train(as_df: bool = True):
    """Load the competition train.csv."""
    return load_csv("data/raw/competition_data/train.csv", as_df=as_df)


def load_test(as_df: bool = True):
    """Load the competition test.csv."""
    return load_csv("data/raw/competition_data/test.csv", as_df=as_df)


# ------------------------------------------------------------
# Optional: Load sample submission
# ------------------------------------------------------------
def load_sample_submission(as_df: bool = True):
    """Load sample_submission.csv if present."""
    return load_csv("data/sample_submissions/sample_submission.csv", as_df=as_df)
