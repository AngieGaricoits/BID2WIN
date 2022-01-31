from datos.base_de_datos import BaseDeDatos


# funcion para crear cotizacion
def crear_cotizacion(team, supplier, brand, quantity_color, group_order, style, status, workfile, measures,
                     dead_line, comments):
    crear_cotizacion_sql = f"""
        INSERT INTO QUOTE(TEAM, SUPPLIER, BRAND, QUANTITY_COLOR, GROUP_ORDER, STYLE, STATUS, WORKFILE, MEASURES, DEAD_LINE, COMMENTS)
        VALUES ('{team}', '{supplier}', '{brand}', '{quantity_color}', '{group_order}', '{style}', '{status}', '{workfile}', '{measures}', '{dead_line}', '{comments}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_cotizacion_sql)


# funcion modificar cotizacion
def modificar_cotizacion(id_quote, datos_cotizacion):
    modificar_cotizacion_sql = f"""
        UPDATE QUOTE
        SET TEAM= '{datos_cotizacion["team"]}', 
        SUPPLIER= '{datos_cotizacion["supplier"]}', 
        BRAND= '{datos_cotizacion["brand"]}', 
        QUANTITY_COLOR= '{datos_cotizacion["quantity_color"]}', 
        GROUP_ORDER= '{datos_cotizacion["group_order"]}', 
        STYLE= '{datos_cotizacion["style"]}', 
        STATUS= '{datos_cotizacion["status"]}', 
        WORKFILE= '{datos_cotizacion["workfile"]}', 
        MEASURES= '{datos_cotizacion["measures"]}', 
        DEAD_LINE= '{datos_cotizacion["dead_line"]}', 
        COMMENTS= '{datos_cotizacion["comments"]}'          
        WHERE ID_QUOTE='{id_quote}'
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(modificar_cotizacion_sql)


# funcion para listar todos las cotizaciones
def obtener_cotizaciones():
    obtener_cotizaciones_sql = f"""
        SELECT id_quote, team, supplier, brand, quantity_color, group_order, style, status, workfile, measures, dead_line, comments
        FROM QUOTE
    """
    bd = BaseDeDatos()
    return [{"id_quote": registro[0],
             "team": registro[1],
             "supplier": registro[2],
             "brand": registro[3],
             "quantity_color": registro[4],
             "group_order": registro[5],
             "style": registro[6],
             "status": registro[7],
             "workfile": registro[8],
             "measures": registro[9],
             "dead_line": registro[10],
             "comments": registro[11],
             } for registro in bd.ejecutar_sql(obtener_cotizaciones_sql)]


# funcion obtener una cotizacion por id
def obtener_cotizacion(id_quote):
    obtener_cotizacion_sql = f"""
        SELECT id_quote, team, supplier, brand, quantity_color, group_order, style, status, workfile, measures, dead_line, comments
        FROM QUOTE
        WHERE ID_QUOTE = {id_quote}
    """
    bd = BaseDeDatos()
    return [{"id_quote": registro[0],
             "team": registro[1],
             "supplier": registro[2],
             "brand": registro[3],
             "quantity_color": registro[4],
             "group_order": registro[5],
             "style": registro[6],
             "status": registro[7],
             "workfile": registro[8],
             "measures": registro[9],
             "dead_line": registro[10],
             "comments": registro[11]
             } for registro in bd.ejecutar_sql(obtener_cotizacion_sql)]

def obtener_cotizacion_por_marca_style(brand, style):
    obtener_cotizacion_por_marca_style_sql = f"""
            SELECT id_quote, team, supplier, brand, quantity_color, group_order, style, status, workfile, measures, dead_line, comments
            FROM QUOTE u
            WHERE BRAND='{brand}' and GROUP_ORDER='{style}' 
        """
    bd = BaseDeDatos()
    return [{"Brand": registro[0],
             "Style": registro[1]
             } for registro in bd.ejecutar_sql(obtener_cotizacion_por_marca_style_sql)]

def obtener_cotizaciones_proveedor(login_supplier):
    obtener_cotizaciones_proveedor_sql = f"""
                SELECT quote.brand, quote.group_order, quote.style, quote.quantity_color, quote.status, 
                quote.dead_line, quote.team, comments, supplier.login_supplier
                FROM QUOTE 
                     INNER JOIN SUPPLIER ON QUOTE.SUPPLIER = SUPPLIER.LOGIN_SUPPLIER
                WHERE supplier.login_supplier = '{login_supplier}'
                COLLATE NOCASE
            """
    bd = BaseDeDatos()
    return [{"brand": registro[0],
             "group_order": registro[1],
             "style": registro[2],
             "quantity_color": registro[3],
             "status": registro[4],
             "dead_line": registro[5],
             "team": registro[6],
             "comments": registro[7],
             } for registro in bd.ejecutar_sql(obtener_cotizaciones_proveedor_sql)]


# funcion borrar cotizacion
def borrar_cotizacion(id_quote):
    obtener_cotizacion_sql = f"""
        DELETE
        FROM QUOTE
        WHERE ID_QUOTE = {id_quote}
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(obtener_cotizacion_sql)
