# app.py
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from bigcommerce_api import add_product_to_bigcommerce
from database import insert_product
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/agregar_producto', methods=['POST'])
def agregar_producto():
    try:
        product_name = request.form['productName']
        product_type = request.form['productType']
        product_price = float(request.form['productPrice'])
        product_weight = float(request.form['productWeight'])
        product_quantity = int(request.form['productQuantity'])

        product_data = {
            "name": product_name,
            "type": product_type,
            "price": product_price,
            "weight": product_weight,
            "quantity": product_quantity,
            "inventory_warning_level": 0
        }

        response = add_product_to_bigcommerce(product_data)

        if response.status_code == 201:
            if insert_product(product_data):
                return 'Producto agregado con éxito a BigCommerce y la base de datos'
            else:
                return 'Error al agregar el producto a la base de datos', 500
        else:
            return f'Error al agregar el producto a BigCommerce: {response.text}', 500

    except ValueError as ve:
        return f'Error en los datos del formulario: {ve}', 400
    except Exception as e:
        return f'Error inesperado al procesar la solicitud: {e}', 500

@app.route('/get_products', methods=['GET'])
def get_products():
    store_url = 'https://api.bigcommerce.com/stores/op9ph1xlis'
    api_path = '/v3/catalog/products'
    api_url = f'{store_url}{api_path}'
    api_token = 'q7bhsjn1imzrn45pciqtgri50z90ts'

    response = requests.get(api_url, headers={
        'Content-Type': 'application/json',
        'X-Auth-Token': api_token
    })

    if response.status_code == 200:
        products_data = response.json()['data']
        return jsonify(products_data)
    else:
        error_message = f"Error al obtener productos: {response.text}"
        print(error_message)
        return jsonify(error=error_message), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
