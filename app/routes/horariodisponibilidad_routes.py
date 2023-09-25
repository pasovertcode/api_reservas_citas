from flask import Blueprint, jsonify, request
from app.controlador import horariodisponibilidad_controlador
from app.modelo.horariodisponibilidad_modelo import HorarioDisponibilidad as horariodisponibilidad_modelo

horariodisponibilidad_blueprint = Blueprint('horario_disponibilidad', __name__)

@horariodisponibilidad_blueprint.route('/horario/buscar/<identificacion>', methods=["GET"])
def buscardisponibilidadDirectivo(identificacion):
    try:
        if request.method == 'GET':
            return horariodisponibilidad_controlador.obtener_horariosdisponibilidad_by_ID(identificacion)
    except Exception as e:
        return jsonify(status=False, msg=str(e))