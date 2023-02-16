from requests import get


def recursion(result, rus) -> list:
    out = f"{rus.get('name', '0')}: {rus.get('id', '0')}"
    result.append(out)
    for area in rus.get('areas', '0'):
        if isinstance(area, dict):
            recursion(result, area)
    return sorted(result)


def get_region() -> list:
    """ Получение списка регионов """
    try:
        url = 'https://api.hh.ru/areas'
        headers = {
            'Host': 'api.hh.ru',
            'User-Agent': 'Mozilla/5.0',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'
        }
        results = get(url, headers).json()
        return recursion([], results[0])
    except OSError as error:
        print(f'Статус: проблемы с доступом в интернет\n{error}')
