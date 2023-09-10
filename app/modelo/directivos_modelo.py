from app import db

class Directivo(db.Model):
    DirectivoID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Departamento = db.Column(db.String(100), nullable=False)
    HorarioDisponibilidad = db.Column(db.String(255), nullable=False)
    Estado = db.Column(db.String(255))

    # Relación con la tabla de Usuarios (uno a uno)
    UsuarioID = db.Column(db.Integer, db.ForeignKey('usuario.UserID'))
    usuario = db.relationship('Usuario', back_populates='directivo')

    # Relación con la tabla de Citas (uno a muchos)
    citas = db.relationship('Cita', back_populates='directivo')
