from flask import Flask, request

app = Flask(__name__)

from products import products

@app.route('/ping', methods=['GET'])
def ping():
    return {"message": 'Pong!'}

@app.route('/products', methods=['GET'])
def getProducts():
    return {"products": products, "message": "Products List"}

@app.route('/products/<string:product_id>', methods=['GET'])
def getSingleProduct(product_id):
    productsFound = [product for product in products if product['id'] == int(product_id)]
    if len(productsFound) > 0:
        return {"product": productsFound}
    return {"error": "item not found"}, 404

@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "id": request.json['id'],
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return {"message": "Product Added Succesfully", "products": products}

@app.route('/products/<string:product_id>', methods=['PUT'])
def editProduct(product_id):
    productsFound = [product for product in products if product['id'] == int(product_id)]
    if len(productsFound) == 0:
        return {"Error": "Item not found"}, 404
    else:
        productsFound[0]['id'] = request.json['id']
        productsFound[0]['name'] = request.json['name']
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['quantity'] = request.json['quantity']
        return {'message': 'Product Succesfully Updated', 'Products': products}

@app.route('/products/<string:product_id>', methods=['DELETE'])
def deleteProduct(product_id):
    productsFound = [product for product in products if product['id'] == int(product_id)]
    if len(productsFound) == 0:
        return {"Error": "Item not found"}, 404
    else:
        products.remove(productsFound[0])
        return {'Message': 'Product Removed', 'Products': products}

if __name__ == '__main__':
    app.run(debug=True, port=3000)