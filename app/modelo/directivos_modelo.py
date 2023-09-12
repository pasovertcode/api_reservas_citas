from app.utils.db import db

class Directivo(db.Model):
    DirectivoID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Departamento = db.Column(db.String(100), nullable=False)
    Estado = db.Column(db.String(255))

    # Relación con la tabla de Usuarios (uno a uno)
    UsuarioID = db.Column(db.Integer, db.ForeignKey('usuario.UserID'))
    usuario = db.relationship('Usuario', back_populates='directivo')

    # Relación con la tabla de Citas (uno a muchos)
    citas = db.relationship('Cita', back_populates='directivo')

    def __init__(self, departamento, estado, IDusuario, usuario):
        self.Departamento = departamento
        self.Estado = estado
        self.UsuarioID = IDusuario
        self.usuario = usuario

    @property
    def obtenerDatos(self):
        return {
            'DirectivoID': self.DirectivoID,
            'Departamento': self.Departamento,
            'Estado': self.Estado,
            'UsuarioID': self.usuario.UserID,  # incluir datos del usuario relacionado
            'Usuario': self.usuario.obtenerDatos  # Incluye datos completos del usuario como diccionario
        }