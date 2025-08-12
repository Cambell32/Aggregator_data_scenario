import mysql.connector
from mysql.connector import Error 
#local installation Maria DB via a local XAMPP installation 
 
#try:
    # Establish connection
def dbconnect():
        connectdb = mysql.connector.connect(
        host='127.0.0.1',        # or '127.0.0.1'
        port=3306,               # custom MariaDB port (default is usually 3306)
        user='root',             # default XAMPP user
        password='',     # set your MySQL password
        database='aggre_db',      # your database name
        allow_local_infile = True 
    )
        return connectdb


       # if connection.is_connected():
        #        print("✅ Connected to MariaDB database!")

                # Example query
         #       cursor = connection.cursor()
          #      cursor.execute("SHOW TABLES;")
           #     for table in cursor.fetchall():
            #        print(table)

       # except Error as e:
        #    print(f"❌ Error while connecting: {e}")

         #finally:
          #  if 'connection' in locals() and connection.is_connected():
           #     cursor.close()
            #    connection.close()
             #   print("🔌 Connection closed.")