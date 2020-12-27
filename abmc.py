import sqlite3
import os


class Abmc:
    def crear_db(self):
        # Crear la base de datos.
        tabla = "CREATE TABLE mi_lista ('id' INTEGER PRIMARY KEY, 'nombre' \
             VARCHAR(50), 'capitulo' INTEGER, 'sub' VARCHAR(50))"
        coneccion = sqlite3.connect("Base.db")
        cursor = coneccion.cursor()
        # crear la tabla en la base de datos.
        cursor.execute(tabla)
        coneccion.close()

    def alta(self, nom, cap, fan):
        """nom = Nombre (str), cap = capitulo (int)
        fan = Sub (str)
        Insertar valores en la tabla"""
        # os.path.isfile verifica que exista la base
        if not os.path.isfile("Base.db"):
            print("La base de datos no extiste.")
            print(("Se procedera a crear una."))
            # Si no exixste Base.db llamo a crear_db
            self.crear_db()
        # Sumamos uno al ultimo ID de la tabla
        ide = self.ultima()
        ide = int(ide) + 1
        sql = "INSERT INTO mi_lista (id, nombre, capitulo, sub) \
             VALUES(?,?,?,?)"
        coneccion = sqlite3.connect("Base.db")
        cursor = coneccion.cursor()
        try:
            cursor.execute(
                sql,
                (
                    ide,
                    nom,
                    cap,
                    fan,
                ),
            )
        except sqlite3.OperationalError:
            print("No hay una tabla en la base de datos")
            print("Se creara la correspondiente tabla")
            # Si no existe la tabla la creo
            self.crear_db()
        coneccion.commit()
        coneccion.close()

    def baja(self, eli):
        """eli = id del registro a eliminar
        Eliminar registro basado en el id"""
        sql = "DELETE FROM mi_lista WHERE id = ?;"
        coneccion = sqlite3.connect("Base.db")
        cursor = coneccion.cursor()
        cursor.execute(sql, (eli,))
        coneccion.commit()
        coneccion.close()
        print("Registro " + str(eli) + " eliminado")

    def modificar(self, ide, clave, valor):
        """ide = id del registro,
        clave = nombre, capitulo o sub
        valor = Nuevo valor del campo"""
        if clave == "1":
            clave = "nombre"
        elif clave == "2":
            clave = "capitulo"
        elif clave == "3":
            clave = "sub"
        else:
            print("Entrada incorecta.")
            exit()
        sql = "UPDATE mi_lista SET " + clave + " = ? where id = ?"
        coneccion = sqlite3.connect("Base.db")
        cursor = coneccion.cursor()
        cursor.execute(
            sql,
            (valor, ide),
        )
        coneccion.commit()
        coneccion.close()

    def consulta(self):
        """Ver todos los valores de la base de datos"""
        try:
            sql = "SELECT * FROM mi_lista"
            coneccion = sqlite3.connect("Base.db")
            cursor = coneccion.cursor()
            cursor.execute(sql)
            tablas = cursor.fetchall()
            for i in tablas:
                print(i[0], i[1], i[2], i[3])
        except sqlite3.OperationalError:
            print("No hay una base de datos o una tabla creada.")
            print("Se creara una base de datos con su tabla.")
            self.crear_db()
            coneccion.commit()
            coneccion.close()
            print(" ")

    def ultima(self):
        """Identifica cual es el ultimo ID ingresado"""
        sql = "SELECT * FROM mi_lista ORDER BY id DESC LIMIT 1; "
        coneccion = sqlite3.connect("Base.db")
        cursor = coneccion.cursor()
        cursor.execute(sql)
        ultimo = cursor.fetchone()
        coneccion.commit()
        coneccion.close()
        try:
            return ultimo[0]
        except TypeError:
            return "0"
