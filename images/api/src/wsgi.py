from flask import Flask, jsonify
from flask_pydantic_spec import FlaskPydanticSpec
from src.user.user import user

def create_app():
	app = Flask(__name__)
	api_specs = FlaskPydanticSpec('flask', title = 'ChefManager')
	api_specs.register(app)

	user(app, api_specs)

	return app