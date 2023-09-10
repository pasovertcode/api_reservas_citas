from flask import Blueprint, jsonify
# agregar controlador y modelo

citas_blueprint = Blueprint('citas', __name__)

#Rutas
@citas_blueprint.route('/citas', methods=['GET'])
def obtenerCitas():
    #agregar logica para obtener lista de citas
    print('por aquí pasó')
    return jsonify(status=True, msg='Obtener citas')

@citas_blueprint.route('/citas', methods=['POST'])
def crearCita():
    #agregar logica para creacion de citas
    pass