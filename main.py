from util.datafunctions import *
from util.datascanner import *
from util.sqlclass import *
from credentials.credential import server, database, username, password

connection_string = f"Driver={{ODBC Driver 18 for SQL Server}};Server=tcp:{server},1433;Database={database};Uid={username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
scanner = DataScanner(server, database, username, password, connection_string,dsn =None)
scanner.scan_data(upload_time=10)

