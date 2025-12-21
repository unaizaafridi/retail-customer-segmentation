import pandas as pd

def prepare_aggregates(cleaned_file):
    """
    Load cleaned retail data and prepare aggregated tables for dashboard.

    Returns:
        monthly_revenue: Revenue by Year & Month
        top_products: Top 10 products by revenue
        country_revenue: Top 10 countries by revenue
        clv: Customer Lifetime Value
    """
    df = pd.read_csv(cleaned_file)
    
    # Feature engineering (if not done in cleaning)
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]
    df["Year"] = df["InvoiceDate"].dt.year
    df["Month"] = df["InvoiceDate"].dt.month
    
    # Aggregated data
    monthly_revenue = df.groupby(["Year", "Month"])["TotalPrice"].sum().reset_index()
    top_products = (
        df.groupby("Description")["TotalPrice"]
          .sum()
          .sort_values(ascending=False)
          .head(10)
          .reset_index()
    )
    country_revenue = (
        df.groupby("Country")["TotalPrice"]
          .sum()
          .sort_values(ascending=False)
          .head(10)
          .reset_index()
    )
    clv = df.groupby("CustomerID")["TotalPrice"].sum().reset_index(name="CLV")
    
    return monthly_revenue, top_products, country_revenue, clv

def save_aggregates(monthly_revenue, top_products, country_revenue, clv, path="../data/aggregated/"):
    monthly_revenue.to_csv(path + "monthly_revenue.csv", index=False)
    top_products.to_csv(path + "top_products.csv", index=False)
    country_revenue.to_csv(path + "country_revenue.csv", index=False)
    clv.to_csv(path + "clv.csv", index=False)
