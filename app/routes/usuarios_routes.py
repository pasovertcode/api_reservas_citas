from flask import Blueprint, jsonify, request
from app.controlador import usuarios_controlador


usuarios_blueprint = Blueprint('usuarios', __name__)

#Rutas
@usuarios_blueprint.route('/usuarios', methods=['GET'])
def obtenerUsuarios():

    try:
        if request.method == 'GET':
            return usuarios_controlador.obtener_Usuarios()
    except Exception as e:
        return jsonify(status=False, msg=str(e))

@usuarios_blueprint.route('/usuarios', methods=['POST'])
def CrearUsuario():
    #agregar logica para creacion de usuarios
    pass