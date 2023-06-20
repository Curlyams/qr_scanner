import pandas as pd
from credentials.credential import username, password, server, database
from sqlclass import SQLHandler
import scanclean

sql_handler = SQLHandler(server=server, database=database, username=username, password=password,)
sql_handler.connect()

raw_data_list = []

while True:
    data = input("Scan data (or type 'exit' to exit): ")
    if data.lower() == 'exit':
        break
    raw_data_list.append(data)
data_list = scanclean.clean_data(raw_data_list)


# Check if there are any scans to upload
if data_list:
    # Convert data_list to DataFrame
    df = pd.DataFrame(data_list, columns=['Clinic', 'Area', 'Member_ID', 'Date_Time_Of_Scan'])

    # Upload data to database
    # Upload DataFrame to the server
    table_name = 'Member_Scans'

    # Get the column names and types for table creation
    column_names = df.columns.tolist()
    column_types = ['VARCHAR(255)' for _ in range(len(column_names))]  # Change to appropriate types if needed

    # Ensure that the table exists in the database
    create_table_query = f"IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = '{table_name}') " \
                         f"CREATE TABLE {table_name} (ID INT IDENTITY(1,1), Member_Scan VARCHAR(255), " + \
                         ", ".join([f"{col} {col_type}" for col, col_type in zip(column_names, column_types)]) + ")"

    sql_handler.execute_query(create_table_query)

    insert_query = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES ({', '.join(['?' for _ in column_names])})"
    values = df.values.tolist()
    sql_handler.insert_data(insert_query, values)

sql_handler.close_connection()


