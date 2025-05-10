from app import db


class Libro(db.Model):
    __tablename__ = 'libros'

    #Crear las columnas de la tabla libros
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(100), nullable =  False)
    autor = db.Column(db.String(100), nullable = False)
    editorial = db.Column(db.String(100), nullable = False)