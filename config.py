import dotenv
from os import getenv


dotenv.load_dotenv(dotenv.find_dotenv())

# database
# ----------------------------------------------------------------------------
db_conect = {

    'db_host': getenv('db_host'),
    'db_user': getenv('db_user'),
    'db_password':  getenv('db_password'),
    'db_database': getenv('db_database')

}
# ----------------------------------------------------------------------------

# email report
# ----------------------------------------------------------------------------
email_connect = {

    'smtp_email_login': getenv('smtp_email_login'),
    'smtp_pass': getenv('smtp_pass'),
    'smtp_email_recipient': getenv('smtp_email_recipient'),
    'smtp_server': getenv('smtp_server'),
    'smtp_port': getenv('smtp_port')

}
# ----------------------------------------------------------------------------
