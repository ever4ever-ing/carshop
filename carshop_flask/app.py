from flask import Flask, redirect, url_for
from models import db, Auto
from autos.routes import autos_bp
from clientes.routes import clientes_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///carshop.db'  # Archivo en el mismo directorio
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar DB
db.init_app(app)
with app.app_context():
    db.create_all() # Crear la base de datos si no existe
    if not Auto.query.first():
        db.session.add(Auto(marca="Ejemplo", modelo="Test", precio=10000))
        db.session.commit()

# Registrar Blueprints
app.register_blueprint(autos_bp)
app.register_blueprint(clientes_bp)

# Ruta de inicio
@app.route('/')
def home():
    return redirect(url_for('autos.list_autos'))

if __name__ == '__main__':
    app.run(debug=True)