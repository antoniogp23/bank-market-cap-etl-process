# Code for ETL operations on Country-GDP data
# Importing the required libraries

from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime

def log_progress(message):
    """Logs the progress of the process to a log file."""
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format)
    with open("./etl_project_log.txt","a") as f:
        f.write(timestamp + ',' + message + '\n') 


def extract(url, table_attribs):
    """Extracts data from the Wikipedia table and stores it in a DataFrame."""
    page = requests.get(url).text
    data = BeautifulSoup(page,'html.parser')
    df = pd.DataFrame(columns=table_attribs)

    #Find tables on the page and select where By Market capitalizacion is located
    tables = data.find_all('tbody')
    rows = tables[0].find_all('tr')

    for row in rows:
        col = row.find_all('td')
        if len(col)!=0:
            data_dict = {"Name" : col[1].text.strip(),
                         "MC_USD_Billion": float(col[2].text.strip().replace('\n','').replace(',',''))}
            df1 = pd.DataFrame([data_dict])
            df = pd.concat([df,df1],ignore_index = True)
    #print(df)
    return df


def transform(df, csv_path):
    """Transforms the Market Cap column into other currencies using exchange rates from a CSV file."""
    #CSV File
    exchange_rate = pd.read_csv(csv_path).set_index('Currency').to_dict()['Rate']
    #Conversions
    df['MC_GBP_Billion'] =  [np.round(x * exchange_rate['GBP'],2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion '] = [np.round(x * exchange_rate['EUR'],2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] =  [np.round(x * exchange_rate['INR'],2) for x in df['MC_USD_Billion']]
    
    return df

def load_to_csv(df, output_path):
    """Saves the DataFrame to a CSV file."""
    df.to_csv(output_path)

def load_to_db(df, sql_connection, table_name):
    """Saves the DataFrame to an SQLite database table."""
    df.to_sql(table_name,sql_connection, if_exists='replace',index=False)
    
def run_query(query_statement, sql_connection):
    """Executes an SQL query on the database and displays the results."""
    print(query_statement)
    query_output = pd.read_sql(query_statement,sql_connection)
    print(query_output)

#Declaring known values
url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs = ['Name','MC_USD_Billion']
db_name = 'Banks.db'
table_name = 'Largest_banks'
csv_path = './exchange_rate.csv'
log_file = 'code_log.txt'
csv_final = 'new_exchange_rate.csv'

log_progress("Preliminaries complete. Initiating ETL process.")

df = extract(url,table_attribs)

log_progress("Data extraction complete. Initiating Transformation process.")

df = transform(df,csv_path)

#print(df)


log_progress("Data transformation complete. Initiating loading process.")

load_to_csv(df, csv_final)

log_progress("Data saved to CSV file.")


sql_connection = sqlite3.connect(db_name)

log_progress("SQL Connection initiated.")

load_to_db(df,sql_connection,table_name)

log_progress('Data loaded to Database as table. Running the query')

#query_statement = f"SELECT * FROM Largest_banks"
#query_statement = f"SELECT AVG(MC_GBP_Billion) FROM Largest_banks"
query_statement = f"SELECT Name from Largest_banks LIMIT 5"
run_query(query_statement, sql_connection)

log_progress('Process Complete.')

sql_connection.close()
