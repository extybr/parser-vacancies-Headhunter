from base64 import decodebytes
from pathlib import Path
from tempfile import gettempdir
from hh_icon import icon as hh
from tv_icon import icon as tv


def decode_b64() -> tuple:
    """ Переменные окружения.
    Декодирование файла из base64.
    Сохранение иконки """
    pic1 = 'hh.svg'
    pic2 = 'trudvsem.png'
    try:
        path1_temp = str(Path(gettempdir()) / pic1)
        path2_temp = str(Path(gettempdir()) / pic2)
        dec1 = decodebytes(hh.encode())
        dec2 = decodebytes(tv.encode())
        with open(path1_temp, 'wb') as file:
            file.write(dec1)
        with open(path2_temp, 'wb') as file:
            file.write(dec2)
        return path1_temp, path2_temp
    except Exception:
        return pic1, pic1
