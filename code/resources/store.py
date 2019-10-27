import sqlite3
from flask_restful import Resource
from flask_jwt import jwt_required
from models.store import StoreModel


class Store(Resource):
    @jwt_required()
    def get(self, name):
        item = StoreModel.find_by_name(name)

        if item:
            return item.json(), 200
        else:
            return {'message': "Store not found"}, 404

    @jwt_required()
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "An store with name '{}' already exists".format(name)}, 400

        item = StoreModel(name)

        try:
            item.save_to_db()
        except:
            return {'message': "Ann error occurred inserting the item"}, 500

        return item.json(), 201

    @jwt_required()
    def delete(self, name):
        store = StoreModel.find_by_name(name)

        if store:
            store.delete_from_db()

        return {'message': 'Store deleted'}


class Stores(Resource):
    @jwt_required()
    def get(self):
        return {'stores': [x.json() for x in StoreModel.query.all()]}
