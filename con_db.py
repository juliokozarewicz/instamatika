import mysql.connector
from config import db_conect, email_connect
from send_email import send_email
from time import sleep
from datetime import datetime


class Database_connect():
    """
    Class responsible for connecting to the database,
     performing queries and inserts.
    """

    def __init__(self):
        self.db_host = db_conect['db_host']
        self.db_database = db_conect['db_database']
        self.db_user = db_conect['db_user']
        self.db_password = db_conect['db_password']

    def db_commit(self, query):
        """
        Method that writes and updates the database.
        """

        try:

            conexao = mysql.connector.connect(

                host=self.db_host,
                database=self.db_database,
                user=self.db_user,
                password=self.db_password,

            )

            cursor = conexao.cursor()

            cursor.execute(query)

            conexao.commit()

            cursor.close()

            conexao.close()

        except Exception as error:

            error = error

            smtp_subject = "INSTAMATIK - Error Report"

            smtp_send_msg = (

                f"{datetime.now()} - "
                f"Database connection problems "
                f"(not inserting information)."

            )

            send_email(

                email_connect['smtp_email_login'],
                email_connect['smtp_pass'],
                email_connect['smtp_email_recipient'],
                smtp_subject,
                smtp_send_msg,
                email_connect['smtp_server'],
                email_connect['smtp_port']

            )

            sleep(150)

            return

        return

    def db_fetchall(self, query):
        """
        Method that queries the database.
        """

        try:

            conexao = mysql.connector.connect(

                host=self.db_host,
                database=self.db_database,
                user=self.db_user,
                password=self.db_password,

            )

            cursor = conexao.cursor()

            cursor.execute(query)

            rec_db = cursor.fetchall()

            cursor.close()

            conexao.close()

            return rec_db

        except Exception as error:

            error = error

            smtp_subject = "INSTAMATIK - Error Report"

            smtp_send_msg = (

                f"{datetime.now()} - "
                f"Database connection problems "
                "(not receiving information)."

            )

            send_email(

                email_connect['smtp_email_login'],
                email_connect['smtp_pass'],
                email_connect['smtp_email_recipient'],
                smtp_subject,
                smtp_send_msg,
                email_connect['smtp_server'],
                email_connect['smtp_port']

            )

            sleep(150)

            return

        return
