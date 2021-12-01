import os
import pyodbc
import pandas as pd
import configparser
from datetime import datetime
import time
import dict_sql_query as sql
from mailer import mailer


def adequacy_member_monthly_pull():
    # set directory to current file location
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # set up config file
    config = configparser.ConfigParser()
    config.read('config.ini')

    config_mailer = configparser.ConfigParser()
    config_mailer.read('./mailer/config_mailer.ini')

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
    print('\tloading data from SQL...')
    df_prov = pd.read_sql(sql.qry_provider, conn)
    df_memb = pd.read_sql(sql.qry_member, conn)

    # export data
    print('\twriting to Excel...')
    df_prov.to_excel(path_export_provider, index=False, engine='xlsxwriter')
    df_memb.to_excel(path_export_member, index=False, engine='xlsxwriter')

    # send report notification
    print('\tsending automated message...')
    mailer.send_report_notification(recipient, subject, text)

    time_lapse = round(time.time() - time0, 2)
    print(f'\nProcess completed.   Time Lapsed: {time_lapse}')

if __name__ == '__main__':
    adequacy_member_monthly_pull()
    