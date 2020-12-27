import re
import requests
from bs4 import BeautifulSoup


class MacheoD:
    """Esta clase se encarga de bajar y procesar todos los datos los
    de la pagina web como el titulo, capitulo, imagenes y demas"""

    def link(self, linki):
        """ Baja los datos de la pagina web."""
        for i in range(0, 2):
            # Lo ejecuto tres veces para asegurarme que
            #  descarge los datos corretamente.
            headers = {"User-Agent": "Mozilla/78.5"}
            url = linki
            pagina = requests.get(url, headers=headers)
            soup = BeautifulSoup(pagina.text, "html.parser")
        return soup

    def titulo(self, titul):
        """Busca el titulo de la pagina entre
        todos los datos bajados."""
        titulos = titul.title.string.split("-")
        nombre = titulos[0].strip()
        return nombre

    def capitulo(self, capit):
        """Busca el capitulo de la pagina entre
        todos los datos bajados."""
        titulos = capit.title.string.split("-")
        capitulo = titulos[2].replace("Capítulo", "").strip()
        return capitulo

    def fansub(self, fansu):
        """Busca el fansub de la pagina entre
        todos los datos bajados."""
        titulos = fansu.title.string.split("-")
        fansub = titulos[3].strip()
        return fansub

    def lista(self, listi):
        """Busca todas las imagenes de la pagina y nos devuelve
        Una lista con todas ellas."""
        imaenes = listi.find_all("img")
        imagenes = re.findall(
            r"https://img1.tucomiconline.com/uploads/[A-Za-z0-9-_/]{5,}.[a-z]{2,4}",
            str(imaenes),
        )
        return imagenes
