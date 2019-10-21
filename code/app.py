from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identify

app = Flask(__name__)
app.secret_key = 'tony 111'
api = Api(app)

jwt = JWT(app, authenticate, identify)
items = []

class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(iter([ x for x in items if x['name'] == name]), None)
        return {'item': item }, 200 if item else 404

    def post(self, name):
        if next(iter([x for x in items if x['name'] == name]), None):
            return {'message': "An item with name '{}' already exists".format(name)}, 400

        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

class Items(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')

app.run(port=5000, debug=True)
