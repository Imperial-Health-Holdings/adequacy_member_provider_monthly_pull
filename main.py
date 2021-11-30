import os
import pyodbc
import pandas as pd
from datetime import datetime
import dict_sql_query as sql

import configparser
config = configparser.ConfigParser()
config.read('config.ini')

# initialization
path_export = config['PATH']['path_export']

year_month = str(datetime.now().year) + str(datetime.now().month)
path_export_member = os.path.join(path_export, f'member_{year_month}.csv')
path_export_provider = os.path.join(path_export, f'provider_{year_month}.csv')

# establish SQL server connection
conn = pyodbc.connect(
    r'Driver=ODBC Driver 17 for SQL Server;'
    r'SERVER=ihpas-ezcaprpt;'
    r'Trusted_Connection=yes;'
)

# read data from SQL server
df_prov = pd.read_sql(sql.qry_provider, conn)
df_memb = pd.read_sql(sql.qry_member, conn)

# export data
