import sqlite3
from datos.base_de_datos import BaseDeDatos
from datos.tablas import crear_tablas

conexion = sqlite3.connect('bid2win.db')

def listar_usuario_cliente(conexion):
    sql = "SELECT * FROM customer;"

    cursor = conexion.cursor()
    cursor.execute(sql)
    clientes = cursor.fetchall()

    for c in clientes:
        print(c)
        lista_clientes = list(c)
        print (lista_clientes)

print("lista clientes: ")
listar_usuario_cliente(conexion)

def listar_cotizaciones_proveedor(conexion):
    sql = "SELECT * FROM quote WHERE SUPPLIER = 'Hilton';"

    cursor = conexion.cursor()
    cursor.execute(sql)
    cotizaciones = cursor.fetchall()

    for c in cotizaciones:
        print(c)
        lista_cotizaciones = list(c)
        print (lista_cotizaciones)

print("lista cotizaciones: ")
listar_cotizaciones_proveedor(conexion)