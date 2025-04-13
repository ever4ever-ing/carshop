from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Auto

autos_bp = Blueprint('autos', __name__, url_prefix='/autos', template_folder='templates')

# --- CRUD ---
@autos_bp.route('/')
def list_autos():
    autos = Auto.query.all()
    return render_template('autos/list.html', autos=autos)

@autos_bp.route('/crear', methods=['GET', 'POST'])
def crear_auto():
    if request.method == 'POST':
        print("Datos recibidos:", request.form)  # Debug en consola
        auto = Auto(
            marca=request.form['marca'],
            modelo=request.form['modelo'],
            precio=float(request.form['precio'])
        )
        db.session.add(auto)
        db.session.commit()  # ¡Este commit es crucial!
        print("Auto guardado:", auto)  # Verifica en consola
        return redirect(url_for('autos.list_autos'))
    return render_template('autos/form.html')

@autos_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_auto(id):
    auto = Auto.query.get_or_404(id)
    if request.method == 'POST':
        auto.marca = request.form['marca']
        auto.modelo = request.form['modelo']
        auto.precio = float(request.form['precio'])
        db.session.commit()
        return redirect(url_for('autos.list_autos'))
    return render_template('autos/form.html', auto=auto)

@autos_bp.route('/eliminar/<int:id>')
def eliminar_auto(id):
    auto = Auto.query.get_or_404(id)
    db.session.delete(auto)
    db.session.commit()
    return redirect(url_for('autos.list_autos'))