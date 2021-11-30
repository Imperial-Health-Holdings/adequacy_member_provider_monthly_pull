
import pyodbc
import pandas as pd

conn = pyodbc.connect(
    r'Driver=ODBC Driver 17 for SQL Server;'
    r'SERVER=ihpas-ezcaprpt;'
    r'Trusted_Connection=yes;'
)

qry = '''SELECT TOP 5 * FROM H2793.dbo.claim_masters_v'''

df = pd.read_sql(qry, conn)

print(df.head())