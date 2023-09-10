from app.modelo.directivos_modelo import Directivo as directivo_modelo
from app.modelo.usuarios_modelo import Usuario as usuario_modelo

from app.utils.db import db

from app import jsonify

def obtener_Directivos():
    try:
        lista_Directivos = [directivo.obtenerDatos for directivo in directivo_modelo.query.all()]
        return jsonify(status=True, msg=lista_Directivos)
    except Exception as e:
        return jsonify(status= False, msg=str(e))
    
def obtener_directivo_by_id(directivoID):
    try:
        # Traer el registro según el id dado
        directivo = directivo_modelo.query.filter_by(DirectivoID=directivoID).first()
        # si está vacio enviar mensaje
        if directivo is None:
            return jsonify(status=False, msg="No se encontraron directivos.")
        
        return jsonify(status=True, msg=directivo.obtenerDatos)
    except Exception as e:
        return jsonify(status=False, msg=str(e))

def obtener_directivo_by_usuarioID(userID):
    try:
        # Traer el registro según el id dado
        directivo = directivo_modelo.query.filter_by(UsuarioID=userID).first()
        # si está vacio enviar mensaje
        if directivo is None:
            return jsonify(status=False, msg="Ningun directivo encontrado.")
        
        return jsonify(status=True, msg=directivo.obtenerDatos)
    except Exception as e:
        return jsonify(status=False, msg=str(e))
    
def agregar_directivo(directivo):
    try:
        usuario = usuario_modelo.query.filter_by(Identificacion=directivo.usuario_identificacion).first()
        nuevo_directivo = directivo_modelo(directivo.departamento, directivo.horario_disponibilidad, directivo.estado, usuario)
        db.session.add(nuevo_directivo)
        db.session.commit()
        return jsonify(status=True, msg="registro de Directivo creado.")
    except Exception as e:
        return jsonify(status=False, msg=str(e))
    
def actualizar_directivo(directivo):
    try:
        old_directivo = directivo_modelo.query.filter_by(DirectivoID=directivo.directivoID).first()
        old_directivo.Departamento = directivo.Departamento
        old_directivo.HorarioDisponibilidad = directivo.HorarioDisponibilidad
        old_directivo.Estado = directivo.Estado
        db.session.commit()
        return jsonify(status=True, msg='Se ha actualizado el directivo.')
    except Exception as e:
        return jsonify(status=False, msg=str(e))
    
def eliminar_directivo(directivo):
    try:
        old_directivo = directivo_modelo.query.filter_by(DirectivoID=directivo.directivoID).first()
        old_directivo.Estado = 'desactivado'
        db.session.commit()
        return jsonify(status=True, msg='Se ha eliminado el directivo.')
    except Exception as e:
        return jsonify(status=False, msg=str(e))