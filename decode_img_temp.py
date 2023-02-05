from base64 import decodebytes
import os.path
from platform import platform
from favicon import icon


def decode_b64() -> str:
    """ Переменные окружения. Декодирование файла из base64. Сохранение иконки """
    name = 'favicon.ico'
    if platform().find('Windows') != -1:
        path_temp = os.environ.get('TEMP', 0)
        if path_temp == 0:
            path_temp = os.environ.get('TMP', 0)
        else:
            if path_temp == 0:
                return name
        dec = decodebytes(icon.encode())
        with open(os.path.join(path_temp, name), 'wb') as file:
            file.write(dec)
        return os.path.join(path_temp, name)
    else:
        return name
