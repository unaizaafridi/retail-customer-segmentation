## Dataset Source

The dataset used in this project is the **Online Retail Dataset**, obtained from Kaggle.  
It contains transactional data from a UK-based online retail store, including invoices, products, quantities, prices, customer IDs, and countries.

**Source:**  
🔗 https://www.kaggle.com/datasets/ulrikthygepedersen/online-retail-dataset/data


# Step 1: 

## Dataset Description

The dataset contains **transaction-level retail sales data**, which contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail.The company mainly sells unique all-occasion gifts. Many customers of the company are wholesalers.

Each row represents a **single product item purchased** as part of a customer invoice. It includes information related to invoices, products, customers, pricing, and geographic location.

## Column Descriptions

| Column Name | Description |
|------------|-------------|
| **InvoiceNo** | Invoice number. Nominal; a 6-digit integral number uniquely assigned to each transaction. If the code starts with the letter **'C'**, it indicates a cancelled transaction. |
| **StockCode** | Product (item) code. Nominal; a 5-digit integral number uniquely assigned to each distinct product. |
| **Description** | Product (item) name. Nominal. |
| **Quantity** | Quantity of each product per transaction. Numeric. |
| **InvoiceDate** | Invoice date and time. Numeric; represents the day and time when each transaction was generated. |
| **UnitPrice** | Unit price of the product. Numeric; price per unit in sterling (GBP). |
| **CustomerID** | Customer identification number. Nominal; a 5-digit integral number uniquely assigned to each customer. |
| **Country** | Country name. Nominal; the country where each customer resides. |

### Notes
- Transactions with invoice numbers starting with **'C'** represent cancellations and may require special handling during data cleaning.
- Negative quantities (if present) typically indicate returned items.

### Key Characteristics

- The dataset is recorded at **item-level granularity**, allowing detailed sales and revenue analysis.
- A single invoice may contain **multiple products**, enabling basket-level insights.
- Timestamped transactions support **trend and seasonality analysis**.
- Customer identifiers enable **Customer Lifetime Value (CLV)** calculation and **customer segmentation**.

### Relevance for Analysis

This dataset closely resembles real-world retail transaction data and is well-suited for:
- Sales performance analysis  
- Customer behavior analysis  
- Customer segmentation using clustering techniques  
- Revenue trend and seasonality analysis  
- Business-driven decision making

---

# Step 2:

## Retail Data Cleaning Pipeline

This pipeline performs **end-to-end cleaning and preparation** of the retail dataset, designed to reflect **real-world ETL and data engineering practices**.

### Pipeline Steps

1. **Load Raw Data**  
   - Load the original CSV from `/data/raw`  
   - Preserve a raw copy for traceability

2. **Schema Validation & Type Conversion**  
   - Ensure all required columns are present  
   - Convert types:
     - `InvoiceDate → datetime`
     - `CustomerID → string`

3. **Flag Cancellations**  
   - Add a boolean column `IsCancellation` for invoices starting with 'C'  
   - Allows analysis of returns/cancellations without removing data

4. **Handle Missing CustomerID**  
   - Fill missing `CustomerID` values with `"ANONYMOUS"`  
   - Preserves data while differentiating unregistered customers

5. **Handle Negative Quantity/UnitPrice**  
   - Preserve negative values as they indicate returns or cancellations  
   - Analysis can account for sign when computing revenue

6. **Feature Engineering**  
   - Compute `TotalPrice = Quantity × UnitPrice`  
   - Extract `Year`, `Month`, and `Day` from `InvoiceDate`

7. **Deduplication**  
   - Remove only **exact duplicate rows**  
   - Ensures data integrity without losing unique transactions

8. **Data Quality Logging**  
   - Report rows before and after cleaning  
   - Count cancellations and anonymous customers  
   - Ensures traceability and accountability

9. **Persist Cleaned Data**  
   - Save cleaned dataset to `/data/processed/clean_retail.csv`  
   - Ready for downstream analysis or modeling

### Highlights

- ETL-style separation → raw → validated → enriched → cleaned  
- Preserves important business signals (returns, cancellations, anonymous customers)  

---

# Step 3

## Exploratory Data Analysis (EDA)

### Customer Behavior Analysis
Analyzed purchasing patterns using metrics such as **purchase frequency, average order value (AOV), and customer lifetime value (CLV)** to understand customer engagement and revenue contribution.

### Product Analysis
Evaluated product-level performance to identify **top-selling products**, key revenue drivers, and demand trends across the catalog.

### Cancellation Analysis
Examined cancelled transactions to identify **products and customers with high cancellation frequency**, highlighting potential issues in product quality or order fulfillment.

### Geographical Analysis
Analyzed revenue distribution across countries to assess **market concentration** and identify regions with strong sales performance and expansion potential.

### Customer Segmentation
Segmented customers based on **CLV, frequency, and AOV** to distinguish high-value loyal customers from lower-engagement segments, supporting targeted marketing and retention strategies.
