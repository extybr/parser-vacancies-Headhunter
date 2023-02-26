import csv


def save_to_csv(job):
    file = open('_vacancies.csv', mode='w', encoding='cp1251')
    writer = csv.writer(file)
    writer.writerow(['компания', 'профессия', 'от', 'до', 'ссылка', 'тип',
                     'дата', 'график', 'счетчик', 'адрес'])
    writer.writerows(job)
