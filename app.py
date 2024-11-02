from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Contoh data produk batik dengan deskripsi
products = [
    {"id": 1, "name": "Batik Kawung", "price": 250000, "description": "Batik dengan motif kawung yang melambangkan kebijaksanaan dan kejujuran."},
    {"id": 2, "name": "Batik Parang", "price": 300000, "description": "Motif batik parang yang melambangkan kekuatan dan keberanian."},
    {"id": 3, "name": "Batik Mega Mendung", "price": 280000, "description": "Motif batik dari Cirebon yang menggambarkan awan mendung, simbol kesejukan."},
    {"id": 4, "name": "Batik Sekar Jagad", "price": 320000, "description": "Motif yang melambangkan keindahan dan keragaman budaya Indonesia."},
    {"id": 5, "name": "Batik Tulis Sidomukti", "price": 400000, "description": "Batik tulis khas Solo dengan motif yang sering digunakan pada acara pernikahan."},
    {"id": 6, "name": "Batik Truntum", "price": 350000, "description": "Batik tradisional yang melambangkan cinta yang tulus dan abadi."},
    {"id": 7, "name": "Batik Lasem", "price": 370000, "description": "Batik dengan pengaruh budaya Tionghoa, terkenal dengan warna merah cerah."},
    {"id": 8, "name": "Batik Priyangan", "price": 330000, "description": "Batik khas Priangan dengan motif yang terinspirasi oleh alam."},
    {"id": 9, "name": "Batik Bali", "price": 290000, "description": "Batik dari Bali dengan motif yang menggabungkan unsur budaya lokal."},
    {"id": 10, "name": "Batik Tambal", "price": 310000, "description": "Motif batik yang mencerminkan kehidupan yang dinamis dan keberagaman."},
    {"id": 11, "name": "Batik Lereng", "price": 260000, "description": "Batik dengan pola garis-garis diagonal yang melambangkan ketekunan."},
    {"id": 12, "name": "Batik Ceplok", "price": 275000, "description": "Motif geometris yang terinspirasi dari bentuk bunga dan alam."},
    {"id": 13, "name": "Batik Sogan", "price": 360000, "description": "Batik khas Solo dengan warna cokelat tua, cocok untuk acara formal."},
    {"id": 14, "name": "Batik Pisan Bali", "price": 340000, "description": "Motif batik dengan detail yang unik dan warna yang mencolok."},
    {"id": 15, "name": "Batik Tumpal", "price": 300000, "description": "Batik tradisional dengan pola segitiga yang melambangkan kesejahteraan."}
]

class ProductList(Resource):
    def get(self):
        return jsonify(products)

class ProductDetail(Resource):
    def get(self, product_id):
        product = next((p for p in products if p["id"] == product_id), None)
        if product:
            return jsonify(product)
        return {"message": "Product not found"}, 404

class AddProduct(Resource):
    def post(self):
        data = request.get_json()
        new_product = {
            "id": len(products) + 1,
            "name": data["name"],
            "price": data["price"],
            "description": data.get("description", "No description provided.")
        }
        products.append(new_product)
        return jsonify(new_product)

class UpdateProduct(Resource):
    def put(self, product_id):
        product = next((p for p in products if p["id"] == product_id), None)
        if not product:
            return {"message": "Product not found"}, 404
        data = request.get_json()
        product.update(data)
        return jsonify(product)

class DeleteProduct(Resource):
    def delete(self, product_id):
        global products
        products = [p for p in products if p["id"] != product_id]
        return {"message": "Product deleted successfully"}

# Menambahkan resource ke API
api.add_resource(ProductList, '/products')
api.add_resource(ProductDetail, '/products/<int:product_id>')
api.add_resource(AddProduct, '/products/add')
api.add_resource(UpdateProduct, '/products/update/<int:product_id>')
api.add_resource(DeleteProduct, '/products/delete/<int:product_id>')

if __name__ == '__main__':
    app.run(debug=True)
