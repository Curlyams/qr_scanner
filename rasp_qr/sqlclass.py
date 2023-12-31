import pypyodbc as odbc
import json

class SQLHandler:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connection = None
        self.cursor = None
        self.dsn = 'AzureDB'
    def connect(self):
        try:
            connection_string = 'DSN={0};UID={1};PWD={2};DATABASE={3};'.format(self.dsn, self.username,self.password,self.database)
            self.connection = odbc.connect(connection_string)
            self.cursor = self.connection.cursor()
            print("Connection established successfully")
        except Exception as e:
            print(e)

    def execute_query(self, query, params=None):
        try:
            if params is not None:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Exception as e:
            print(e)

    def insert_data(self, query, values):
        try:
            for value in values:
                self.cursor.execute(query, tuple(value))
            self.connection.commit()
            print("Data inserted successfully")
        except Exception as e:
            print("Error occurred while inserting data:", str(e))




    def fetch_data(self, query):
        try:
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            print(e)
    def delete_data(self,table_name):
        self.execute_query(f"DELETE FROM {table_name}")


    def close_connection(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
            print("Connection closed successfully")
        except Exception as e:
            print(e)

