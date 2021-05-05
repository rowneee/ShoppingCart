from decimal import Decimal
from flask_restful import Resource
from flask import request
from services.CartService import *

class CheckoutManager(Resource):
    def get(self):
        return {
            'Items in Cart': breakdown(),
            'Subtotal': round(get_total(),2),
            'Taxes': round((get_total() * 0.07),2),
            'Shipping': round((get_total() * 0.09),2),
            'Total': round(get_total() + (get_total() * 0.06),2)
        }