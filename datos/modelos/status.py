from datos.base_de_datos import BaseDeDatos

# funcion para crear status
def crear_status(status_id, status, quote_id, date):
    crear_status_sql = f"""
        INSERT INTO STATUS(STATUS_ID, STATUS, QUOTE_ID, DATE)
        VALUES ('{status_id}', '{status}', '{quote_id}', '{date}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_status_sql)