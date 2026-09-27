import pandas as pd
import pymssql

# ==========================================
# CONFIGURATION
# ==========================================
DB_SERVER = '127.0.0.1'
DB_PORT = '1433'
DB_USER = 'sa'
DB_PASSWORD = 'Vaish123@' # Make sure this matches your password
DB_NAME = 'FMCG_DB'
OUTPUT_FILE = 'FMCG_SupplyChain_Report.xlsx'

print("Connecting to SQL Database...")

try:
    # Connect to the database
    conn = pymssql.connect(
        server=DB_SERVER, 
        port=DB_PORT, 
        user=DB_USER, 
        password=DB_PASSWORD, 
        database=DB_NAME
    )
    
    print("Connection successful. Extracting tables...")

    # Read the 4 tables into pandas DataFrames
    fact_orders = pd.read_sql('SELECT * FROM FactOrders', conn)
    dim_products = pd.read_sql('SELECT * FROM DimProducts', conn)
    dim_customers = pd.read_sql('SELECT * FROM DimCustomers', conn)
    dim_date = pd.read_sql('SELECT * FROM DimDate', conn)
    
    conn.close()
    print("Data extracted. Writing to Excel...")

    # Write to Excel with multiple sheets
    with pd.ExcelWriter(OUTPUT_FILE, engine='openpyxl') as writer:
        fact_orders.to_excel(writer, sheet_name='FactOrders', index=False)
        dim_products.to_excel(writer, sheet_name='DimProducts', index=False)
        dim_customers.to_excel(writer, sheet_name='DimCustomers', index=False)
        dim_date.to_excel(writer, sheet_name='DimDate', index=False)

    print(f"Success! File saved as '{OUTPUT_FILE}'")

except Exception as e:
    print(f"An error occurred: {e}")