from app import db


class Alumno(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nombre = db.Column(db.String(100), primary_key=True)
    apellido = db.Column(db.String(100), primary_key=True)
    idAula = db.Column(db.Integer, primary_key=True)
