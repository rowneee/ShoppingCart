from flask import Flask, jsonify
from flask_restful import Resource, Api
from db import *

class Cart:
    def __init__(self):
        self.items = []

