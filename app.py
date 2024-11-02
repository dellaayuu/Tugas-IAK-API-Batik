from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Contoh data produk batik dengan deskripsi dan alamat
batik_products = [
    {"id": 1, "name": "Batik Mega Mendung", "price": 500000, "description": "Motif batik klasik dengan pola awan yang elegan, asal Cirebon.", "address": "Jalan Batik Mega No. 10, Cirebon"},
    {"id": 2, "name": "Batik Parang", "price": 450000, "description": "Motif batik tradisional dari Yogyakarta dengan pola parang yang melambangkan kekuatan.", "address": "Jalan Malioboro No. 20, Yogyakarta"},
    {"id": 3, "name": "Batik Kawung", "price": 400000, "description": "Batik dengan motif kawung berbentuk lingkaran yang melambangkan kemurnian, asal Solo.", "address": "Jalan Slamet Riyadi No. 15, Solo"},
    {"id": 4, "name": "Batik Sekar Jagad", "price": 550000, "description": "Motif yang melambangkan keindahan dan keragaman dunia, populer di Jawa Tengah.", "address": "Jalan Diponegoro No. 30, Semarang"},
    {"id": 5, "name": "Batik Lasem", "price": 600000, "description": "Batik dengan perpaduan warna merah khas dan motif dari Lasem, Jawa Tengah.", "address": "Jalan Merah Lasem No. 25, Lasem"}
]

class ProductList(Resource):
    def get(self):
        return jsonify(batik_products)

class ProductDetail(Resource):
    def get(self, product_id):
        product = next((p for p in batik_products if p["id"] == product_id), None)
        if product:
            return jsonify(product)
        return {"message": "Product not found"}, 404

class AddProduct(Resource):
    def post(self):
        data = request.get_json()
        new_product = {
            "id": len(batik_products) + 1,
            "name": data["name"],
            "price": data["price"],
            "description": data.get("description", "No description provided."),
            "address": data.get("address", "No address provided.")
        }
        batik_products.append(new_product)
        return jsonify(new_product)

class UpdateProduct(Resource):
    def put(self, product_id):
        product = next((p for p in batik_products if p["id"] == product_id), None)
        if not product:
            return {"message": "Product not found"}, 404
        data = request.get_json()
        product.update(data)
        return jsonify(product)

class DeleteProduct(Resource):
    def delete(self, product_id):
        global batik_products
        batik_products = [p for p in batik_products if p["id"] != product_id]
        return {"message": "Product deleted successfully"}

# Menambahkan resource ke API
api.add_resource(ProductList, '/products')
api.add_resource(ProductDetail, '/products/<int:product_id>')
api.add_resource(AddProduct, '/products/add')
api.add_resource(UpdateProduct, '/products/update/<int:product_id>')
api.add_resource(DeleteProduct, '/products/delete/<int:product_id>')

if __name__ == '__main__':
    app.run(debug=True)
