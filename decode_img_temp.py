from base64 import decodebytes
from pathlib import Path
from tempfile import gettempdir
from hh_icon import icon as hh
from tv_icon import icon as tv


def decode_b64() -> tuple:
    """ Переменные окружения.
    Декодирование файла из base64.
    Сохранение иконки """
    pic_hh = 'hh.svg'
    pic_tv = 'trudvsem.png'
    try:
        path_hh_temp = Path(gettempdir()) / pic_hh
        path_tv_temp = Path(gettempdir()) / pic_tv
        if Path.exists(path_hh_temp) and Path.exists(path_tv_temp):
            return str(path_hh_temp), str(path_tv_temp)
        else:
            dec1 = decodebytes(hh.encode())
            dec2 = decodebytes(tv.encode())
            with open(path_hh_temp, 'wb') as file:
                file.write(dec1)
            with open(path_tv_temp, 'wb') as file:
                file.write(dec2)
            return str(path_hh_temp), str(path_tv_temp)
    except Exception:
        return 'favicon.ico', 'favicon.ico'
