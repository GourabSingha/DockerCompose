from flask import Flask
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)
class Product(Resource):
    def get(self):
        return {
            'products': ['Ice cream', 'Chocolate', 'Fruit', 'Eggs']
        }
api.add_resource(Product, '/')
if __name__ == '__main__':
    app.run(host='192.168.99.100', port=80, debug=True)
