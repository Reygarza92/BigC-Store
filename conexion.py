import mysql.connector

db_host = "localhost"
db_user = "root"
db_password = ""
db_name = "bigcommerce"

try:
    connection = mysql.connector.connect(
        host=db_host, user=db_user, password=db_password, database=db_name
    )
    print("Conexión exitosa a la base de datos")
except mysql.connector.Error as err:
    print(f"Error de conexión a la base de datos: {err}")
finally:
    if connection:
        connection.close()
 