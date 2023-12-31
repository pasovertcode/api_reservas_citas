from app.utils.db import db
from . import directivohorario_modelo

class HorarioDisponibilidad(db.Model):
    __tablename__ = "Horario_Disponibilidad"
    HorarioID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    HorarioNombre = db.Column(db.String(255), nullable=False)
    Fecha = db.Column(db.Date, nullable=False)
    HoraInicio = db.Column(db.Time, nullable=False)
    HoraFin = db.Column(db.Time, nullable=False)
    """ 
    # Agregar la relación de muchos a muchos a través de DirectivosHorarios
    directivo = db.relationship('Directivo', secondary=directivohorario_modelo.DirectivoHorario, back_populates='HorarioDisponibilidad')
    """
    def __init__(self, horario_nombre, fecha, hora_inicio, hora_fin):
        self.HorarioNombre = horario_nombre
        self.Fecha = fecha
        self.HoraInicio = hora_inicio
        self.HoraFin = hora_fin

    @property
    def obtenerDatos(self):
        return {
            'HorarioID': self.HorarioID,
            'HorarioNombre': self.HorarioNombre,
            'Dia': self.Fecha.day,
            'Mes': self.Fecha.month,
            'Año': self.Fecha.year,
            'HoraInicio': self.HoraInicio.strftime('%H:%M:%S'),
            'HoraFin': self.HoraFin.strftime('%H:%M:%S')
        }
    
