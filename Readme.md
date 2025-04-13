## Compra y venta de autos con Flask
Este es un proyecto de ejemplo que utiliza Flask para crear una aplicación web de compra y venta de autos. La aplicación permite a los usuarios listar, agregar, editar y eliminar autos.

## Estructura del proyecto
```plaintext
carshop_flask/  
├── app.py                     # Aplicación principal
├── models.py                  # Modelos de DB (SQLAlchemy)
├── templates/                 # Templates globales
│   ├── base.html              # Layout base
│   └── autos/                 # Templates específicos de autos
│       ├── list.html          # Lista de autos
│       └── form.html          # Formulario de autos
├── autos/                     # Módulo de autos (Blueprint)
│   ├── __init__.py
│   └── routes.py              # Rutas CRUD de autos
└── clientes/                  # Módulo de clientes (opcional)
    ├── __init__.py
    └── routes.py
```


## Posibles Mejoras

### Historial de compras: Página para ver qué autos ha comprado un cliente.

### Validaciones: Que un auto no se pueda vender dos veces.

### Autenticación: Blueprint auth/ para vendedores (ej: Flask-Login).
