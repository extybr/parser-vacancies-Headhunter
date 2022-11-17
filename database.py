import sqlite3
import os.path


class Database:
    db = '_vacancies.db'
    command_create = ('CREATE TABLE headhunter (company text, name text, from_salary text, '
                      'to_salary text, link text, types text, date text, schedule text, '
                      'counters_responses text, address text)')
    command_drop = "DROP TABLE headhunter"
    command_read = 'SELECT * FROM headhunter'

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
        if os.path.exists(self.db):
            self.command_database(self.command_drop)
            self.command_database(self.command_create)

    def initialize_database(self) -> None:
        """
        Создание базы данных и таблицы при ее отсутствии.
        :return: None
        """
        if not [i for i in os.listdir('.') if i == self.db]:
            print('База данных отсутствует и будет создана')
            self.command_database(self.command_create)

    def insert_database(self, company: str, name: str, from_salary: str, to_salary: str, link: str,
                        types: str, date: str, schedule: str, counters_responses: str,
                        address: str) -> None:
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
        command_insert = (f"INSERT INTO headhunter (company, name, from_salary, to_salary, link, "
                          f"types, date, schedule, counters_responses, address) "
                          f"VALUES ('{company}', '{name}', '{from_salary}', '{to_salary}', "
                          f"'{link}', '{types}', '{date}',' {schedule}', '{counters_responses}',"
                          f" '{address}')")
        self.command_database(command_insert)

    def read_database(self) -> str:
        """
        Передача данных с базы данных.
        :return: str
        """
        connect = sqlite3.connect(self.db, check_same_thread=False)
        cursor = connect.cursor()
        data = cursor.execute(self.command_read)
        for variable in data:
            yield (f'  {variable[0]}  '.center(107, '*') + f'\n\n🚮   Профессия: {variable[1]}\n😍'
                   f'   Зарплата: {variable[2]} - {variable[3]}\n⚜   Ссылка: {variable[4]}\n🐯   '
                   f'/{variable[5]}/   -🌼-   дата публикации: {variable[6]}   -🌻-   график '
                   f'работы: {variable[7]}\n🚦   Количество откликов для вакансии: '
                   f'{variable[8]}\n🚘   Адрес: {variable[9]}\n')
