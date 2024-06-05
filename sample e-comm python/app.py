from flask import Flask, jsonify, request
import json

app = Flask(__name__)

def load_products_data():
    with open('products.json', 'r', encoding='utf-8') as file:
        return json.load(file)
    
def save_products_data(products):
    with open('products.json', 'w') as file:
        json.dump(products, file, indent=4)    

@app.route('/', methods=['GET'])
def hello():
    return "hello"

@app.route('/products', methods=['GET'])
def get_products():
    data = load_products_data()
    return jsonify(data)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_products_by_id(product_id):
    products = load_products_data()
    product = next((p for p in products if p['id'] == product_id), None)
    return jsonify(product) if product else ('Product not found', 404)

@app.route('/products', methods=['POST'])
def create_product():
    new_product = request.json
    products = load_products_data()
    products.append(new_product)
    save_products_data(products)
    return jsonify(new_product), 201

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    products = load_products_data()
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        update_data = request.json
        product.update(update_data)
        save_products_data(products)
        return jsonify(product)
    

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    products = load_products_data()
    
    updated_list = list(filter(lambda p: p["id"] != product_id ,products))
    save_products_data(updated_list)
    return 'Deleted successfully', 204
    

if __name__ == '__main__':
    app.run(debug=True)
