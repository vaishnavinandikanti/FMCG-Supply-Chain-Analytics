# FMCG Supply Chain Operations & Inventory Intelligence Dashboard

[Dashboard Preview]

<img width="1465" height="858" alt="Dashboard" src="https://github.com/user-attachments/assets/3873a227-d3c3-4335-9714-8c3af85991ee" />

## 📌 Project Overview
An end-to-end data analytics project simulating a real-world FMCG supply chain operation. The goal was to transform messy ERP/SAP-style data into an interactive dashboard that uncovers logistics bottlenecks and inventory inefficiencies.

## 🛠️ Tech Stack
- **Database:** Azure SQL Edge (Docker), SQL Server
- **Data Processing:** Python (pandas, pymssql, SQLAlchemy)
- **Reporting:** Advanced Spreadsheet Reporting (Google Sheets / Excel), Tableau Public

## 📊 Data Pipeline
1. **Ingestion:** Extracted 180K+ rows of raw transactional data from CSV into a Dockerized SQL Server.
2. **Cleaning & Transformation:** Used SQL to handle missing values, remove duplicates, and create calculated metrics (e.g., Delivery Delay Days).
3. **Data Modeling:** Built a Star Schema with `FactOrders`, `DimProducts`, `DimCustomers`, and `DimDate` tables.
4. **Visualization:** Developed an interactive Tableau dashboard to track delivery performance, profitability, and order trends.

## 🔍 Key Insights
- **Logistics Bottleneck:** Identified **98,977 late deliveries**, with **Standard Class** shipping accounting for the vast majority.
- **Profitability:** Analyzed sales and profit margins across 50+ product categories.
- **Seasonality:** Tracked order trends over time to identify peak sales periods.

## 🚀 How to Run
1. Start the Azure SQL Edge Docker container (`docker start sqlserver`).
2. Run the Python ingestion scripts (`01_profile_data.py` through `05_export_to_excel.py`).
3. Open the `.twbx` file in Tableau Public to explore the interactive dashboard.
