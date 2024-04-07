from flask import Flask
from flask_restx import Api

from modules.animation.animation_controller import api as animation

app = Flask(__name__)
api = Api(
  app,
  title='Animation',
  version='1.0',
  description='Animation API'
)

api.add_namespace(animation)

app.run(debug=True)