from flask import Blueprint, jsonify, request
from app.controlador import citas_controlador


citas_blueprint = Blueprint('citas', __name__)

#Rutas
@citas_blueprint.route('/citas', methods=['GET'])
def obtenerCitas():
     try:
        if request.method == 'GET':
            return citas_controlador.obtener_Citas()
     except Exception as e:
        return jsonify(status=False, msg=str(e))

@citas_blueprint.route('/citas', methods=['POST'])
def crearCita():
    #agregar lógica para creación de citas
    pass