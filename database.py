import sqlite3
from pathlib import Path


class Database:
    def __init__(self, name):
        self.name = name
        self.db = '_hh-trudvsem_.db'
        if name == 'hh':
            self.command_create = (
                'CREATE TABLE headhunter (company text, name text, '
                'from_salary text, to_salary text, link text, types text,'
                ' date text, schedule text, counters_responses text, '
                'address text)'
            )
            self.command_drop = "DROP TABLE IF EXISTS headhunter"
            self.command_read = 'SELECT * FROM headhunter'
        else:
            self.command_create = (
                'CREATE TABLE trudvsem (company text, name text, '
                'from_salary text, to_salary text, link text, date text, '
                'schedule text, address text)'
            )
            self.command_drop = "DROP TABLE IF EXISTS trudvsem"
            self.command_read = "SELECT * FROM trudvsem"

    def command_database(self, command_sql: str) -> None:
        """
        Подключение к базе данных и выполнение переданной команды.
        :param command_sql: str
        :return: None
        """
        connect = sqlite3.connect(self.db, check_same_thread=False)
        cursor = connect.cursor()
        cursor.execute(command_sql)
        connect.commit()
        connect.close()

    def drop_database(self) -> None:
        """
        Удаление таблицы с базы данных и создание новой таблицы.
        :return: None
        """
        if Path.exists(Path(self.db)):
            try:
                self.command_database(self.command_drop)
            except Exception as e:
                print(e)
            self.command_database(self.command_create)

    def initialize_database(self) -> None:
        """
        Создание базы данных и таблицы при ее отсутствии.
        :return: None
        """
        if not Path.exists(Path(self.db)):
            # print('База данных отсутствует и будет создана')
            self.command_database(self.command_create)

    def insert_hh(self, company: str, name: str, from_salary: str,
                  to_salary: str, link: str, types: str, date: str,
                  schedule: str, counters_responses: str, address: str):
        """
        Запись данных в таблицу базу данных.
        :param company: str
        :param name: str
        :param from_salary: str
        :param to_salary: str
        :param link: str
        :param types: str
        :param date: str
        :param schedule: str
        :param counters_responses: str
        :param address: str
        :return: None
        """
        command_insert = (f"INSERT INTO headhunter (company, name, from_salary,"
                          f" to_salary, link, types, date, schedule, "
                          f"counters_responses, address) VALUES ('{company}',"
                          f" '{name}', '{from_salary}', '{to_salary}', "
                          f"'{link}', '{types}', '{date}',' {schedule}', "
                          f"'{counters_responses}', '{address}')")
        self.command_database(command_insert)

    def insert_trudvsem(self, company: str, name: str, from_salary: str,
                        to_salary: str, link: str, date, schedule: str,
                        address: str) -> None:
        """
        Запись данных в таблицу базу данных.
        :param company: str
        :param name: str
        :param from_salary: str
        :param to_salary: str
        :param link: str
        :param date: text
        :param schedule: str
        :param address: str
        :return: None
        """
        command_insert = (f"INSERT INTO trudvsem (company, name, from_salary, "
                          f"to_salary, link, date, schedule, address) "
                          f"VALUES ('{company}', '{name}', '{from_salary}', "
                          f"'{to_salary}', '{link}', '{date}',' {schedule}', "
                          f"'{address}')")
        self.command_database(command_insert)

    def read_db(self) -> str:
        """
        Передача данных с базы данных.
        :return: str
        """
        try:
            connect = sqlite3.connect(self.db, check_same_thread=False)
            cursor = connect.cursor()
            data = cursor.execute(self.command_read)
            for variable in data:
                if self.name == 'hh':
                    yield (f'  {variable[0]}  '.center(107, '*') + f'\n\n🚮   '
                           f'Профессия: {variable[1]}\n😍   Зарплата: '
                           f'{variable[2]} - {variable[3]}\n⚜   Ссылка: '
                           f'{variable[4]}\n🐯   /{variable[5]}/   -🌼-   дата '
                           f'публикации: {variable[6]}   -🌻-   график работы: '
                           f'{variable[7]}\n🚦   Количество откликов для '
                           f'вакансии: {variable[8]}\n🚘   Адрес: '
                           f'{variable[9]}\n')
                else:
                    yield (f'  {variable[0]}  '.center(107, '*') + f'\n\n🚮   '
                           f'Профессия: {variable[1]}\n😍    Зарплата: '
                           f'{variable[2]} - {variable[3]}\n⚜   Ссылка: '
                           f'{variable[4]}\n🐯   дата публикации: {variable[5]}'
                           f'   -🌻-   график работы: {variable[6]}\n🚘   '
                           f'Адрес: {variable[7]}\n')
        except Exception as e:
            if str(e).find('no such table') != -1:
                yield '\n\n' + '  Не было сохранений в базу  '.center(107, '*')
            pass
