from app.modelo.usuarios_modelo import Usuario as usuario_modelo
from app import jsonify

def obtener_Usuarios():
    try:
        lista_Usuarios = [usuario.obtenerDatos for usuario in usuario_modelo.query.all()]
        return jsonify(status=True, msg=lista_Usuarios)
    except Exception as e:
        return jsonify(status= False, msg=str(e))
    
    