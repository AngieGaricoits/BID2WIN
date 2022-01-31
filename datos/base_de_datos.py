import sqlite3


class BaseDeDatos:
    url_base_de_datos = 'datos/tablas/bid2win.db'

    def crear_conexion(self):
        try:
            self.conexion = sqlite3.connect(BaseDeDatos.url_base_de_datos)
        except Exception as e:
            print(e)

    def cerrar_conexion(self):
        self.conexion.close()
        self.conexion = None

    def ejecutar_sql(self, sql, retornar_id_creado=False):
        self.crear_conexion()
        cur = self.conexion.cursor()
        cur.execute(sql)

        filas = cur.fetchall()

        if retornar_id_creado:
            filas = cur.lastrowid

        self.conexion.commit()
        self.cerrar_conexion()

        return filas

