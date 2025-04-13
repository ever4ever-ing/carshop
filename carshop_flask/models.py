from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Auto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(80), nullable=False)
    modelo = db.Column(db.String(80), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    vendido = db.Column(db.Boolean, default=False)
    venta = db.relationship('Venta', backref='auto', uselist=False)  # 1:1 con Venta

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True)
    ventas = db.relationship('Venta', backref='cliente')  # 1:N con Venta

class Venta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, default=db.func.now())
    auto_id = db.Column(db.Integer, db.ForeignKey('auto.id'))
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))

    
    def __repr__(self):
        return f"Auto({self.marca}, {self.modelo})"