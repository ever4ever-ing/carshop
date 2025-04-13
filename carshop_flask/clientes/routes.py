from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Cliente, Auto, Venta
from datetime import datetime

clientes_bp = Blueprint('clientes', __name__, url_prefix='/clientes', template_folder='templates')

# --- CRUD Clientes ---
@clientes_bp.route('/')
def list_clientes():
    clientes = Cliente.query.all()
    return render_template('clientes/list.html', clientes=clientes)

@clientes_bp.route('/crear', methods=['GET', 'POST'])
def crear_cliente():
    if request.method == 'POST':
        cliente = Cliente(
            nombre=request.form['nombre'],
            email=request.form['email']
        )
        db.session.add(cliente)
        db.session.commit()
        return redirect(url_for('clientes.list_clientes'))
    return render_template('clientes/form.html')

# --- Registrar Venta ---
@clientes_bp.route('/comprar/<int:auto_id>', methods=['GET', 'POST'])
def comprar_auto(auto_id):
    auto = Auto.query.get_or_404(auto_id)
    clientes = Cliente.query.all()
    
    if request.method == 'POST':
        cliente_id = request.form['cliente_id']
        cliente = Cliente.query.get_or_404(cliente_id)
        
        # Crear la venta y marcar auto como vendido
        venta = Venta(auto_id=auto.id, cliente_id=cliente.id)
        auto.vendido = True
        
        db.session.add(venta)
        db.session.commit()
        return redirect(url_for('autos.list_autos'))
    
    return render_template('clientes/comprar.html', auto=auto, clientes=clientes)