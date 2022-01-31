from flask import Flask, request, jsonify, render_template
from servicios.autenticacion import autenticacion_cliente
from servicios.autenticacion import autenticacion_proveedor
from servicios.cotizacion import cotizacionn

app = Flask(__name__)

@app.route('/')
def get_index():
    titulo_bid2win = 'BID2WIN'
    return render_template('index.html', titulo=titulo_bid2win)

# Endpoint crear nuevo cliente
@app.route('/customers', methods=['POST'])
def crear_usuario_cliente():
    datos_usuario_cliente = request.get_json()
    if 'login_customer' not in datos_usuario_cliente:
        return 'El nombre de usuario es requerido', 412
    if 'password' not in datos_usuario_cliente:
        return 'La clave es requerida', 412
    if 'email' not in datos_usuario_cliente:
        return 'El email es requerido', 412
    try:
        autenticacion_cliente.crear_usuario_cliente(datos_usuario_cliente['login_customer'],
                                                    datos_usuario_cliente['password'],
                                                    datos_usuario_cliente['email'], datos_usuario_cliente['team'])
    except Exception:
        return "El usuario ya existe", 412
    return 'OK', 200


# Endpoint modificar un cliente
@app.route('/customers/<login_customer>', methods=['PUT'])
def modificar_usuario_cliente(login_customer):
    datos_usuario_cliente = request.get_json()
    if 'password' not in datos_usuario_cliente:
        return 'La clave es requerida', 412
    if 'email' not in datos_usuario_cliente:
        return 'El email es requerido', 412
    if 'team' not in datos_usuario_cliente:
        return 'El team es requerido', 412
    try:
        autenticacion_cliente.modificar_usuario_cliente(login_customer, datos_usuario_cliente)
    except Exception:
        return 'Usuario no encontrado', 404
    return "OK", 200


# Endpoint listar cliente
@app.route('/customers', methods=['GET'])
def obtener_usuarios_cliente():
    return jsonify(autenticacion_cliente.obtener_usuarios_cliente())


# Endpoint obtener un cliente por nombre
@app.route('/customers/<login_customer>', methods=['GET'])
def obtener_usuario_cliente(login_customer):
    try:
        customer = autenticacion_cliente.obtener_usuario_cliente(login_customer)
        return jsonify(customer)
    except Exception:
        return 'Usuario no encontrado', 404


# Endpoint obtener un cliente por team , no me funciono porque no es primary key
@app.route('/customers/<team>', methods=['GET'])
def obtener_usuario_cliente_team(team):
    try:
        equipo = autenticacion_cliente.obtener_usuario_cliente_team(team)
        return jsonify(equipo)
    except Exception:
        return 'Usuario no encontrado', 404


# Endpoint borrar un cliente
@app.route('/customers/<login_customer>', methods=['DELETE'])
def borrar_usuario_cliente(login_customer):
    autenticacion_cliente.borrar_usuario_cliente(login_customer)
    return "Borrado", 200


# Endpoint login
@app.route('/login_customers', methods=['POST'])
def login_cliente():
    datos_usuario_cliente = request.get_json()
    if 'login_customer' not in datos_usuario_cliente:
        return 'El nombre de usuario es requerido', 412
    if 'password' not in datos_usuario_cliente:
        return 'La clave es requerida', 412
    id_sesion_cliente = autenticacion_cliente.login_cliente(datos_usuario_cliente['login_customer'],
                                                            datos_usuario_cliente['password'])
    return jsonify({"id_sesion_cliente": id_sesion_cliente})


# ------------------------------------------------SUPPLIER-------------------------------------------------

# Endpoint crear nuevo proveedor
@app.route('/suppliers', methods=['POST'])
def crear_usuario_proveedor():
    datos_usuario_proveedor = request.get_json()
    if 'login_supplier' not in datos_usuario_proveedor:
        return 'El nombre de usuario es requerido', 412
    if 'password' not in datos_usuario_proveedor:
        return 'La clave es requerida', 412
    if 'email' not in datos_usuario_proveedor:
        return 'El email es requerido', 412
    autenticacion_proveedor.crear_usuario_proveedor(datos_usuario_proveedor['login_supplier'],
                                                    datos_usuario_proveedor['password'],
                                                    datos_usuario_proveedor['email'],
                                                    datos_usuario_proveedor['company'])
    return 'OK', 200


# Endpoint modificar un proveedor
@app.route('/suppliers/<login_supplier>', methods=['PUT'])
def modificar_usuario_proveedor(login_supplier):
    datos_usuario_proveedor = request.get_json()
    if 'password' not in datos_usuario_proveedor:
        return 'La clave es requerida', 412
    if 'email' not in datos_usuario_proveedor:
        return 'El email es requerido', 412
    if 'company' not in datos_usuario_proveedor:
        return 'La empresa es requerida', 412
    try:
        autenticacion_proveedor.modificar_usuario_proveedor(login_supplier, datos_usuario_proveedor)
    except Exception:
        return 'Proveedor no encontrado', 404
    return "OK", 200


# Endpoint listar proveedor
@app.route('/suppliers', methods=['GET'])
def obtener_usuarios_proveedor():
    return jsonify(autenticacion_proveedor.obtener_usuarios_proveedor())


# Endpoint obtener un proveedor por nombre
@app.route('/suppliers/<login_supplier>', methods=['GET'])
def obtener_usuario_proveedor(login_supplier):
    try:
        supplier = autenticacion_proveedor.obtener_usuario_proveedor(login_supplier)
        return jsonify(supplier)
    except Exception:
        return 'Proveedor no encontrado', 404


# Endpoint borrar un proveedor
@app.route('/suppliers/<login_supplier>', methods=['DELETE'])
def borrar_usuario_proveedor(login_supplier):
    autenticacion_proveedor.borrar_usuario_proveedor(login_supplier)
    return "Borrado", 200


# Endpoint login
@app.route('/login_suppliers', methods=['POST'])
def login_proveedor():
    datos_usuario_proveedor = request.get_json()
    if 'login_supplier' not in datos_usuario_proveedor:
        return 'El nombre de usuario es requerido', 412
    if 'password' not in datos_usuario_proveedor:
        return 'La clave es requerida', 412
    id_sesion_proveedor = autenticacion_proveedor.login_proveedor(datos_usuario_proveedor['login_supplier'],
                                                           datos_usuario_proveedor['password'])
    return jsonify({"id_sesion_proveedor": id_sesion_proveedor})

# ------------------------------------------------COTIZACION-------------------------------------------------

# Endpoint crear nueva cotizacion
@app.route('/quotations', methods=['POST'])
def crear_cotizacion():
    datos_cotizacion = request.get_json()
    if 'brand' not in datos_cotizacion:
        return 'La marca es requerida', 412
    if 'supplier' not in datos_cotizacion:
        return 'El proveedor es requerido', 412
    if 'quantity_color' not in datos_cotizacion:
        return 'La cantidad es requerida', 412
    cotizacionn.crear_cotizacion(datos_cotizacion['team'], datos_cotizacion['supplier'], datos_cotizacion['brand'],
                                 datos_cotizacion['quantity_color'], datos_cotizacion['group_order'],
                                 datos_cotizacion['style'],
                                 datos_cotizacion['status'], datos_cotizacion['workfile'],
                                 datos_cotizacion['measures'],
                                 datos_cotizacion['dead_line'], datos_cotizacion['comments'])
    return 'OK', 200


# Endpoint modificar una cotizacion
@app.route('/quotations/<id_quote>', methods=['PUT'])
def modificar_cotizacion(id_quote):
    datos_cotizacion = request.get_json()
    if 'brand' not in datos_cotizacion:
        return 'La marca es requerida', 412
    if 'style' not in datos_cotizacion:
        return 'El style es requerido', 412
    if 'group_order' not in datos_cotizacion:
        return 'La grupo requerido', 412
    cotizacionn.modificar_cotizacion(id_quote, datos_cotizacion)
    return "OK", 200


# Endpoint listar cotizaciones
@app.route('/quotations', methods=['GET'])
def obtener_cotizaciones():
    return jsonify(cotizacionn.obtener_cotizaciones())


# Endpoint obtener una cotizacion por id
@app.route('/quotations/<id_quote>', methods=['GET'])
def obtener_cotizacion(id_quote):
    try:
        cotizacion = cotizacionn.obtener_cotizacion(id_quote)
        return jsonify(cotizacion)
    except Exception:
        return 'Cotizacion no encontrada', 404

# Endpoint obtener cotizaciones por suppliers
@app.route('/quotes/<login_supplier>', methods=['GET'])
def obtener_cotizaciones_proveedor(login_supplier):
    try:
        cotizaciones_supplier = cotizacionn.obtener_cotizaciones_proveedor(login_supplier)
        return jsonify(cotizaciones_supplier)
    except Exception as e:
        print(e)
        return 'No quote in process for this supplier', 404


# Endpoint borrar una cotizacion
@app.route('/quotations/<id_quote>', methods=['DELETE'])
def borrar_cotizacion(id_quote):
    cotizacionn.borrar_cotizacion(id_quote)
    return "Borrado", 200


# ------------------------------------------------STATUS-------------------------------------------------

# Endpoint crear un status
@app.route('/status', methods=['POST'])
def crear_status():
    datos_status = request.get_json()
    if 'status' not in datos_status:
        return 'El status es requerido', 412
    if 'quote_id' not in datos_status:
        return 'El id de cotizacion es requerido', 412
    if 'date' not in datos_status:
        return 'La fecha es requerida', 412
    status.crear_status(datos_status['status_id'], datos_status['status'], datos_status['quote_id'],
                        datos_status['date'])
    return 'OK', 200


if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
