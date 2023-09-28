from httpx import get


def recursion_hh(result: list, rus: dict) -> list:
    """ Рекурсивный проход по структуре и возврат отсортированного списка """
    out = f"{rus.get('name', '0')}: {rus.get('id', '0')}"
    result.append(out)
    for area in rus.get('areas', '0'):
        if isinstance(area, dict):
            recursion_hh(result, area)
    return sorted(result)


def get_hh_region() -> list:
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
        results = get(url, headers=headers).json()
        return recursion_hh([], results[0])
    except OSError as error:
        # print(f'Статус: проблемы с доступом в интернет\n{error}')
        from info_module.area import area_hh
        return area_hh
    except Exception:
        pass


def get_tv_region() -> list:
    """ Получение списка регионов """
    try:
        url = 'https://opendata.trudvsem.ru/json/regions.json'
        headers = {
            'Host': 'opendata.trudvsem.ru',
            'User-Agent': 'Mozilla/5.0',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'
        }
        results = get(url, headers=headers).json()
        result = []
        for area in results.get('regions', '0'):
            out = f"{area.get('name', '0')}: {area.get('code', '0')[:2]}"
            result.append(out)
        return sorted(result)
    except OSError as error:
        # print(f'Статус: проблемы с доступом в интернет\n{error}')
        from info_module.area import area_trudvsem
        return area_trudvsem
    except Exception:
        pass
