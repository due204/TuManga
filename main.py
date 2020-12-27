from vista import MiVista
from validar import Validare
from macheo import MacheoD
from descargar import BajarDes
from abmc import Abmc
import argparse


class Controlador:
    def __init__(self):
        # Instacias
        self.vist = MiVista()
        self.mach = MacheoD()
        self.bajar = BajarDes()
        self.vali = Validare()
        self.base = Abmc()
        self.parametros = argparse.ArgumentParser()
        # Creo los argumentos
        self.parametros.add_argument(
            "-v", "--version", help="Version del script", action="store_true"
        )
        self.parametros.add_argument(
            "-b", "--base", help="Base de datos", action="store_true"
        )
        self.argumento = self.parametros.parse_args()
        # Proceso los argumentos
        if self.argumento.version:
            print(self.vist.version())
            exit()
        elif self.argumento.base:
            print(self.vist.base())
            read_base = input("? ")
            if read_base == "1":
                self.base.consulta()
            elif read_base == "2":
                self.base.consulta()
                ides = input("Ingrese el Id a modificar: ")
                clav = input("1 - Nombre \n2 - Capitulo \n3 - Estado \n? ")
                valo = input("Ingrese el nuevo valor: ")
                self.base.modificar(ides, clav, valo)
                print("Base modificada")
            elif read_base == "3":
                self.base.consulta()
                read_base2 = input("Ingrese el Id a eliminar: ")
                self.base.baja(read_base2)
            else:
                exit()
        else:
            self.baja = self.vist.entrada1()
            self.val = self.vali.validar_link(self.baja)
            if self.val == "Campo vacio":
                print(self.val)
                exit()
            elif self.val == "Link invalido":
                print(self.val)
                exit()
            else:
                self.pagina = self.mach.link(self.val)
                self.nombre = self.mach.titulo(self.pagina)
                self.capitu = self.mach.capitulo(self.pagina)
                self.fansuu = self.mach.fansub(self.pagina)
                self.listaa = self.mach.lista(self.pagina)
                self.vist.entrada2(
                    self.nombre,
                    self.capitu,
                    self.fansuu,
                    self.listaa,
                )
                continuar = input("? ")
                if continuar == "s" or continuar == "S":
                    self.bajar.descarga(self.nombre, self.capitu, self.listaa)
                    self.base.alta(self.nombre, self.capitu, self.fansuu)
                else:
                    exit()


if __name__ == "__main__":
    miapp = Controlador()
