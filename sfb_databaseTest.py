"""Read write to Azure SQL database from pandas"""
import pyodbc
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# 1. Constants
AZUREUID = 'sfbdbadmin'                                    # Azure SQL database userid
AZUREPWD = 'DtJang2VdBkV9max'                                # Azure SQL database password
AZURESRV = 'sfb-sql.database.windows.net'   # Azure SQL database server name (fully qualified)
DATABASE = 'SfbEtlStagingDev'                                      # Azure SQL database name (if it does not exit, pandas will create it)
TABLE = '[etl].[MATCentral]'                                      # Azure SQL database table name
driver =  '{ODBC Driver 17 for SQL Server}'             # ODBC Driver

def main():
    """Main function"""

    # 2. Build a connectionstring
    connectionstring = pyodbc.connect('DRIVER='+driver+';SERVER='+AZURESRV+';DATABASE='+DATABASE+';UID='+AZUREUID+';PWD='+AZUREPWD)#mssql+pyodbc://{uid}:{password}@{server}:1433/{database}?driver={driver}'.format(
    #('DRIVER=driver;SERVER=AZURESRV;DATABASE=DATABASE;UID=AZUREUID;PWD=AZUREPWD')
       # uid=AZUREUID,
       # password=AZUREPWD,
       # server=AZURESRV,
       # database=DATABASE,
       # driver=DRIVER)#.replace(' ', '+'))

    # 3. Read dummydata into dataframe
    #df = pd.read_csv('./data/data.csv')
    cursor = connectionstring.cursor()
    query = "select * from [etl].[MATCentral];"  # .format(table=TABLE)
    query2 = "SELECT TOP(1000)[LAEstab] , [LA] , [Estab] , [URN] , [School Name] FROM[etl].[MATCentral]"

    cursor.execute(query2, connectionstring)
    engn = create_engine(connectionstring)











    #dfsql = pd.read_sql(query, connectionstring)

    # 4. Create SQL Alchemy engine and write data to SQL
    # engn = create_engine(connectionstring)
    #
    # #df.to_sql(TABLE, engn, if_exists='append')
    #
    # # 5. Read data from SQL into dataframe
    # query = 'SELECT * FROM {table}'.format(table=TABLE)
    # dfsql = pd.read_sql(query, engn)
    #
    # print(dfsql.head())


if __name__ == "__main__":

   main()