import re

# Patron de busqueda
patron = re.compile(r"https://lectortmo.com/viewer/[A-Za-z0-9-_/]{5,}/")


class Validare:
    """Verifica que el link igresado no este
    vacio y sea el correcto."""

    def validar_link(self, linki=""):
        # Verifica que el sea el de la pagina.
        veri = linki.startswith("https://lectortmo.com/viewer/")
        if not linki:
            veri = "Campo vacio"
            return veri
        elif not veri:
            veri = "Link invalido"
            return veri
        else:
            busqueda = patron.match(linki)
            if not busqueda:
                linki = "Link invalido"
                return linki
            else:
                if "paginated" in linki:
                    # Reemplaza paginated por cascade.
                    linki = linki.replace("paginated", "cascade")
                    return linki
                else:
                    return linki
