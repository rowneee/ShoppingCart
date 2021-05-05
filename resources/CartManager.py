from decimal import Decimal
from flask_restful import Resource
from flask import request
from services.CartService import *
import json

class CartManager(Resource):
    def get(self):
        return {
            'Cart Data': fetch_cart_payload()
        }

    def post(self):
        add_item(request.json['name'])
        return '200'

    def delete(self):
        remove_item(request.json['name'])
        return '200'







