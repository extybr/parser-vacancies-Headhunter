from base64 import decodebytes
from pathlib import Path
from tempfile import gettempdir
from favicon import icon


def decode_b64() -> str:
    """ Переменные окружения.
    Декодирование файла из base64.
    Сохранение иконки """
    name = 'favicon.ico'
    try:
        path_temp = str(Path(gettempdir()) / name)
        dec = decodebytes(icon.encode())
        with open(path_temp, 'wb') as file:
            file.write(dec)
        return path_temp
    except Exception:
        return name
