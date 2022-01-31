from datos.modelos import usuario_cliente as modelo_usuario_cliente
from datetime import datetime


def _existe_usuario_cliente(login_customer, password):
    usuarios = modelo_usuario_cliente.obtener_usuarios_por_login_password(login_customer, password)
    return not len(usuarios) == 0


def crear_usuario_cliente(login_customer, password, email, team):
    if not _existe_usuario_cliente(login_customer, password):
        modelo_usuario_cliente.crear_usuario_cliente(login_customer, password, email, team)
    else:
        raise Exception('El usuario ya existe')


def modificar_usuario_cliente(login_customer, datos_usuario_cliente):
    modelo_usuario_cliente.modificar_usuario_cliente(login_customer, datos_usuario_cliente)


def obtener_usuarios_cliente():
    return modelo_usuario_cliente.obtener_usuarios_cliente()


def obtener_usuario_cliente(login_customer):
    customer = modelo_usuario_cliente.obtener_usuario_cliente(login_customer)
    if len(customer) == 0:
        raise Exception("El usuario no existe")
    return customer[0]


def obtener_usuario_cliente_team(team):
    equipo = modelo_usuario_cliente.obtener_usuario_cliente_team(team)
    if len(equipo) == 0:
        raise Exception("El usuario no existe")
    return equipo[0]


def borrar_usuario_cliente(login_customer):
    modelo_usuario_cliente.borrar_usuario_cliente(login_customer)


def _crear_sesion_cliente(login_customer):
    hora_actual = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = hora_actual.strftime("%d/%m/%Y %H:%M:%S")
    return modelo_usuario_cliente.crear_sesion_cliente(login_customer, dt_string)


def login_cliente(login_customer, password):
    if _existe_usuario_cliente(login_customer, password):
        usuario_cliente = modelo_usuario_cliente.obtener_usuarios_por_login_password(login_customer, password)[0]
        return _crear_sesion_cliente(usuario_cliente['Customer'])
    else:
        raise Exception("El usuario no existe o la clave es invalida")


def validar_sesion_cliente(id_sesion_cliente):
    sesiones = modelo_usuario_cliente.obtener_sesion_cliente(id_sesion_cliente)
    if len(sesiones) == 0:
        return False
    elif (datetime.now() - datetime.strptime(sesiones[0]['fecha_hora'], "%d/%m/%Y %H:%M:%S")).total_seconds() > 60:
        # Sesion expirada
        return False
    else:
        return True
