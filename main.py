import pyodbc
import pandas as pd

import dict_sql_query as sql

conn = pyodbc.connect(
    r'Driver=ODBC Driver 17 for SQL Server;'
    r'SERVER=ihpas-ezcaprpt;'
    r'Trusted_Connection=yes;'
)

df_prov = pd.read_sql(sql.qry_provider, conn)
df_memb = pd.read_sql(sql.qry_member, conn)

