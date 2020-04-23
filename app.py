from flask import Flask, jsonify, request

from products import products

app = Flask(__name__)

#Get all the Products
@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({"produscts": products})

#Get a specific Product
@app.route('/products/<int:product_id>')
def getProduct(product_id):
    productsFound = [product for product in products if product['id'] == product_id]
    if (len(productsFound) > 0):
        return jsonify({'product': productsFound[0]})
    return jsonify({'message': 'Product Not found'})

# Create Product
@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        'id': request.json['id'],
        'name': request.json['name'],
        'price': request.json['price'],
        'quantity': 10
    }
    products.append(new_product)
    return jsonify({'products': products})

# Update Price and Quantity  Route
@app.route('/products/<int:product_id>', methods=['PUT'])
def editProduct(product_id):
    productsFound = [product for product in products if product['id'] == product_id]
    if (len(productsFound) > 0):
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            'message': 'Product Updated',
            'product': productsFound[0]
        })
    return jsonify({'message': 'Product Not found'})
    
# DELETE Data Route
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if len(productsFound) > 0:
        products.remove(productsFound[0])
        return jsonify({
            'message': 'Product Deleted',
            'products': products
        })

if __name__ == '__main__':
    app.run(debug=True, port=4000)