from app.utils.db import db


class DirectivoHorario(db.Model):
    DirectivoHorarioID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    DirectivoID = db.Column(db.Integer, db.ForeignKey('directivo.DirectivoID'), nullable=False)
    HorarioID = db.Column(db.Integer, db.ForeignKey('horarios_disponibilidad.HorarioID'), nullable=False)

    directivo = db.relationship('Directivo', backref=db.backref('directivos_horarios', cascade='all, delete-orphan'))
    horario_disponibilidad = db.relationship('HorarioDisponibilidad', backref=db.backref('directivos_horarios', cascade='all, delete-orphan'))

    def __ini__(self, DirectivoID, HorarioID):
        self.DirectivoID = DirectivoID
        self.HorarioID = HorarioID

    def getDatos(self):
        return {
            'DirectivoHorarioID': self.DirectivoHorarioID,
            'Directivo': self.directivo.getDatos,
            'HorarioDisponibilidad': self.horario_disponibilidad.getDatos
        }