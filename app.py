from flask import Flask
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Resource, Api

from api.utils import population, male_population, female_population

app = Flask(__name__)
api = Api(app)


class World(Resource):
    def get(self):
        return population().to_json()

api.add_resource(World, '/')

if __name__ == '__main__':
    app.run(debug=True)