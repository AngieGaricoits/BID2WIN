from datos.base_de_datos import BaseDeDatos

# funcion para crear usuario proveedor
def crear_usuario_proveedor(login_supplier, password, email, company):
    crear_usuario_proveedor_sql = f"""
        INSERT or IGNORE INTO SUPPLIER(LOGIN_SUPPLIER, PASSWORD, EMAIL, COMPANY)
        VALUES ('{login_supplier}', '{password}', '{email}', '{company}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_usuario_proveedor_sql)


# funcion modificar usuario proveedor
def modificar_usuario_proveedor(login_supplier, datos_usuario_proveedor):
    modificar_usuario_proveedor_sql = f"""
        UPDATE SUPPLIER
        SET PASSWORD= '{datos_usuario_proveedor["password"]}', EMAIL= '{datos_usuario_proveedor["email"]}', COMPANY= '{datos_usuario_proveedor["company"]}' 
        WHERE LOGIN_SUPPLIER='{login_supplier}'
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(modificar_usuario_proveedor_sql)

# funcion para listar todos los proveedor
def obtener_usuarios_proveedor():
    obtener_usuarios_proveedor_sql = f"""
        SELECT login_supplier, email, company
        FROM SUPPLIER
    """
    bd = BaseDeDatos()
    return [{"nombre": registro[0],
             "email": registro[1],
             "company": registro[2]
             } for registro in bd.ejecutar_sql(obtener_usuarios_proveedor_sql)]


# funcion obtener un proveedor por nombre
def obtener_usuario_proveedor(login_supplier):
    obtener_usuario_proveedor_sql = f"""
        SELECT login_supplier, email, company
        FROM SUPPLIER
        WHERE LOGIN_SUPPLIER = {login_supplier}
    """
    bd = BaseDeDatos()
    return [{"nombre": registro[0],
             "email": registro[1],
             "company": registro[2]
             } for registro in bd.ejecutar_sql(obtener_usuario_proveedor_sql)]


# funcion borrar proveedor por nombre
def borrar_usuario_proveedor(login_supplier):
    obtener_usuarios_proveedor_sql = f"""
        DELETE
        FROM SUPPLIER
        WHERE LOGIN_SUPPLIER='{login_supplier}'
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(obtener_usuarios_proveedor_sql)


def obtener_usuarios_por_login_password(login_supplier, password):
    obtener_usuarios_por_login_password_sql = f"""
            SELECT login_supplier, email
            FROM SUPPLIER u
            WHERE UPPER(LOGIN_SUPPLIER)=UPPER('{login_supplier}') and PASSWORD='{password}' 
        """
    bd = BaseDeDatos()
    return [{"Supplier": registro[0],
             "Email": registro[1]
             } for registro in bd.ejecutar_sql(obtener_usuarios_por_login_password_sql)]

def crear_sesion_proveedor(login_supplier, dt_string):
    crear_sesion_proveedor_sql = f"""
               INSERT INTO SESIONES_SUPPLIER(LOGIN_SUPPLIER, FECHA_HORA)
               VALUES ('{login_supplier}', '{dt_string}')
    """
    bd = BaseDeDatos()
    return bd.ejecutar_sql(crear_sesion_proveedor_sql, True)


def obtener_sesion_proveedor(id_sesion_proveedor):
    obtener_sesion_proveedor_sql = f"""
        SELECT ID, LOGIN_SUPPLIER, FECHA_HORA FROM SESIONES_SUPPLIER WHERE ID = {id_sesion_supplier}
    """
    bd = BaseDeDatos()
    return [{"id": registro[0],
             "login_supplier": registro[1],
             "fecha_hora": registro[2]}
            for registro in bd.ejecutar_sql(obtener_sesion_proveedor_sql)]
