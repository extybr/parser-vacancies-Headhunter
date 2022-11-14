import sys
import requests
import sqlite3
import os.path
from PyQt5 import QtWidgets
from job_gui import UiMainWindow


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


class MyWin(QtWidgets.QMainWindow, Database):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = UiMainWindow()
        self.ui.setup_ui(self)
        self.text_vacancies = self.ui.lineEdit.displayText()
        self.ui.pushButton.clicked.connect(self.extract_jobs)
        self.ui.pushButton_2.clicked.connect(self.read_jobs)

    def read_jobs(self) -> None:
        """
        Чтение базы данных и вывод в поле программы.
        :return: None
        """
        self.ui.textBrowser.clear()
        if os.path.exists(self.db):
            output = self.read_database()
            for count, line in enumerate(output):
                self.ui.textBrowser.append(f'{line}')
                self.ui.lcdNumber.display(count + 1)
            self.ui.textBrowser.scrollToAnchor("scroll")
        else:
            self.ui.textBrowser.append('\n\n' + '  База Данных отсутствует  '.center(107, '*'))

    def extract_jobs(self) -> None:
        """
        Парсит вакансии с api.hh.ru,
        выводит ответ в поле вывода,
        пишет в лог-файл.
        :return: None
        """
        self.ui.textBrowser.clear()
        period = self.ui.lineEdit_5.displayText()
        professional_role = ''
        if len(self.ui.lineEdit_3.displayText().strip()) > 0:
            professional_role = '&professional_role=' + str(self.ui.lineEdit_3.displayText())
        text_profession = '&text=' + self.ui.lineEdit.displayText()
        page = self.ui.spinBox.value()
        if page == 0:
            self.text_vacancies = self.ui.lineEdit.displayText()
        if self.text_vacancies != self.ui.lineEdit.displayText():
            page = 0
            self.text_vacancies = self.ui.lineEdit.displayText()
        count = self.ui.lineEdit_4.displayText()
        area = self.ui.lineEdit_2.displayText()
        publication_time = ''
        industry = ''
        if len(self.ui.lineEdit_6.displayText().strip()) > 0:
            industry = '&industry=' + str(self.ui.lineEdit_6.displayText())
        if self.ui.checkbox_2.isChecked():
            publication_time = 'order_by=publication_time&'
        # '&employer_id=3083859' идентификатор компании Сталь
        url = (f'https://api.hh.ru/vacancies?clusters=true&st=searchVacancy&enable_snippets=true&'
               f'{publication_time}period={period}&only_with_salary=false{professional_role}'
               f'{text_profession}&page={page}&per_page={count}&area={area}{industry}'
               f'&responses_count_enabled=true')

        if self.extract_jobs:
            page = int(page) + 1
            self.ui.spinBox.setValue(page)

        headers = {
            'Host': 'api.hh.ru',
            'User-Agent': 'Mozilla',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'
        }

        if self.ui.checkbox_4.isChecked():
            self.drop_database()
            self.initialize_database()

        try:
            print(f'Headhunter: парсинг страницы')
            result = requests.get(url, headers)
            results = result.json()
            count_results = results.get('found')
            print('Найдено результатов:', count_results)
            print('\n' + '*' * 150 + '\n')
            self.ui.lcdNumber.display(count_results)
            if self.ui.checkbox_3.isChecked():
                with open('_vacancies.txt', 'w', encoding='utf-8') as text:
                    text.write('Найдено результатов:' + str(count_results) + '\n\n')
            items = results.get('items', {})
            for index in items:
                company = index['employer']['name']
                name = index['name']
                link = index["alternate_url"]
                types = index['type']['name']
                counters_responses = index['counters']['responses']
                schedule = index['schedule']['name']
                date = index['published_at'][:10]
                address = index['area']['name']
                if index['address']:
                    address = index['address']['raw']
                # logo = index['employer']['logo_urls']['90']
                salary = index['salary']
                information = ''
                if self.ui.radioButton.isChecked():
                    count_vacancies = ''
                    if self.ui.checkbox.isChecked():
                        company_id = index['employer']['id']

                        def get_count_vacancies(company_number: str, header: dict) -> str:
                            url_id = f'https://api.hh.ru/employers/{company_number}'
                            counter = ('\n🚷   Всего количество вакансий у компании: ' + str(
                                requests.get(url_id, header).json().get('open_vacancies', 0)
                            ) + '\n')
                            return counter

                        count_vacancies = get_count_vacancies(company_id, headers)
                    requirement = str(index['snippet']['requirement']).replace(
                        '<highlighttext>', '*')
                    requirement = str(requirement).replace('</highlighttext>', '*')
                    responsibility = str(index['snippet']['requirement']).replace(
                        '<highlighttext>', '*')
                    responsibility = str(responsibility).replace('</highlighttext>', '*')
                    information = (f'\n🐵   Отрывок из требований по вакансии: {requirement}\n🐼   '
                                   f'Отрывок из обязанностей по вакансии: {responsibility}'
                                   f'\n' + count_vacancies)
                if salary:
                    from_salary = salary['from']
                    to_salary = salary['to']
                    if not isinstance(from_salary, int):
                        from_salary = '😜'
                    if not isinstance(to_salary, int):
                        to_salary = '🚀'
                    output = (f'  {company}  '.center(107, '*') + f'\n\n🚮   Профессия: {name}\n😍   '
                              f'Зарплата: {from_salary} - {to_salary}\n⚜   Ссылка: {link}\n🐯   '
                              f'/{types}/   -🌼-   дата публикации: {date}   -🌻-   график работы: '
                              f'{schedule.lower()}\n🚦   Количество откликов для вакансии: '
                              f'{counters_responses}\n🚘   Адрес: {address}\n{information}')
                    print(output)
                    self.ui.textBrowser.append(output)
                    if self.ui.checkbox_3.isChecked():
                        text = open('_vacancies.txt', 'a', encoding='utf-8')
                        text.write(output.center(120, '*') + '\n')
                    if self.ui.checkbox_4.isChecked():
                        self.insert_database(company, name, str(from_salary), str(to_salary),
                                             link, types, date, schedule.lower(),
                                             counters_responses, address)
                else:
                    output = (f'  {company}  '.center(107, '*') + f'\n\n🚮   Профессия: {name}\n😍'
                              f'   Зарплата: не указана\n⚜   Ссылка: {link}\n🐯   /{types}/'
                              f'   -🌼-   дата публикации: {date}   -🌻-   график работы: '
                              f'{schedule.lower()}\n🚦   Количество откликов для вакансии: '
                              f'{counters_responses}\n🚘   Адрес: {address}\n{information}')
                    print(output)
                    self.ui.textBrowser.append(output)
                    if self.ui.checkbox_3.isChecked():
                        text = open('_vacancies.txt', 'a', encoding='utf-8')
                        text.write(output.center(120, '*') + '\n')
                    if self.ui.checkbox_4.isChecked():
                        self.insert_database(company, name, 'не указана', 'не указана', link,
                                             types, date, schedule.lower(), counters_responses,
                                             address)
                # self.ui.textBrowser.append("<a name=\"scroll\" href=\"\">۩</a>")
            if self.ui.checkbox_3.isChecked():
                text.close()
            self.ui.textBrowser.scrollToAnchor("scroll")
            if self.ui.checkbox_5.isChecked():
                from PyQt5 import QtGui
                pdf = QtGui.QPdfWriter('_vacancies.pdf')
                self.ui.textBrowser.print(pdf)
        except OSError as error:
            if str(error).find('HTTPSConnection') != -1:
                print(f'Статус: проблемы с доступом в интернет\n{error}')
                self.ui.textBrowser.append('\n\n\n' + '  Статус: проблемы с доступом в интернет  '
                                           .center(142, '-'))
            else:
                print(f'Статус: не хватает прав доступа\n{error}')
                self.ui.textBrowser.append(
                    '\n\n\n' + '  Статус: не хватает прав доступа создания лог файла (базы '
                               'данных)  '.center(130, '-'))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
