from app.utils.db import db

class Cita(db.Model):
    CitaID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    FechaHoraCita = db.Column(db.DateTime, nullable=False)
    EstadoCita = db.Column(db.String(50), nullable=False)
    Notas = db.Column(db.Text)

    # Relación con la tabla de Usuarios (muchos a uno)
    UsuarioID = db.Column(db.Integer, db.ForeignKey('usuario.UserID'), nullable=False)
    usuario = db.relationship('Usuario', back_populates='citas')

    # Relación con la tabla de Directivos (muchos a uno)
    DirectivoID = db.Column(db.Integer, db.ForeignKey('directivo.DirectivoID'), nullable=False)
    directivo = db.relationship('Directivo', back_populates='citas')
    
    def __init__(self, fecha_hora_cita, estado_cita, notas, usuario, directivo):
        self.FechaHoraCita = fecha_hora_cita
        self.EstadoCita = estado_cita
        self.Notas = notas
        self.usuario = usuario
        self.directivo = directivo
        
    @property
    def obtenerDatos(self):
        return {
            'CitaID': self.CitaID,
            'FechaHoraCita': self.FechaHoraCita,
            'EstadoCita': self.EstadoCita,
            'Notas': self.Notas,
            'UsuarioID': self.usuario.UserID,
            'Usuario': self.usuario.obtenerDatos(),
            'DirectivoID': self.directivo.DirectivoID,
            'Directivo': self.directivo.obtenerDatos()
        }