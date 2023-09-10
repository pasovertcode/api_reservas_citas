from flask import Blueprint, jsonify, request
from app.controlador import directivos_controlador

directivos_blueprint = Blueprint('directivos', __name__)

#Rutas
@directivos_blueprint.route('/directivos', methods=['GET'])
def obtenerDirectivos():
     try:
        if request.method == 'GET':
            return directivos_controlador.obtener_Directivos()
     except Exception as e:
        return jsonify(status=False, msg=str(e))

@directivos_blueprint.route('/directivos', methods=['POST'])
def crearDirectivo():
    #agregar logica para creacion de Directivos
    pass