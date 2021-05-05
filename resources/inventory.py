from flask import Flask, jsonify
from flask_restful import Resource
from services import InventoryService


class Inventory(Resource):

    def get(self):
        result = list(map(lambda x: x.json(), InventoryService.fetch_inventory()))
        return {'inventory': result}







