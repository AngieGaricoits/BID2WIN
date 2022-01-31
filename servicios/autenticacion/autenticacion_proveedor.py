from datos.modelos import usuario_proveedor as modelo_usuario_proveedor
from datetime import datetime


def _existe_usuario_proveedor(login_supplier, password):
    usuarios = modelo_usuario_proveedor.obtener_usuarios_por_login_password(login_supplier, password)
    return not len(usuarios) == 0


def crear_usuario_proveedor(login_supplier, password, email, company):
    if not _existe_usuario_proveedor(login_supplier, password):
        modelo_usuario_proveedor.crear_usuario_proveedor(login_supplier, password, email, company)
    else:
        raise Exception('El usuario ya existe')


def modificar_usuario_proveedor(login_supplier, datos_usuario_proveedor):
    modelo_usuario_proveedor.modificar_usuario_proveedor(login_supplier, datos_usuario_proveedor)


def obtener_usuarios_proveedor():
    return modelo_usuario_proveedor.obtener_usuarios_proveedor()


def obtener_usuario_proveedor(login_supplier):
    customer = modelo_usuario_proveedor.obtener_usuario_proveedor(login_supplier)
    if len(customer) == 0:
        raise Exception("El usuario no existe")
    return customer[0]


def borrar_usuario_proveedor(login_supplier):
    modelo_usuario_proveedor.borrar_usuario_proveedor(login_supplier)


def _crear_sesion_proveedor(login_supplier):
    hora_actual = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = hora_actual.strftime("%d/%m/%Y %H:%M:%S")
    return modelo_usuario_proveedor.crear_sesion_proveedor(login_supplier, dt_string)


def login_proveedor(login_supplier, password):
    if _existe_usuario_proveedor(login_supplier, password):
        usuario_proveedor = modelo_usuario_proveedor.obtener_usuarios_por_login_password(login_supplier, password)[0]
        return _crear_sesion_proveedor(usuario_proveedor['Supplier'])
    else:
        raise Exception("El usuario no existe o la clave es invalida")


def validar_sesion_proveedor(id_sesion_proveedor):
    sesiones = modelo_usuario_proveedor.obtener_sesion_proveedor(id_sesion_proveedor)
    if len(sesiones) == 0:
        return False
    elif (datetime.now() - datetime.strptime(sesiones[0]['fecha_hora'], "%d/%m/%Y %H:%M:%S")).total_seconds() > 60:
        # Sesion expirada
        return False
    else:
        return True
