from flask import Blueprint, jsonify, request, make_response
from app.controlador import usuarios_controlador
from app.modelo.usuarios_modelo import Usuario as usuario_modelo
from flask_cors import cross_origin

usuarios_blueprint = Blueprint('usuarios', __name__)

#Rutas
@usuarios_blueprint.route('/usuarios', methods=["GET"])
@usuarios_blueprint.route('/usuarios/buscar/<id_usuario>', methods=["GET"])
@usuarios_blueprint.route('/usuarios/actualizar', methods=["PUT"])
@usuarios_blueprint.route('/usuarios/agregar', methods=["POST"])
@usuarios_blueprint.route('/usuarios/eliminar', methods=["DELETE"])
@cross_origin()
def managerUsuario(id_usuario = None):
    try:
        if id_usuario == None:
            if request.method == 'GET':
                return usuarios_controlador.obtener_Usuarios()
            if request.method == 'DELETE':
                identificacion = request.json['identificacion']
                return usuarios_controlador.eliminar_usuario(identificacion)

            usuario = usuario_modelo(
                request.json['NombreCompleto'], 
                request.json['CorreoElectronico'], 
                request.json['Identificacion'], 
                request.json['Contraseña'], 
                request.json['Rol'],
                request.json['Estado']
            )

            if request.method == 'POST':
                return usuarios_controlador.agregar_usuario(usuario)

            if request.method == 'PUT':
                print(usuario.obtenerDatos)
                return usuarios_controlador.actualizar_usuario(usuario)

        if id_usuario is not None:
            return usuarios_controlador.obtener_usuario_by_identificacion(id_usuario)
        
    except Exception as e:
        return jsonify(status=False, msg=str(e))

@usuarios_blueprint.route('/usuarios/login', methods=["POST"])
@cross_origin()
def loginUsuario():
    try:
        if request.method == 'POST':
            usuarioID = request.json['usuario']
            password = request.json['password']
            return usuarios_controlador.login_usuario(usuarioID, password)

    except Exception as e:
        return jsonify(status=False, msg=str(e))

""" @usuarios_blueprint.route('/usuarios/login', methods=['OPTIONS'])
def handle_options():
    response = make_response()
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:4200')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    return response """