Script para descargar mangas de TuMangaOnline (https://lectortmo.com/)

La idea fue modificar un viejo script mio que tenia echo en bash y pasarlo a
python. Por el momento el script esta echo para correr sobre GNU/Linux pero con
algunos retoques se puede correr sin problemas en otros OS.
Al principo la idea original era hacer algo y darle una grafica con tkinter
pero me gusto mas la idea de la terminal y utilizar parametros como todo buen
programa de consola en GNU/Linux.

Dependencias: argparse, re, sb4, requests, os, sqlite3.

Paara ejecutarlo desde un terminal: python3.7 main.py
Para acceder a la base de datos: python3.7 main.py -b
Para ver la version del script: python3.7 main.py -v
Para la ayuda general: python3.7 main.py -h
El man del script no esta terminado y pienso enpaquetarlo
un .deb para facilitar su utilizacion.

Links de prueba:
https://lectortmo.com/viewer/5af141696b8b6/cascade
https://lectortmo.com/viewer/5ecf4552b627e/cascade
https://lectortmo.com/viewer/5af1c42d8a154/paginated
https://lectortmo.com/viewer/5af1eb4bc91d9/paginated
