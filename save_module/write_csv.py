from csv import writer


def save_to_csv(name: str, job: list) -> None:
    """ Создание csv файла """
    file = open(f'_{name}_.csv', mode='w', encoding='cp1251')
    csv_writer = writer(file)
    csv_writer.writerow(['компания', 'профессия', 'от', 'до', 'ссылка', 'тип',
                        'дата', 'график', 'счетчик', 'адрес'])
    csv_writer.writerows(job)
