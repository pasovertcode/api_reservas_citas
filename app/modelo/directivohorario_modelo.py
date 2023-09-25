from app.utils.db import db


class DirectivoHorario(db.Model):
    
    DirectivoHorarioID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    DirectivoID = db.Column(db.Integer, db.ForeignKey('directivo.DirectivoID'), nullable=False)
    directivo = db.relationship('Directivo', foreign_keys=[DirectivoID])
    HorarioID = db.Column(db.Integer, db.ForeignKey('Horario_Disponibilidad.HorarioID'), nullable=False)
    Horario_disponibilidad = db.relationship('HorarioDisponibilidad', foreign_keys=[HorarioID])

    def __ini__(self, DirectivoID, HorarioID, directivo):
        self.DirectivoID = DirectivoID
        self.HorarioID = HorarioID
        self.Directivo = directivo

    def getDatos(self):
        return {
            'DirectivoHorarioID': self.DirectivoHorarioID,
            'Directivo': self.Directivo.getDatos,
            'HorarioDisponibilidad': self.Horario_disponibilidad.getDatos
        }