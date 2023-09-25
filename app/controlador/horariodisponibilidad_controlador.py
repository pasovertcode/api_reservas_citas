from app.modelo.horariodisponibilidad_modelo import HorarioDisponibilidad as horariodisponibilidad_modelo
from app.modelo.directivohorario_modelo import DirectivoHorario as directivohorario_modelo
from app.modelo.usuarios_modelo import Usuario as usuario_modelo
from app.modelo.directivos_modelo import Directivo as directivo_modelo

from app.utils.db import db

from app import jsonify

def obtener_horariosDisponibilidad():
    try:
        listaHorariosDisponibilidad = [horariodisponibilidad.obtenerDatos  for horariodisponibilidad in horariodisponibilidad_modelo.query.all()]
        return jsonify(status=True, msg=listaHorariosDisponibilidad)
    except Exception as e:
        return jsonify(status= False, msg=str(e))
    
def obtener_horariosdisponibilidad_by_ID(identificacion):
    try:
        horariosDisponiblidad = [directivodisponibilidad.obtenerDatos for directivodisponibilidad in horariodisponibilidad_modelo.query\
            .join(directivohorario_modelo, directivohorario_modelo.HorarioID == horariodisponibilidad_modelo.HorarioID)\
            .filter(usuario_modelo.Identificacion == identificacion)\
            .filter(directivo_modelo.DirectivoID == directivohorario_modelo.DirectivoID)\
            .filter(usuario_modelo.UserID == directivo_modelo.UsuarioID)\
            .all()]
        
        return jsonify(status=True, msg=horariosDisponiblidad)
    except Exception as e:
        return jsonify(status=True, msg=str(e))

def crear_horarioDisponibilidad(directivo):
    pass

def actualizar_horarioDisponibilidad(directivo):
    pass

def eliminar_horarioDisponibilidad(horarioDisponibilidad):
    pass