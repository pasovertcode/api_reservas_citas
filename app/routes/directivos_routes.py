from flask import Blueprint, jsonify, request
from app.controlador import directivos_controlador
from app.modelo.directivos_modelo import Directivo as directivo_modelo

directivos_blueprint = Blueprint('directivos', __name__)

#Rutas
@directivos_blueprint.route('/directivos', methods=["GET"])
@directivos_blueprint.route('/directivos/buscar/<id_directivo>', methods=["GET"])
@directivos_blueprint.route('/directivos/actualizar', methods=["PUT"])
@directivos_blueprint.route('/directivos/agregar', methods=["POST"])
@directivos_blueprint.route('/directivos/eliminar', methods=["DELETE"])
def managerDirectivo(id_directivo = None):
    try:
        if id_directivo == None:
            if request.method == 'GET':
                return directivos_controlador.obtener_Directivos()
            if request.method == 'DELETE':
                identificacion = request.json['identificacion']
                return directivos_controlador.eliminar_directivo(identificacion)

            directivo = directivo_modelo(
                request.json['horario_nombre'], 
                request.json['fecha'], 
                request.json['Identificacion'], 
                request.json['hora_inicio'], 
                request.json['hora_fin']
            )

            if request.method == 'POST':
                return directivos_controlador.agregar_directivo(directivo)

            if request.method == 'PUT':
                print(directivo.obtenerDatos)
                return directivos_controlador.actualizar_directivo(directivo)

        if id_directivo is not None:
            return directivos_controlador.obtener_directivo_by_identificacion(id_directivo)
        
    except Exception as e:
        return jsonify(status=False, msg=str(e))

