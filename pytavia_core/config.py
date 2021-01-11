import os
import sys
# import copy
# import logging
import json
import pytavia_logger

sys.path.append("pytavia_core"    )
sys.path.append("pytavia_modules" )
sys.path.append("pytavia_settings")
sys.path.append("pytavia_stdlib"  )
sys.path.append("pytavia_storage" )

# from pytavia_stdlib import idgen

G_FLASK_SECRET=b'_5#y2L"F4Q8z\n\xec]/'

# This is the home path for the home of this project
G_HOME_PATH=os.getcwd()

# This is where all the cookies are stored
G_SESSION_STORAGE           = G_HOME_PATH + "/settings/storage"
G_STATIC_URL_PATH           = G_HOME_PATH + "/static"
G_STATIC_URL_PATH           = "/static"
G_UPLOAD_PATH               = G_HOME_PATH + G_STATIC_URL_PATH + "/upload"
G_UPLOAD_URL_PATH           = G_STATIC_URL_PATH + "/upload"
G_STATIC_STARTUP_PATH       = G_HOME_PATH + "/pytavia_startup"

# read the config file and pass the values in
app_config_handle           = open(G_STATIC_STARTUP_PATH + "/app-running.conf" , "r")
config_json_str             = app_config_handle.read()
config_json                 = json.loads( config_json_str )

# the pytavia logger that can be used througout the app
plogger = pytavia_logger.pytavia_logger({
    "file"     : "app.log",
    "print_to" : "STDOUT"
})

plogger.print_out("---------------------------------------")
plogger.print_out("PYTAVIA - CONFIG MODULE")
plogger.print_out( config_json_str )
plogger.print_out("---------------------------------------")

# CORE DATABASES DO NOT MODIFY

pytavia_dispatchDB  = "pytavia_dispatchDB"
pytavia_dispatch    = "mongodb://127.0.0.1:27017/" + pytavia_dispatchDB

###################### USER DATABASES BELOW HERE (MODIFYABLE) 


mainDB                      = config_json["mainDB"]
mongo_main_db_report_string = config_json["mongo_main_db_report_string"]

# This is where we have all the databases we want to connect to
G_DATABASE_CONNECT  = [
    {"dbname" : pytavia_dispatchDB , "dbstring" : pytavia_dispatch },

    # USER DATABASES MODIFY BELOW
    {"dbname" : mainDB , "dbstring" : mongo_main_db_report_string  },
]

G_RANDOM_START = config_json["G_RANDOM_START"]
G_RANDOM_END   = config_json["G_RANDOM_END"]

# these are just default status codes and descriptions
G_STATUS = {
    "SUCCESS"               : {
        "CODE"              : "0000",
        "DESC"              : "Operation Successful."
    },
    "UNEXPECTED_ERROR"      : {
        "CODE"              : "9999",
        "DESC"              : "Unexpected error occured."
    },
    # DATABASE RELATED STATUS CODES
    "RECORD_NOT_FOUND"      : {
        "CODE"              : "0101",
        "DESC"              : "Record does not exist."
    },
    "FK_EXISTS"             : {
        "CODE"              : "0102",
        "DESC"              : "Record is already referenced."
    },
    "NO_FK_EXISTS"          : {
        "CODE"              : "0103",
        "DESC"              : "Record is not referenced."
    },
    "NOT_UNIQUE"          : {
        "CODE"              : "0104",
        "DESC"              : "Record is not unique"
    },
    # PAYLOAD RELATED STATUS CODES
    "FIELD_REQUIRED"        : {
        "CODE"              : "0201",
        "DESC"              : "Field is required."
    },
    "NOT_NUMBER"            : {
        "CODE"              : "0202",
        "DESC"              : "Field should be a number."
    },
    "NOT_GREATER_THAN"      : {
        "CODE"              : "0203",
        "DESC"              : "The number should be greater than the correct value"
    },
    "NOT_LESS_THAN"         : {
        "CODE"              : "0204",
        "DESC"              : "The number should be less than the correct value"
    },
}

# used by utils.py - _get_current_timestamp - used to convert to readable timestamp
G_STR_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"             