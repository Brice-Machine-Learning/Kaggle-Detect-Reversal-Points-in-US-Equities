"""
src/data/eda_utils.py
---------------------
Utility helper function to analyze and group columns in a dataframe.
"""

import duckdb
import pandas as pd

def get_prefix_counts(df: pd.DataFrame, table_name: str = "tbl") -> pd.DataFrame:
    """
    Analyze a wide DataFrame by grouping its column names by prefix (text before first underscore).

    This function:
    - Registers the DataFrame as a DuckDB table
    - Extracts column names through a temporary DuckDB relation
    - Performs fast SQL-based prefix grouping
    - Returns a DataFrame sorted by descending feature count

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame whose columns will be analyzed.
    table_name : str, optional
        The name to assign to the DuckDB-registered table (default="tbl").

    Returns
    -------
    pd.DataFrame
        A DataFrame with two columns:
        - prefix : extracted text before first underscore
        - count : number of columns sharing that prefix
    """

    # Register pandas DataFrame into DuckDB
    duckdb.register(table_name, df)

    # Create a temporary table of column names
    col_df = pd.DataFrame({"column_name": df.columns})
    duckdb.register("cols", col_df)

    # Perform prefix grouping SQL
    query = """
        SELECT
            regexp_extract(column_name, '^[^_]+') AS prefix,
            COUNT(*) AS count
        FROM cols
        GROUP BY prefix
        ORDER BY count DESC
    """

    return duckdb.query(query).df()
