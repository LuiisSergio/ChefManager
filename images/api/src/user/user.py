from flask import jsonify
from src.database.database import dbQuery


def user(app, api_specs):

	@app.route('/user/list', methods=['GET'])
	def get_usuarios():
		user_list = dbQuery("SELECT * FROM user_conf")
		return jsonify(user_list)
	

	