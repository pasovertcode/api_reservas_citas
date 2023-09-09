from flask import Blueprint, jsonify
# agregar controlador y modelo

usuarios_blueprint = Blueprint('usuarios', __name__)

#Rutas
@usuarios_blueprint.route('/usuarios', methods=['GET'])
def obtenerUsuarios():
    #agregar logica para obtener lista de usuarios
    print('por aquí pasó')
    return jsonify(status=True, msg='Obtener Usuarios')

@usuarios_blueprint.route('/usuarios', methods=['POST'])
def CrearUsuario():
    #agregar logica para creacion de usuarios
    pass