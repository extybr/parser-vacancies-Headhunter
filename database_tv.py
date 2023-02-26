import sqlite3
import os.path


class DatabaseTrudvsem:
    db = "_vacancies.db"
    command_create = ('CREATE TABLE trudvsem (company text, name text, '
                      'from_salary text, to_salary text, link text, '
                      'date text, schedule text, address text)')
    command_drop = "DROP TABLE  IF EXISTS trudvsem"
    command_read = "SELECT * FROM trudvsem"

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
            # print('База данных отсутствует и будет создана')
            self.command_database(self.command_create)

    def insert_database(self, company: str, name: str, from_salary: str,
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

    def read_database(self) -> str:
        """
        Передача данных с базы данных.
        :return: str
        """
        try:
            connect = sqlite3.connect(self.db, check_same_thread=False)
            cursor = connect.cursor()
            data = cursor.execute(self.command_read)
            for variable in data:
                yield (f'  {variable[0]}  '.center(107, '*') + f'\n\n🚮   '
                       f'Профессия: {variable[1]}\n😍    Зарплата: {variable[2]} -'
                       f' {variable[3]}\n⚜   Ссылка: {variable[4]}\n🐯   '
                       f'дата публикации: {variable[5]}   -🌻-   график работы: '
                       f'{variable[6]}\n🚘   Адрес: {variable[7]}\n')
        except Exception as e:
            if str(e).find('no such table') != -1:
                yield '\n\n' + '  Не было сохранений в базу  '.center(107, '*')
            pass


dt = DatabaseTrudvsem()
