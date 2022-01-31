import os
from flask import Flask, request, redirect, url_for, session, flash, send_from_directory
from flask import render_template
from werkzeug.utils import secure_filename
from web.servicios import autenticacion

UPLOAD_FOLDER = '../web/static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'xlsx', 'xls'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "abc"


# ----------------------PARA LA PANTALLA LOGIN--------------------------------------
@app.route('/')
def index():
    return redirect(url_for('login_cliente'))


@app.route('/login_customers', methods=['GET', 'POST'])
def login_cliente():
    error = None
    if request.method == 'POST':
        if not autenticacion.validar_credenciales_cliente(request.form['login_customer'], request.form['password']):
            error = 'User or Password incorrect'
        else:
            session['usuario_actual'] = request.form['login_customer']
            session['tipo_usuario'] = "customer"
            return render_template('inicio_cliente.html', messages={'login_customer': request.form['login_customer']})
    return render_template('login.html', error=error)


# PARA VOLVER A LA PAGINA DE INICIO
@app.route('/inicio_cliente')
def inicio_cliente():
    usuarios_cliente = autenticacion.obtener_usuarios_cliente()
    return render_template('inicio_cliente.html', usuarios=usuarios_cliente,
                           messages={'login_customer': session['usuario_actual']})


@app.route('/login_suppliers', methods=['GET', 'POST'])
def login_proveedor():
    error = None
    if request.method == 'POST':
        if not autenticacion.validar_credenciales_proveedor(request.form['login_supplier'],
                                                            request.form['password_supplier']):
            error = 'User or Password incorrect'
        else:
            session['usuario_actual'] = request.form['login_supplier']
            session['tipo_usuario'] = "supplier"
            return redirect(url_for('inicio_proveedor'))
    return render_template('login.html', error=error)


# ----------------------PRIMER PANTALLA PROVEEDOR (INICIO)--------------------------------------
# QUOTES IN PROCESS SUPPLIER
@app.route('/inicio_proveedor', methods=['GET'])
def inicio_proveedor():
    quotations = autenticacion.obtener_cotizaciones_loginsupplier(session['usuario_actual'])
    return render_template('inicio_proveedor.html', quotations=quotations,
                           messages={'login_supplier': session['usuario_actual']})


# QUOTES IN PROCESS SUPPLIER
@app.route('/quotes/<login_supplier>', methods=['GET', 'POST'])
def obtener_cotizaciones_loginsupplier(login_supplier):
    cotizaciones = autenticacion.obtener_cotizaciones_loginsupplier(login_supplier)
    return render_template('inicio_proveedor.html', quotations=cotizaciones,
                           messages={'login_supplier': session['usuario_actual']})


# ----------------------PARA LA PANTALLA ADD NEW QUOTE DEL CLIENTE--------------------------------------
# ABRIR LA PAG DE NEW QUOTE + SELECT PROVEEDOR
@app.route('/add_new_quote', methods=['GET'])
def add_new_quote():
    usuarios_proveedor = autenticacion.obtener_usuarios_proveedor()
    return render_template('add_new_quote.html', suppliers=usuarios_proveedor)


# PARA MOSTRAR EL SELECT CON LOS PROVEEDORES
@app.route('/suppliers/<login_supplier>')
def obtener_usuario_proveedor():
    usuario_proveedor = autenticacion.obtener_usuario_proveedor()
    return render_template('add_new_quote.html', supplier=usuario_proveedor)


# PARA ADJUNTAR ARCHIVOS
def subir_archivos(request, nombre_archivo):
    filename = ''
    if nombre_archivo not in request.files:
        flash('No file part')
        return filename
    file = request.files[nombre_archivo]
    # Si el usuario deja el campo vacío. request.files['file'] tendrá
    # un archivo vacio con nombre de archivo también vacío.
    if file.filename == '':
        print('No selected file')
        return filename
    if file:  # and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))  # Acá se guarda el archivo
    return filename


# En la base de datos almaceno el nombre que referencia al archivo en el sistema de ficheros.


# PARA GUARDAR COTIZACION
@app.route('/add_new_quote', methods=['POST', 'GET'])
def submit_quote():
    error = None
    if request.method == 'POST':
        filename_workfile = subir_archivos(request, 'workfile')
        filename_measures = subir_archivos(request, 'measures')
        if not autenticacion.crear_cotizacion(request.form['brand'],
                                              request.form['group'],
                                              request.form['style'],
                                              request.form['quantity'],
                                              request.form['supplier'],
                                              request.form['status'],
                                              request.form['dead_line'],
                                              request.form['comments'],
                                              request.form['team'],
                                              filename_workfile,
                                              filename_measures):
            error = 'Some information is incorrect'
        else:
            return redirect(url_for('obtener_cotizaciones'))
    return render_template('add_new_quote.html', error=error)


# ----------------------PARA LA PANTALLA QUOTE IN PROCESS--------------------------------------
# LISTAR COATIZACIONES
@app.route('/quotations', methods=['GET', 'POST'])
def obtener_cotizaciones():
    cotizaciones = autenticacion.obtener_cotizaciones()
    return render_template('quote_in_process.html', quotations=cotizaciones)


# ----------------------EDIT QUOTE DEL LADO DEL CLIENTE--------------------------------------
# ABRIR LA PAG EDIT QUOTE
@app.route('/edit_quote')
def edit_quote():
    cotizaciones = autenticacion.obtener_cotizaciones()
    return render_template('edit_quote.html', quotations=cotizaciones)

# MODIFICAR QUOTE
@app.route('/quotations/<id_quote>', methods=['GET', 'POST'])
def modificar_cotizacion(id_quote):
    error = None
    if request.method == 'POST':
        if not autenticacion.modificar_cotizaciones(request.form['brand'],
                                              request.form['group'],
                                              request.form['supplier'],
                                              request.form['team'],
                                              request.form['dead_line'],
                                              request.form['status'],
                                              request.form['quantity'],
                                              request.form['comments'],
                                              request.form['style'],
                                              filename_workfile,
                                              filename_measures):
            error = 'Some information is incorrect'
        else:
            return redirect(url_for('obtener_cotizaciones'))
    return redirect(url_for('obtener_cotizaciones'))


# ----------------------PARA LA PANTALLA SUPPLIER DATA BASE--------------------------------------

# AGREGAR USUARIO PROVEEDOR
@app.route('/add_suppliers', methods=['GET', 'POST'])
def crear_usuario_proveedor():
    error = None
    if request.method == 'POST':
        if not autenticacion.crear_usuario_proveedor(request.form['login_supplier'],
                                                     request.form['password'],
                                                     request.form['email'],
                                                     request.form['company']):
            error = 'No se pudo crear el usuario'
        else:
            return redirect(url_for('obtener_usuarios_proveedor'))
    return render_template('supplier_database.html', error=error)


# LISTAR PROVEEDORES
@app.route('/suppliers')
def obtener_usuarios_proveedor():
    usuarios_proveedor = autenticacion.obtener_usuarios_proveedor()
    return render_template('supplier_database.html', suppliers=usuarios_proveedor)


# EDITAR PROVEEDORES !!!! pendiente!!!!
@app.route('/suppliers/<login_supplier>/editar', methods=['POST'])
def editar_usuario_proveedor(login_supplier):
    error = None
    if request.method == 'POST':
        if not autenticacion.editar_usuario_proveedor(request.form['login_supplier'],
                                                      request.form['password'],
                                                      request.form['email'],
                                                      request.form['company']):
            error = 'Some information is incorrect'
        else:
            return redirect(url_for('obtener_usuarios_proveedor'))
    return redirect(url_for('obtener_usuarios_proveedor'))


# ELIMINAR PROVEEDORES

@app.route('/suppliers/<login_supplier>/eliminar', methods=['POST'])
def borrar_usuario_proveedor(login_supplier):
    if request.method == 'POST':
        autenticacion.borrar_usuario_proveedor(login_supplier)
    return redirect(url_for('obtener_usuarios_proveedor'))


# RECUPERAR UN ARCHIVO GUARDADO
# @app.route('/uploads/<filename>')
# def get_file(filename):
#    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
# ponemos un return redirect(url_for('get_file', filename=filename) esto va en la funcion subir archivo

if __name__ == '__main__':
    app.debug = True
    app.run(port=5002)
