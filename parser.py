from requests import get
import os.path
from database import Database
from PyQt5 import QtWidgets
from gui import UiMainWindow
from write_csv import save_to_csv
from write_xls import save_to_xls
from datetime import date as dd
from time import time


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = UiMainWindow()
        self.ui.setup_ui(self)
        self.ui.pushButton.clicked.connect(self.extract_hh)
        self.ui.pushButton_2.clicked.connect(self.read_hh)
        self.ui.pushButton_3.clicked.connect(self.extract_trudvsem)
        self.ui.pushButton_4.clicked.connect(self.read_trudvsem)
        self.ui.pushButton_5.clicked.connect(self.get_areas_id)
        self.text_vacancies = self.ui.lineEdit.displayText()
        self.tv_vacancies = self.ui.lineEdit_20.displayText()
        self.text_period = self.ui.lineEdit_5.displayText()
        self.tv_period = self.ui.lineEdit_23.displayText()
        self.text_professional_role = self.ui.lineEdit_3.displayText()
        self.text_area = self.ui.lineEdit_2.displayText()
        self.tv_area = self.ui.lineEdit_21.displayText()
        self.text_industry = self.ui.lineEdit_6.displayText()
        self.text_page_count = self.ui.lineEdit_4.displayText()
        self.tv_page_count = self.ui.lineEdit_22.displayText()
        self.checkbox_2_time = self.ui.checkbox_2.checkState()
        self.checkbox_6_schedule = self.ui.checkbox_6.checkState()
        self.checkbox_7_schedule = self.ui.checkbox_7.checkState()
        self.checkbox_8_schedule = self.ui.checkbox_8.checkState()
        self.checkbox_9_schedule = self.ui.checkbox_9.checkState()
        self.checkbox_10_schedule = self.ui.checkbox_10.checkState()

    def set_state(self):
        """ Для запоминания состояний """
        self.text_vacancies = self.ui.lineEdit.displayText()
        self.text_period = self.ui.lineEdit_5.displayText()
        self.text_professional_role = self.ui.lineEdit_3.displayText()
        self.text_area = self.ui.lineEdit_2.displayText()
        self.text_industry = self.ui.lineEdit_6.displayText()
        self.text_page_count = self.ui.lineEdit_4.displayText()
        self.checkbox_2_time = self.ui.checkbox_2.checkState()
        self.checkbox_6_schedule = self.ui.checkbox_6.checkState()
        self.checkbox_7_schedule = self.ui.checkbox_7.checkState()
        self.checkbox_8_schedule = self.ui.checkbox_8.checkState()
        self.checkbox_9_schedule = self.ui.checkbox_9.checkState()
        self.checkbox_10_schedule = self.ui.checkbox_10.checkState()
        self.tv_vacancies = self.ui.lineEdit_20.displayText()
        self.tv_period = self.ui.lineEdit_23.displayText()
        self.tv_area = self.ui.lineEdit_21.displayText()
        self.tv_page_count = self.ui.lineEdit_22.displayText()

    def get_areas_id(self) -> None:
        """
        Получение списка с сайта hh.ru
        :return: None
        """
        from region_id import get_region
        self.ui.comboButton.addItems(['выбор региона'] + get_region())

    def read_hh(self) -> None:
        """
        Чтение базы данных и вывод в поле программы.
        :return: None
        """
        _db = Database('hh')
        self.ui.textBrowser.clear()
        if os.path.exists('_hh-trudvsem_.db'):
            _output = _db.read_db()
            _count = 0
            for line in _output:
                self.ui.textBrowser.append(line)
                _count += 1
            self.ui.lcdNumber.display(_count)
            self.ui.textBrowser.scrollToAnchor("scroll")
        else:
            self.ui.textBrowser.append('\n\n' + '  База Данных отсутствует  '
                                                ''.center(107, '*'))

    def extract_hh(self) -> None:
        """
        Парсит вакансии с api.hh.ru,
        выводит ответ в поле вывода,
        пишет в лог-файл.
        :return: None
        """
        _db = Database('hh')
        self.ui.textBrowser.clear()
        period = self.ui.lineEdit_5.displayText()
        professional_role = '&professional_role=' + str(
            self.ui.lineEdit_3.displayText()) if len(
            self.ui.lineEdit_3.displayText().strip()) > 0 else ''
        text_profession = '&text=' + self.ui.lineEdit.displayText()
        if self.ui.comboButton.currentText() != 'выбор региона':
            self.ui.lineEdit_2.setText(
                self.ui.comboButton.currentText().split(': ')[1])
        page = self.ui.spinBox.value()
        if page == 0:
            self.set_state()
        hold_state = [self.text_vacancies, self.text_period,
                      self.text_professional_role, self.text_area,
                      self.text_industry, self.text_page_count,
                      self.checkbox_2_time, self.checkbox_6_schedule,
                      self.checkbox_7_schedule, self.checkbox_8_schedule,
                      self.checkbox_9_schedule, self.checkbox_10_schedule]
        current_state = [self.ui.lineEdit.displayText(),
                         self.ui.lineEdit_5.displayText(),
                         self.ui.lineEdit_3.displayText(),
                         self.ui.lineEdit_2.displayText(),
                         self.ui.lineEdit_6.displayText(),
                         self.ui.lineEdit_4.displayText(),
                         self.ui.checkbox_2.checkState(),
                         self.ui.checkbox_6.checkState(),
                         self.ui.checkbox_7.checkState(),
                         self.ui.checkbox_8.checkState(),
                         self.ui.checkbox_9.checkState(),
                         self.ui.checkbox_10.checkState()]
        if [i for i in zip(hold_state, current_state) if i[0] != i[1]]:
            page = 0
            self.set_state()
        count = self.ui.lineEdit_4.displayText()
        area = self.ui.lineEdit_2.displayText()
        checkbox = [self.ui.checkbox_6.isChecked(),
                    self.ui.checkbox_7.isChecked(),
                    self.ui.checkbox_8.isChecked(),
                    self.ui.checkbox_9.isChecked(),
                    self.ui.checkbox_10.isChecked()]
        day = [f'&schedule={i}' for i in [
            'fullDay', 'remote', 'flyInFlyOut', 'shift', 'flexible']]
        checkbox_schedule = list(filter(lambda x: x[0], list(zip(checkbox, day))))
        schedule_id = '' if len(checkbox_schedule) == len(checkbox) else \
            ''.join(i[1] for i in checkbox_schedule)
        industry = '&industry=' + str(self.ui.lineEdit_6.displayText()) if len(
            self.ui.lineEdit_6.displayText().strip()) > 0 else ''
        publication_time = 'order_by=publication_time&' if self.ui.checkbox_2.isChecked() else ''
        url = (f'https://api.hh.ru/vacancies?clusters=true&st=searchVacancy'
               f'&enable_snippets=true&{publication_time}period={period}'
               f'&only_with_salary=false{professional_role}{text_profession}'
               f'&page={page}&per_page={count}&area={area}{industry}'
               f'&responses_count_enabled=true{schedule_id}')

        if self.extract_hh:
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
            _db.drop_database()
            _db.initialize_database()
        save_csv, save_xls = [], []

        try:
            # print('Headhunter: парсинг страницы')
            result = get(url, headers)
            results = result.json()
            count_results = results.get('found')
            # print('Найдено результатов:', count_results)
            # print('\n' + '*' * 150 + '\n')
            self.ui.lcdNumber.display(count_results)
            if self.ui.checkbox_3.isChecked():
                with open('_hh_.txt', 'w', encoding='utf-8') as text:
                    text.write(f'Найдено результатов: {count_results}\n\n')
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
                            counter = ('\n🚷   Всего количество вакансий у '
                                       'компании: ' + str(get(url_id, header).json(
                            ).get('open_vacancies', 0)) + '\n')
                            return counter

                        count_vacancies = get_count_vacancies(company_id, headers)
                    requirement = str(index['snippet']['requirement']).replace(
                        '<highlighttext>', '*')
                    requirement = str(requirement).replace('</highlighttext>', '*')
                    responsibility = str(index['snippet']['requirement']).replace(
                        '<highlighttext>', '*')
                    responsibility = str(responsibility).replace('</highlighttext>', '*')
                    information = (
                            f'\n🐵   Отрывок из требований по вакансии: '
                            f'{requirement}\n🐼   Отрывок из обязанностей по '
                            f'вакансии: {responsibility}\n' + count_vacancies
                    )
                if salary:
                    from_salary = salary['from']
                    to_salary = salary['to']
                    if not isinstance(from_salary, int):
                        from_salary = '😜'
                    if not isinstance(to_salary, int):
                        to_salary = '🚀'
                    output = (
                            f'  {company}  '.center(107, '*') + f'\n\n🚮   '
                            f'Профессия: {name}\n😍   Зарплата: {from_salary} '
                            f'- {to_salary}\n⚜   Ссылка: {link}\n🐯   /{types}/'
                            f'   -🌼-   дата публикации: {date}   -🌻-   '
                            f'график работы: {schedule.lower()}\n🚦   Количество'
                            f' откликов для вакансии: {counters_responses}\n🚘'
                            f'   Адрес: {address}\n{information}'
                    )
                    # print(output)
                    self.ui.textBrowser.append(output)
                    if self.ui.checkbox_3.isChecked():
                        text = open('_hh_.txt', 'a', encoding='utf-8')
                        text.write(output.center(120, '*') + '\n')
                    if self.ui.checkbox_4.isChecked():
                        _db.insert_hh(company, name, str(from_salary),
                                      str(to_salary), link, types, date,
                                      schedule.lower(), counters_responses,
                                      address)
                    if self.ui.checkbox_11.isChecked():
                        salary_from = salary['from'] if isinstance(salary['from'], int) else '*'
                        salary_to = salary['to'] if isinstance(salary['to'], int) else '*'
                        save_csv.append([company, name, salary_from, salary_to,
                                         link, types, date, schedule.lower(),
                                         counters_responses, address])
                    if self.ui.checkbox_12.isChecked():
                        save_xls.append([company, name, from_salary, to_salary,
                                         link, types, date, schedule.lower(),
                                         counters_responses, address])
                else:
                    output = (
                            f'  {company}  '.center(107, '*') + f'\n\n🚮   '
                            f'Профессия: {name}\n😍   Зарплата: не указана\n'
                            f'⚜   Ссылка: {link}\n🐯   /{types}/   -🌼-   '
                            f'дата публикации: {date}   -🌻-   график работы: '
                            f'{schedule.lower()}\n🚦   Количество откликов для '
                            f'вакансии: {counters_responses}\n🚘   Адрес: '
                            f'{address}\n{information}'
                    )
                    # print(output)
                    self.ui.textBrowser.append(output)
                    if self.ui.checkbox_3.isChecked():
                        text = open('_hh_.txt', 'a', encoding='utf-8')
                        text.write(output.center(120, '*') + '\n')
                    if self.ui.checkbox_4.isChecked():
                        _db.insert_hh(company, name, 'не указана',
                                      'не указана', link, types, date,
                                      schedule.lower(), counters_responses,
                                      address)
                    if self.ui.checkbox_11.isChecked():
                        save_csv.append([company, name, 'не указана',
                                         'не указана', link, types,
                                         date, schedule.lower(),
                                         counters_responses, address])
                    if self.ui.checkbox_12.isChecked():
                        save_xls.append([company, name, 'не указана',
                                         'не указана', link, types,
                                         date, schedule.lower(),
                                         counters_responses, address])
                # self.ui.textBrowser.append("<a name=\"scroll\" href=\"\">۩</a>")
            if self.ui.checkbox_3.isChecked():
                text.close()
            if self.ui.checkbox_11.isChecked():
                save_to_csv('hh', save_csv)
            if self.ui.checkbox_12.isChecked():
                save_to_xls('hh', save_xls)
            self.ui.textBrowser.scrollToAnchor("scroll")
            if self.ui.checkbox_5.isChecked():
                from PyQt5 import QtGui
                pdf = QtGui.QPdfWriter('_hh_.pdf')
                self.ui.textBrowser.print(pdf)
        except OSError as error:
            if str(error).find('HTTPSConnection') != -1:
                # print(f'Статус: проблемы с доступом в интернет\n{error}')
                self.ui.textBrowser.append('\n\n\n' +
                                           '  Статус: проблемы с доступом в '
                                           'интернет  '.center(142, '-'))
            else:
                # print(f'Статус: не хватает прав доступа\n{error}')
                self.ui.textBrowser.append(
                    '\n\n\n' + '  Статус: не хватает прав доступа создания '
                               'лог файла (базы данных)  '.center(130, '-'))

    def read_trudvsem(self) -> None:
        """
        Чтение базы данных и вывод в поле программы.
        :return: None
        """
        _db = Database('trudvsem')
        self.ui.textBrowser_2.clear()
        if os.path.exists('_hh-trudvsem_.db'):
            _output = _db.read_db()
            _count = 0
            for line in _output:
                self.ui.textBrowser_2.append(line)
                _count += 1
            self.ui.lcdNumber_2.display(_count)
            self.ui.textBrowser_2.scrollToAnchor("scroll")
        else:
            self.ui.textBrowser_2.append(
                '\n\n' + '  База Данных отсутствует  '.center(107, '*'))

    def extract_trudvsem(self) -> None:
        """  Парсер вакансий с сайта trudvsem.ru """
        _db = Database('trudvsem')
        self.ui.textBrowser_2.clear()
        if self.ui.checkbox_24.isChecked():
            _db.drop_database()
            _db.initialize_database()
        try:
            text_profession = f'&text={self.ui.lineEdit_20.displayText()}'
            if self.ui.comboButton_2.currentText() != 'выбор региона':
                self.ui.lineEdit_21.setText(
                    self.ui.comboButton_2.currentText().split(': ')[1])
            region = f'/region/{self.ui.lineEdit_21.displayText()}00000000000'\
                if len(self.ui.lineEdit_21.displayText()) > 0 else ''

            day = int(self.ui.lineEdit_23.displayText())
            pd = dd.fromtimestamp(time() - 86400 * day)
            period = f'&modifiedFrom={pd}T08:00:00Z' if len(
                self.ui.lineEdit_23.displayText()) > 0 else ''

            page_count = f'&limit={self.ui.lineEdit_22.displayText()}' if len(
                self.ui.lineEdit_22.displayText()) else ''

            page = self.ui.spinBox_2.value()
            if page == 0:
                self.set_state()

            hold_state = [self.tv_vacancies, self.tv_area,
                          self.tv_page_count, self.tv_period]
            current_state = [self.ui.lineEdit_20.displayText(),
                             self.ui.lineEdit_21.displayText(),
                             self.ui.lineEdit_22.displayText(),
                             self.ui.lineEdit_23.displayText()]
            if [i for i in zip(hold_state, current_state) if i[0] != i[1]]:
                page = 0
                self.set_state()

            url = (f'https://opendata.trudvsem.ru/api/v1/vacancies{region}?'
                   f'{text_profession}&offset={page}{page_count}{period}')

            headers = {
                'Host': 'opendata.trudvsem.ru',
                'User-Agent': 'Mozilla/5.0',
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive'
            }

            if self.extract_trudvsem:
                page = int(page) + 1
                self.ui.spinBox_2.setValue(page)

            result = get(url, headers)
            results = result.json()
            count_vacancies = results.get('meta').get('total', 0)
            vacancies = results.get('results', 0).get('vacancies', {})
            # print('Найдено результатов:', count_vacancies)
            self.ui.lcdNumber_2.display(count_vacancies)
            save_xls = []
            if count_vacancies > 0 and len(vacancies) > 0:
                for index in vacancies:
                    company = index['vacancy']['company']['name']
                    name = index['vacancy']['job-name']
                    link = index['vacancy']['vac_url']
                    date = index['vacancy']['creation-date']
                    address = index['vacancy']['addresses']['address'][0][
                        'location']
                    schedule = index.get('vacancy').get('schedule', 'не указано')
                    # salary = index['vacancy']['salary']
                    if count_vacancies > 0:
                        from_salary = index.get('vacancy').get('salary_min', 0)
                        to_salary = index.get('vacancy').get('salary_max', 0)
                        if from_salary == 0:
                            from_salary = '😜'
                        if to_salary == 0:
                            to_salary = '🚀'
                        output = (
                                f'  {company}  '.center(107, '*') + f'\n\n🚮   '
                                f'Профессия: {name}\n😍   Зарплата: '
                                f'{from_salary} - {to_salary}\n⚜   Ссылка: '
                                f'{link}\n🐯   дата публикации: {date}   -🌻-'
                                f'   график работы: {schedule.lower()}\n🚘   '
                                f'Адрес: {address}\n'
                        )
                        # print(output)
                        self.ui.textBrowser_2.append(output)
                        if self.ui.checkbox_24.isChecked():
                            _db.insert_trudvsem(company, name, str(from_salary),
                                                str(to_salary), link, date,
                                                schedule.lower(), address)
                        if self.ui.checkbox_26.isChecked():
                            save_xls.append([company, name, str(from_salary),
                                             str(to_salary), link, date,
                                             schedule.lower(), address])
                self.ui.textBrowser_2.scrollToAnchor("scroll")
                if self.ui.checkbox_26.isChecked():
                    save_to_xls('trudvsem', save_xls)
                if self.ui.checkbox_25.isChecked():
                    from PyQt5 import QtGui
                    pdf = QtGui.QPdfWriter('_trudvsem_.pdf')
                    self.ui.textBrowser_2.print(pdf)
        except OSError as error:
            # print(f'Статус: проблемы с доступом в интернет\n{error}')
            self.ui.textBrowser_2.append(
                '\n\n\n' + '  Статус: не хватает прав доступа создания '
                           'лог файла (базы данных)  '.center(130, '-'))
