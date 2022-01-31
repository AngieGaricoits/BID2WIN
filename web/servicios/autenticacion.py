import requests

from web.servicios import rest_api


def validar_credenciales_cliente(login_customer, password):
    body = {"login_customer": login_customer,
            "password": password}
    respuesta = requests.post(f'{rest_api.API_URL}/login_customers', json=body)
    # Solo verificamos el codigo de la respuesta en este caso
    return respuesta.status_code == 200

def validar_credenciales_proveedor(login_supplier, password):
    body = {"login_supplier": login_supplier,
            "password": password}
    respuesta = requests.post(f'{rest_api.API_URL}/login_suppliers', json=body)
    # Solo verificamos el codigo de la respuesta en este caso
    return respuesta.status_code == 200

def obtener_usuarios_cliente():
    respuesta = requests.get(f'{rest_api.API_URL}/customers')
    return respuesta.json()

def obtener_usuarios_proveedor():
    respuesta = requests.get(f'{rest_api.API_URL}/suppliers')
    return respuesta.json()

def obtener_usuario_proveedor(login_supplier):
    respuesta = requests.get(f'{rest_api.API_URL}/suppliers/{login_supplier}')
    return respuesta.json()

def crear_usuario_proveedor(login_supplier, password, email, company):
    body = {"login_supplier": login_supplier,
            "password": password,
            "email": email,
            "company": company}
    respuesta = requests.post(f'{rest_api.API_URL}/suppliers', json=body)
    return respuesta.status_code == 200

def borrar_usuario_proveedor(login_supplier):
    body = {"login_supplier": login_supplier}
    respuesta = requests.delete(f'{rest_api.API_URL}/suppliers/{login_supplier}', json=body)
    return respuesta.status_code == 200

def editar_usuario_proveedor(login_supplier, password, email, company):
    body = {"login_supplier": login_supplier,
            "password": password,
            "email": email,
            "company": company}
    respuesta = requests.put(f'{rest_api.API_URL}/suppliers/{login_supplier}', json=body)
    return respuesta.status_code == 200


def crear_cotizacion(brand, group, style, quantity, supplier, status, dead_line, comments, team, workfile, measures):
    """

    :rtype: object
    """
    body = {"brand": brand,
            "group_order": group,
            "style": style,
            "quantity_color": quantity,
            "supplier": supplier,
            "status": status,
            "dead_line": dead_line,
            "comments": comments,
            "team": team,
            "workfile": workfile,
            "measures": measures
            }
    respuesta = requests.post(f'{rest_api.API_URL}/quotations', json=body)
    return respuesta.status_code == 200

def obtener_cotizaciones_loginsupplier(login_supplier):
    respuesta = requests.get(f'{rest_api.API_URL}/quotes/{login_supplier}')
    return respuesta.json()

def obtener_cotizaciones():
    respuesta = requests.get(f'{rest_api.API_URL}/quotations')
    return respuesta.json()

"""
def modificar_cotizaciones(brand, group, supplier, team, dead_line, status, workfile, measures, quantity, comments, style):
    body = {"brand": brand,
            "group_order": group,
            "supplier": supplier,
            "team": team,
            "dead_line": dead_line,
            "status": status,
            "workfile": workfile,
            "measures": measures,
            "quantity_color": quantity,
            "comments": comments,
            "style": style}
    respuesta = requests.put(f'{rest_api.API_URL}/quotations/{id_quote}', json=body)
    return respuesta.status_code == 200"""