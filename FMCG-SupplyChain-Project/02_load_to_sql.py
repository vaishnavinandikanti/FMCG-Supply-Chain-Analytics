import pandas as pd
from sqlalchemy import create_engine
import pymssql
import time

# ==========================================
# CONFIGURATION - UPDATE YOUR PASSWORD HERE
# ==========================================
DB_PASSWORD = 'Vaish123@' # <--- CHANGE THIS
DB_SERVER = '127.0.0.1'
DB_PORT = '1433'
DB_USER = 'sa'
DB_NAME = 'FMCG_DB'
CSV_FILE = 'DataCoSupplyChainDataset.csv'

# ==========================================
# STEP 1: Create the Database if it doesn't exist
# ==========================================
print("Connecting to master database to create FMCG_DB...")
try:
    # Connect to the default 'master' database first
    conn = pymssql.connect(server=DB_SERVER, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, database='master')
    conn.autocommit(True)
    cursor = conn.cursor()
    
    # Create database
    cursor.execute(f"IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = '{DB_NAME}') CREATE DATABASE {DB_NAME}")
    print(f"Database '{DB_NAME}' is ready.")
    conn.close()
except Exception as e:
    print(f"Error creating database: {e}")
    exit()

# ==========================================
# STEP 2: Load and Clean Column Names for SQL
# ==========================================
print("\nLoading CSV data into pandas...")
df = pd.read_csv(CSV_FILE, encoding='latin-1')

# Drop columns that are entirely empty or irrelevant for supply chain analysis
columns_to_drop = ['Product Description', 'Customer Password', 'Customer Email', 'Product Image', 'Order Zipcode']
df.drop(columns=columns_to_drop, inplace=True, errors='ignore')

# Rename columns to be SQL-friendly (snake_case, no spaces or brackets)
print("Cleaning column names for SQL...")
df.columns = df.columns.str.lower() \
    .str.replace(' ', '_') \
    .str.replace('(', '') \
    .str.replace(')', '') \
    .str.replace('-', '_')

# Convert string dates to actual datetime objects
print("Converting date strings to datetime objects...")
df['order_date_dateorders'] = pd.to_datetime(df['order_date_dateorders'], errors='coerce')
df['shipping_date_dateorders'] = pd.to_datetime(df['shipping_date_dateorders'], errors='coerce')

print(f"Data shape after dropping irrelevant columns: {df.shape}")

# ==========================================
# STEP 3: Ingest into Azure SQL Edge
# ==========================================
print("\nIngesting data into SQL Server. This may take 1-2 minutes...")

# Create the SQLAlchemy engine using pymssql
# Notice the %40 instead of @
engine = create_engine(f'mssql+pymssql://{DB_USER}:{DB_PASSWORD.replace("@", "%40")}@{DB_SERVER}:{DB_PORT}/{DB_NAME}')

# Load data into a table named 'raw_supply_chain'
start_time = time.time()
df.to_sql('raw_supply_chain', engine, if_exists='replace', index=False, chunksize=5000)
end_time = time.time()

print(f"\nSuccess! Data loaded into table 'raw_supply_chain' in {round(end_time - start_time, 2)} seconds.")
print("You can now open VS Code's SQL extension and query this table!")