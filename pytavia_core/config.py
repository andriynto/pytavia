import os

G_FLASK_SECRET = b'_5#y2L"F4Q8z\n\xec]/'

# This is the
G_HOME_PATH = os.getcwd()
# home path for the home of this project

# This is where all the cookies are stored
G_SESSION_STORAGE = G_HOME_PATH + "/settings/storage"
G_STATIC_URL_PATH = "/static"

MGDBString = "mongodb://127.0.0.1:27017/"  # Local/DEV/UAT

# Database
mainDB = "aladin-v2-db"

mainDB_string = MGDBString + mainDB


# This is where we have all the databases we want to connect to
G_DATABASE_CONNECT = [
    {"dbname": mainDB, "dbstring": mainDB_string}
]

G_RECORD_ADD_MODIFIED_TIMESTAMP = True
G_RECORD_ADD_ARCHIVED_TIMESTAMP = True