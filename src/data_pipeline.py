import pandas as pd
import numpy as np
import os

# ---------------------------
# 1️) Load Raw Data
# ---------------------------
def load_raw_data(file_path: str) -> pd.DataFrame:
    """
    Load raw CSV file into a pandas DataFrame.
    """
    df = pd.read_csv(file_path, encoding="latin1")
    df_raw = df.copy()  # keep original copy for traceability
    return df_raw

# ---------------------------
# 2️) Schema Validation & Type Conversion
# ---------------------------
def validate_schema(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ensure all required columns exist and convert types.
    """
    expected_columns = [
        "InvoiceNo", "StockCode", "Description", 
        "Quantity", "InvoiceDate", "UnitPrice", 
        "CustomerID", "Country"
    ]
    missing_cols = [col for col in expected_columns if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing columns: {missing_cols}")
    
    # Type conversions
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")
    df["CustomerID"] = df["CustomerID"].astype(str)
    
    return df

# ---------------------------
# 3️) Flag Cancellations
# ---------------------------
def flag_cancellations(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add a flag for invoices that start with 'C' indicating cancellations.
    """
    df["IsCancellation"] = df["InvoiceNo"].astype(str).str.startswith("C")
    return df

# ---------------------------
# 4️) Handle Missing CustomerID
# ---------------------------
def handle_missing_customer(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fill missing CustomerID as 'ANONYMOUS' instead of dropping rows.
    """
    # Step 1: Convert to string
    df["CustomerID"] = df["CustomerID"].astype("str")

    # Step 2: Replace "nan" or empty strings with NaN, then fill
    df["CustomerID"] = df["CustomerID"].replace(["nan", ""], np.nan)
    df["CustomerID"] = df["CustomerID"].fillna("ANONYMOUS")
    return df

# ---------------------------
# 5) Feature Engineering
# ---------------------------
def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add TotalPrice and extract Year, Month, Day from InvoiceDate.
    TotalPrice will be negative for returns/cancellations.
    """
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]
    df["Year"] = df["InvoiceDate"].dt.year
    df["Month"] = df["InvoiceDate"].dt.month
    df["Day"] = df["InvoiceDate"].dt.day
    return df

# ---------------------------
# 6) Deduplication
# ---------------------------
def remove_exact_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove exact duplicate rows (all columns identical).
    """
    df_clean = df.drop_duplicates()
    return df_clean

# ---------------------------
# 7) Data Quality Logging
# ---------------------------
def data_quality_report(df_before: pd.DataFrame, df_after: pd.DataFrame):
    """
    Print a simple data quality summary.
    """
    print("Rows before cleaning:", df_before.shape[0])
    print("Rows after cleaning:", df_after.shape[0])
    print("Rows removed:", df_before.shape[0] - df_after.shape[0])
    print("Number of cancellations:", df_after["IsCancellation"].sum())
    print("Number of anonymous customers:", (df_after["CustomerID"] == "ANONYMOUS").sum())

# ---------------------------
# 8) Persist Cleaned Data
# ---------------------------
def save_clean_data(df: pd.DataFrame, file_path: str):
    """
    Save cleaned DataFrame to CSV or Parquet.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df.to_csv(file_path, index=False)
    print(f"Cleaned data saved to {file_path}")

# ---------------------------
def run_pipeline(raw_file_path: str, cleaned_file_path: str) -> pd.DataFrame:
    df_raw = load_raw_data(raw_file_path)
    df = validate_schema(df_raw)
    df = flag_cancellations(df)
    df = handle_missing_customer(df)
    df = feature_engineering(df)
    df = remove_exact_duplicates(df)
    
    # Data quality logging
    data_quality_report(df_raw, df)
    
    # Save cleaned data
    save_clean_data(df, cleaned_file_path)
    
    return df
