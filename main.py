from util.datafunctions import *
from util.datascanner import *
from util.sqlclass import *
from credentials.credential import server, database, username, password


scanner = DataScanner(server, database, username, password)
scanner.scan_data(upload_time=10)

