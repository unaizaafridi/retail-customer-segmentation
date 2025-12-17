## 📦 Dataset Description

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
