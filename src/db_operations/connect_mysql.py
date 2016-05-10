import mysql.connector
from mysql.connector import errors

def db_connect():
    """
    Mysql connector def
    :return:
    """
    host= "localhost"
    port =3306
    username= "root"
    password=''
    db = "plan4cloud"
    try:
        connection = mysql.connector.connect(host=host,
                                             username = username,
                                             password = password,
                                             db =db

                                            )
        if connection.is_connected():
            print "connection success"
    except errors as err:
        print err

    finally:
        connection.close()




if __name__ =="__main__" :
    db_connect()

