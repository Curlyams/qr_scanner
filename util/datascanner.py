import time
import pandas as pd
from credentials.credential import username, password, server, database
from util.sqlclass import SQLHandler
from util.datafunctions import *

class DataScanner:

    def __init__(self, server, database, username, password):
        self.sql_handler = SQLHandler(server=server, database=database, username=username, password=password)
        
    def scan_data(self,upload_time):
        while True:
            raw_data_list = []
            start_time = time.time()
            print(start_time)

            while time.time() - start_time < upload_time:
                data = input("Scan data (or type 'exit' to exit): ")
                if data.lower() == 'exit':
                    break
                raw_data_list.append(data)
            
            data_list = clean_data(raw_data_list)

            if data_list:
                self.save_to_db(data_list)

    def save_to_db(self, data_list):
        self.sql_handler.connect()
        df = pd.DataFrame(data_list, columns=['Clinic', 'Area', 'Member_ID', 'Date_Time_Of_Scan'])
        missing_columns = set(['Clinic', 'Area', 'Member_ID', 'Date_Time_Of_Scan']) - set(df.columns)
        for col in missing_columns:
            df[col] = 'error in cols'
        df['Date_Time_Of_Scan'] = int(time.time())
        table_name = 'Member_Scans'
        column_names = df.columns.tolist()
        column_types = ['VARCHAR(255)' for _ in range(len(column_names))]
        create_table_query = f"IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = '{table_name}') " \
                            f"CREATE TABLE {table_name} (ID INT IDENTITY(1,1), Member_Scan VARCHAR(255), " + \
                            ", ".join([f"{col} {col_type}" for col, col_type in zip(column_names, column_types)]) + ")"
        self.sql_handler.execute_query(create_table_query)
        insert_query = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES ({', '.join(['?' for _ in column_names])})"
        values = df.values.tolist()
        self.sql_handler.insert_data(insert_query, values)
        self.sql_handler.close_connection()


