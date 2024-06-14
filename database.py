import mysql.connector

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost", user="root", password="", database="bigcommerce"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        return None

def insert_product(product_data):
    connection = connect_to_database()
    if connection:
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO products (name, type, price, weight, quantity, inventory_level, inventory_warning_level) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                values = (
                    product_data["name"],
                    product_data["type"],
                    product_data["price"],
                    product_data["weight"],
                    product_data["quantity"],
                    product_data["inventory_warning_level"],
                )
                cursor.execute(sql, values)
            connection.commit()
            return True
        except mysql.connector.IntegrityError as ie:
            print(f"Error de integridad al insertar producto: {ie}")
            return False
        except mysql.connector.Error as err:
            print(f"Error inesperado al insertar producto: {err}")
            return False
        finally:
            connection.close()
    else:
        return False
