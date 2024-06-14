# bigcommerce_api.py
import requests

def add_product_to_bigcommerce(product_data):
    response = requests.post(
        'https://api.bigcommerce.com/stores/op9ph1xlis/v3/catalog/products',
        headers={
            'Content-Type': 'application/json',
            'X-Auth-Token': 'q7bhsjn1imzrn45pciqtgri50z90ts'
        },
        json=product_data
    )

    return response
