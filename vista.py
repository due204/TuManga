class MiVista:
    """Vistas y menus del script """

    def entrada1(self):
        self.entrada = input("Ingrese el link: ")
        return self.entrada

    def version(self):
        print("Version 0.1 del script")
        print("Trabajo práctico integrador final")
        print("Mail: due204@gmail.com")

    def base(self):
        print("1 - Ver base de datos")
        print("2 - Editar base de datos")
        print("3 - Eliminar registro de base de datos")

    def entrada2(self, titu, capi, fans, lisu):
        self.titu = titu
        self.capi = capi
        self.fans = fans
        self.lisu = lisu
        print(" ")
        print("Nombre:", self.titu)
        print("capitulo:", self.capi)
        print("Fansub:", self.fans)
        print("Imagenes a bajar:", len(self.lisu))
        print(" ")
        print("Desea continuar: S/n")
