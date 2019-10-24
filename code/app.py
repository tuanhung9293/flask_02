from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identify
from resources.user import UserRegister
from resources.item import Item, Items

app = Flask(__name__)
app.secret_key = 'tony 111'
api = Api(app)

jwt = JWT(app, authenticate, identify)
items = []


api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
