import requests
import os


class BajarDes:
    """Esta clase es la encargada de crear los directorios y
    colocar ahi dentro las imagenes correspondientes"""

    def descarga(self, nombre, capitulo, lista):
        self.nombre = nombre
        self.capitulo = capitulo
        self.lista = lista
        contador = 1
        self.directorio = str(self.nombre) + "/" + str(self.capitulo) + "/"
        try:
            os.makedirs(self.directorio)
        except FileExistsError:
            print("El directorio ya existe")
        print(" ")
        for i in self.lista:
            nombre_local = self.directorio + str(contador).zfill(3) + ".jpg"
            imagen = requests.get(i).content
            with open(nombre_local, "wb") as handler:
                handler.write(imagen)
            print("Bajando imagen numero:", contador)
            contador = contador + 1
        print(" ")
