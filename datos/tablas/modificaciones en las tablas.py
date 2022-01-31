import sqlite3
from sqlite3 import Error
def conectar():
    try:
        conexion = sqlite3.connect('bid2win.db')
        conexion.execute('PRAGMA foreing_keys = ON')
        print('Conexion establablecida')
        return conexion
    except Error:
        print(Error)

def modificarTabla(conexion):
    #conexion.execute('ALTER TABLE status RENAME COLUMN STATUS TO STATUS_ID')
    conexion.commit()

def modificarTabla(conexion):
    conexion.execute('ALTER TABLE status ADD COLUMN status text')
    conexion.commit()

con = conectar()
modificarTabla(con)
conjuntos(con)