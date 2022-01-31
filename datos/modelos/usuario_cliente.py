from datos.base_de_datos import BaseDeDatos


# funcion para crear usuario cliente
def crear_usuario_cliente(login_customer, password, email, team):
    crear_usuario_cliente_sql = f"""
        INSERT INTO CUSTOMER(LOGIN_CUSTOMER, PASSWORD, EMAIL, TEAM)
        VALUES ('{login_customer}', '{password}', '{email}', '{team}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_usuario_cliente_sql)


# funcion modificar usuario cliente
def modificar_usuario_cliente(login_customer, datos_usuario_cliente):
    modificar_usuario_cliente_sql = f"""
        UPDATE CUSTOMER
        SET PASSWORD= '{datos_usuario_cliente["password"]}', EMAIL= '{datos_usuario_cliente["email"]}', TEAM= '{datos_usuario_cliente["team"]}' 
        WHERE LOGIN_CUSTOMER='{login_customer}'
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(modificar_usuario_cliente_sql)


# funcion para listar todos los clientes
def obtener_usuarios_cliente():
    obtener_usuarios_cliente_sql = f"""
        SELECT login_customer, email, team
        FROM CUSTOMER
    """
    bd = BaseDeDatos()
    return [{"nombre": registro[0],
             "email": registro[1],
             "team": registro[2]
             } for registro in bd.ejecutar_sql(obtener_usuarios_cliente_sql)]


# funcion obtener un cliente por nombre
def obtener_usuario_cliente(login_customer):
    obtener_usuario_cliente_sql = f"""
        SELECT login_customer, email, team
        FROM CUSTOMER
        WHERE LOGIN_CUSTOMER = {login_customer}
    """
    bd = BaseDeDatos()
    return [{"nombre": registro[0],
             "email": registro[1],
             "team": registro[2]
             } for registro in bd.ejecutar_sql(obtener_usuario_cliente_sql)]


# funcion obtener un cliente por team, no me funciono porque no es primary key
def obtener_usuario_cliente_team(team):
    obtener_usuario_cliente_team_sql = f"""
        SELECT login_customer, email, team
        FROM CUSTOMER
        WHERE TEAM = {team}
    """
    bd = BaseDeDatos()
    return [{"nombre:": registro[0],
             "email": registro[1],
             "team": registro[2]
             } for registro in bd.ejecutar_sql(obtener_usuario_cliente_team_sql)]


# funcion borrar cliente por nombre
def borrar_usuario_cliente(login_customer):
    obtener_usuarios_cliente_sql = f"""
        DELETE
        FROM CUSTOMER
        WHERE LOGIN_CUSTOMER = {login_customer}
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(obtener_usuarios_cliente_sql)


def obtener_usuarios_por_login_password(login_customer, password):
    obtener_usuarios_por_login_password_sql = f"""
            SELECT login_customer, email, team
            FROM CUSTOMER u
            WHERE UPPER(LOGIN_CUSTOMER)=UPPER('{login_customer}') and PASSWORD='{password}' 
    """
    bd = BaseDeDatos()
    return [{"Customer": registro[0],
             "Email": registro[1],
             "Team": registro[2]
             } for registro in bd.ejecutar_sql(obtener_usuarios_por_login_password_sql)]


def crear_sesion_cliente(login_customer, dt_string):
    crear_sesion_cliente_sql = f"""
               INSERT INTO SESIONES_CUSTOMER(LOGIN_CUSTOMER, FECHA_HORA)
               VALUES ('{login_customer}', '{dt_string}')
    """
    bd = BaseDeDatos()
    return bd.ejecutar_sql(crear_sesion_cliente_sql, True)


def obtener_sesion_cliente(id_sesion_cliente):
    obtener_sesion_cliente_sql = f"""
        SELECT ID, LOGIN_CUSTOMER, FECHA_HORA FROM SESIONES_CUSTOMER WHERE ID = {id_sesion_cliente}
    """
    bd = BaseDeDatos()
    return [{"id": registro[0],
             "login_customer": registro[1],
             "fecha_hora": registro[2]}
            for registro in bd.ejecutar_sql(obtener_sesion_cliente_sql)]
