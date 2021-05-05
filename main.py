from flask import *
from flask_restful import Api
from resources.CheckoutManager import CheckoutManager
from resources.CartManager import CartManager
from resources.inventory import Inventory

app = Flask(__name__)
api = Api(app)

api.add_resource(Inventory, '/inventory')
api.add_resource(CartManager, '/cart')
api.add_resource(CheckoutManager, '/cart/checkout')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
