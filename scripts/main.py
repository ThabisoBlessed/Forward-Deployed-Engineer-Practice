import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / "data" / "prodeliver_assessment.db"

con = sqlite3.connect(DB_PATH)

# List database tables
tables = pd.read_sql("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
""", con)

print("DATABASE TABLES")
print(tables)

# Preview orders
df = pd.read_sql("SELECT * FROM orders LIMIT 5", con)

print("\nORDERS PREVIEW")
print(df)

con.close()


# Preview orders
df = pd.read_sql("SELECT * FROM orders LIMIT 5", con)