from app.utils.db import db

class Usuario(db.Model):
    UserID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    NombreCompleto = db.Column(db.String(255), nullable=False)
    CorreoElectronico = db.Column(db.String(255), nullable=False, unique=True)
    Identificacion = db.Column(db.String(20))
    Contraseña = db.Column(db.String(255), nullable=False)
    Rol = db.Column(db.String(50), nullable=False)
    Estado = db.Column(db.String(255))

    # Relación con la tabla de Directivos (uno a uno)
    directivo = db.relationship('Directivo', back_populates='usuario', uselist=False)

    # Relación con la tabla de Citas (uno a muchos)
    citas = db.relationship('Cita', back_populates='usuario')

    def __init__(self, nombre_completo, correo_electronico, identificacion, contraseña, rol, estado):
        self.NombreCompleto = nombre_completo
        self.CorreoElectronico = correo_electronico
        self.Identificacion = identificacion
        self.Contraseña = contraseña
        self.Rol = rol
        self.Estado = estado

    @property
    def obtenerDatos(self):
        return {
            'UserID': self.UserID,
            'NombreCompleto': self.NombreCompleto,
            'CorreoElectronico': self.CorreoElectronico,
            'Identificacion': self.Identificacion,
            'Contraseña': self.Contraseña,
            'Rol': self.Rol,
            'Estado': self.Estado
        }