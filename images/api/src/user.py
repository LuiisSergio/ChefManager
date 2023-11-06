from flask import jsonify
from src.database import dbQuery


def user(app, api_specs):

	@app.route('/')
	def home():
		dbQuery("INSERT INTO user_conf (name) VALUES (%s)", ("a",))
		return jsonify(message='Bem-vindo à API2!')

	@app.route('/usuarios', methods=['GET'])
	def get_usuarios():
		# Implementar lógica para retornar os usuários
		pass

	@app.route('/usuarios', methods=['POST'])
	def create_usuario():
		# Implementar lógica para criar um novo usuário
		pass

	@app.route('/produtos', methods=['GET'])
	def get_produtos():
		# Implementar lógica para retornar os produtos
		pass


	