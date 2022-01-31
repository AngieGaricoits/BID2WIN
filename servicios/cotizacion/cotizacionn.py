from datos.modelos import cotizacion as modelo_cotizacion


def _existe_cotizacion(brand, style):
    cotizacion = modelo_cotizacion.obtener_cotizacion_por_marca_style(brand, style)
    return not len(cotizacion) == 0


def crear_cotizacion(team, supplier, brand, quantity_color, group_order, style, status, workfile, measures,
                     dead_line, comments):
    if not _existe_cotizacion(brand, style):
        modelo_cotizacion.crear_cotizacion(team, supplier, brand, quantity_color, group_order, style, status, workfile,
                                           measures, dead_line, comments)
    else:
        raise Exception('La cotizacion ya existe')


def modificar_cotizacion(id_quote, datos_cotizacion):
    modelo_cotizacion.modificar_cotizacion(id_quote, datos_cotizacion)


def obtener_cotizaciones():
    return modelo_cotizacion.obtener_cotizaciones()


def obtener_cotizacion(id_quote):
    cotizacion = modelo_cotizacion.obtener_cotizacion(id_quote)
    if len(cotizacion) == 0:
        raise Exception("La cotizacion no existe")
    return cotizacion[0]

def obtener_cotizaciones_proveedor(login_supplier):
    cotizaciones_supplier = modelo_cotizacion.obtener_cotizaciones_proveedor(login_supplier)
    if len(cotizaciones_supplier) == 0:
        raise Exception("No quote in process for this supplier")
    return cotizaciones_supplier

def borrar_cotizacion(id_quote):
    modelo_cotizacion.borrar_cotizacion(id_quote)


