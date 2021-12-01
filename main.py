import os
import pyodbc
import pandas as pd
from datetime import datetime
import time
import dict_sql_query as sql
import mailer

import configparser
config = configparser.ConfigParser()
config.read('config.ini')

config_mailer = configparser.ConfigParser()
config_mailer.read('config_mailer.ini')

def adequacy_member_monthly_pull():
    # initialization
    path_export = config['PATH']['path_export']

    year_month = str(datetime.now().year) + str(datetime.now().month)
    path_export_provider = os.path.join(path_export, f'provider_{year_month}.xlsx')
    path_export_member = os.path.join(path_export, f'member_{year_month}.xlsx')

    recipient = config_mailer['RECIPIENT']['recipient']
    subject = config_mailer['MAILER']['subject']
    text = config_mailer['MAILER']['text']

    time0 = time.time()

    # establish SQL server connection
    conn = pyodbc.connect(
        r'Driver=ODBC Driver 17 for SQL Server;'
        r'SERVER=ihpas-ezcaprpt;'
        r'Trusted_Connection=yes;'
    )

    print('===== Adequacy Month Pull =====')

    # read data from SQL server
    df_prov = pd.read_sql(sql.qry_provider, conn)
    df_memb = pd.read_sql(sql.qry_member, conn)

    # export data
    df_prov.to_excel(path_export_provider, index=False, engine='xlsxwriter')
    df_memb.to_excel(path_export_member, index=False, engine='xlsxwriter')

    # send report notification
    mailer.send_report_notification(recipient, subject, text)

    time_lapse = round(time.time() - time0, 2)
    print(f'Process completed.   Time Lapsed: {time_lapse}')

if __name__ == '__main__':
    adequacy_member_monthly_pull()
    