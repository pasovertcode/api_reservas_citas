from app.modelo.citas_modelo import Cita as cita_modelo
from app.modelo.directivos_modelo import Directivo as directivo_modelo
from app.modelo.usuarios_modelo import Usuario as usuario_modelo

from app.utils.db import db

from app import jsonify

def obtener_Citas():
    try:
        lista_Citas = [cita.obtenerDatos for cita in cita_modelo.query.all()]
        return jsonify(status=True, msg=lista_Citas)
    except Exception as e:
        return jsonify(status= False, msg=str(e))

def obtener_cita_by_id(id_cita):
    try:
        # Traer el registro según el id dado
        cita = cita_modelo.query.filter_by(CitaID=id_cita).first()
        # si está vacio enviar mensaje
        if cita is None:
            return jsonify(status=False, msg="Ninguna cita encontrada")
        
        return jsonify(status=True, msg=cita.obtenerDatos)
    except Exception as e:
        return jsonify(status=False, msg=str(e))
    
def obtener_cita_by_usuarioID(userID):
    try:
        # Traer el registro según el id dado
        cita = cita_modelo.query.filter_by(UsuarioID=userID).first()
        # si está vacio enviar mensaje
        if cita is None:
            return jsonify(status=False, msg="Ninguna cita encontrada")
        
        return jsonify(status=True, msg=cita.obtenerDatos)
    except Exception as e:
        return jsonify(status=False, msg=str(e))
    
def obtener_cita_by_directivo(directivo):
    try:
        # Traer el registro según el id dado
        cita = cita_modelo.query.filter_by(DirectivoID=directivo.DirectivoID).first()
        # si está vacio enviar mensaje
        if cita is None:
            return jsonify(status=False, msg="Ninguna cita encontrada")
        
        return jsonify(status=True, msg=cita.obtenerDatos)
    except Exception as e:
        return jsonify(status=False, msg=str(e))
    
def agregar_cita(cita):
    try:
        usuario = usuario_modelo.query.filter_by(Identificacion=cita.Identificacion).first()
        
        usuario_directivo = usuario_modelo.query.filter_by(Identificacion=cita.identificacion_directivo).first()
        directivo = directivo_modelo.query.filter_by(UsuarioID=usuario_directivo.UserID).first()
        nueva_cita = cita_modelo(cita.fecha_hora, cita.estado, cita.notas, usuario, directivo)
        db.session.add(nueva_cita)
        db.session.commit()
        return jsonify(status=True, msg="Cita creada correctamente.")
    except Exception as e:
        return jsonify(status=False, msg=str(e))
    
def actualizar_cita(cita):
    try:
        old_cita = cita_modelo.query.filter_by(CitaID=cita.CitaID).first()
        old_cita.FechaHoraCita = cita.FechaHoraCita
        old_cita.EstadoCita = cita.EstadoCita
        old_cita.Notas = cita.Notas
        db.session.commit()
        return jsonify(status=True, msg='Se ha actualizado la cita.')
    except Exception as e:
        return jsonify(status=False, msg=str(e))
    
def eliminar_cita(cita):
    try:
        old_cita = cita_modelo.query.filter_by(CitaID=cita.CitaID).first()
        old_cita.EstadoCita = 'desactivado'
        db.session.commit()
        return jsonify(status=True, msg='Se ha eliminado la cita.')
    except Exception as e:
        return jsonify(status=False, msg=str(e))