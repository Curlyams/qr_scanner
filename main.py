from util.datafunctions import *
from util.datascanner import *
from util.sqlclass import *
from credentials.credential import server, database, username, password, connection_string_windows

connection_string = connection_string_windows
scanner = DataScanner(server, database, username, password, connection_string ,dsn=None)
scanner.scan_data(upload_time=10)

