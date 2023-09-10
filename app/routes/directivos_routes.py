from flask import Blueprint, jsonify
# agregar controlador y modelo

directivos_blueprint = Blueprint('directivos', __name__)

#Rutas
@directivos_blueprint.route('/directivos', methods=['GET'])
def obtenerDirectivos():
    #agregar logica para obtener lista de Directivo
    print('por aquí pasó')
    return jsonify(status=True, msg='Obtener Directivo')

@directivos_blueprint.route('/directivos', methods=['POST'])
def crearDirectivo():
    #agregar logica para creacion de Directivos
    pass