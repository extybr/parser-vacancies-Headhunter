from requests import get
from pathlib import Path
from datetime import date as dd
from time import time
from PyQt5 import QtWidgets
from gui import UiMainWindow
from database import Database
from write_csv import save_to_csv
from write_xls import save_to_xls


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = UiMainWindow()
        self.ui.setup_ui(self)
        self.ui.pushButton.clicked.connect(self.extract_hh)
        self.ui.pushButton_2.clicked.connect(self.read_hh)
        self.ui.pushButton_3.clicked.connect(self.extract_trudvsem)
        self.ui.pushButton_4.clicked.connect(self.read_trudvsem)
        self.ui.pushButton_5.clicked.connect(self.get_hh_areas_id)
        self.ui.pushButton_6.clicked.connect(self.get_tv_areas_id)
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

    def set_state(self) -> None:
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

    def get_hh_areas_id(self) -> None:
        """
        Получение списка с сайта hh.ru.
        Не записывается и не запоминается.
        :return: None
        """
        from region_id import get_hh_region
        self.ui.comboButton.clear()
        self.ui.comboButton.addItems(['выбор региона'] + get_hh_region())

    def get_tv_areas_id(self) -> None:
        """
        Получение списка с сайта trudvsem.ru.
        Не записывается и не запоминается.
        :return: None
        """
        from region_id import get_tv_region
        self.ui.comboButton_2.clear()
        self.ui.comboButton_2.addItems(['выбор региона'] + get_tv_region())

    def read_database(self, name, index) -> None:
        """
        Чтение базы данных и вывод в поле программы.
        :return: None
        """
        _db = Database(name)
        browser = self.ui.textBrowser if index == 1 else self.ui.textBrowser_2
        lcd = self.ui.lcdNumber if index == 1 else self.ui.lcdNumber_2
        browser.clear()
        if Path.exists(Path('_hh-trudvsem_.db')):
            _output = _db.read_db()
            _count = 0
            for line in _output:
                browser.append(f'<html>{line}</html>')
                _count += 1
            lcd.display(_count)
            browser.scrollToAnchor("scroll")
        else:
            browser.append(
                '\n\n' + '  База Данных отсутствует  '.center(107, '*'))

    def read_hh(self) -> None:
        """ Выбор названия таблицы для чтения из базы данных """
        self.read_database(name='hh', index=1)

    def read_trudvsem(self) -> None:
        """ Выбор названия таблицы для чтения из базы данных """
        self.read_database(name='trudvsem', index=2)

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
        professional_role = (
            f'&professional_role={self.ui.lineEdit_3.displayText()}'
            if len(self.ui.lineEdit_3.displayText().strip()) > 0 else ''
        )
        text_profession = f'&text={self.ui.lineEdit.displayText()}'
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
        schedule_id = ('' if len(checkbox_schedule) == len(checkbox)
                       else ''.join(i[1] for i in checkbox_schedule))
        industry = (f'&industry={self.ui.lineEdit_6.displayText()}'
                    if len(self.ui.lineEdit_6.displayText().strip()) > 0 else '')
        publication_time = ('&order_by=publication_time' if
                            self.ui.checkbox_2.isChecked() else '')
        url = (f'https://api.hh.ru/vacancies?clusters=true&st=searchVacancy'
               f'&enable_snippets=true{publication_time}&period={period}'
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
                schedule = index['schedule']['name'].lower()
                date = index['published_at'][:10]
                address = index['area']['name']
                if index['address']:
                    address = index['address']['raw']
                # logo = index['employer']['logo_urls']['90']

                information = ''
                if self.ui.radioButton.isChecked():
                    count_vacancies = ''
                    if self.ui.checkbox.isChecked():
                        company_id = index['employer']['id']

                        def get_count_vacancies(company_number: str, header: dict) -> str:
                            url_id = f'https://api.hh.ru/employers/{company_number}'
                            cnt = str(get(url_id, header).json().get('open_vacancies', 0))
                            counter = (f'🚷   Всего количество вакансий у '
                                       f'компании: {cnt}')
                            return counter

                        count_vacancies = get_count_vacancies(company_id, headers)
                    requirement = index['snippet']['requirement']
                    responsibility = index['snippet']['responsibility']
                    information = (
                        f'<p align=center><br>🐵   Отрывок из требований'
                        f' по вакансии: {requirement}<br>🐼   Отрывок из '
                        f'обязанностей по вакансии: {responsibility}<br>'
                        f'{count_vacancies}</p>'
                    )

                salary = index['salary']
                from_salary, to_salary = 'не указана', 'не указана'
                if salary:
                    from_salary = (salary['from']
                                   if isinstance(salary['from'], int) else '😜')
                    to_salary = (salary['to']
                                 if isinstance(salary['to'], int) else '🚀')
                salary_full = (f'{from_salary} - {to_salary}'
                               if (from_salary and to_salary) != 'не указана'
                               else 'не указана')

                html = (f'<p align="center"><font color=#027132>'
                        f'<h3><b>{company}</b></h3></font>'
                        f'<ul><br>🚮   Профессия: <b>{name}</b></br>'
                        f'<br>😍   Зарплата: <b>{salary_full}</b></br>'
                        f'<br>⚜   Ссылка: <a href="{link}">{link}</a></br>'
                        f'<br>🐯   /{types}/   -🌼-   дата публикации: '
                        f'<b>{date}</b>   -🌻-   график работы: <b>'
                        f'{schedule}</b></br>'
                        f'<br>🚦   Количество откликов для вакансии: '
                        f'{counters_responses}</br>'
                        f'<br>🚘   Адрес: {address}</br></ul></p>')
                if not self.ui.checkbox_13.isChecked():
                    html = html.replace('</font>', '</font></p>')
                if information:
                    html += information
                self.ui.textBrowser.append(html)
                sign = ''.center(100, '*')
                self.ui.textBrowser.append(f'<html>{sign}</html>')

                output = (
                        f'  {company}  '.center(107, '*') + f'\n\n🚮   '
                        f'Профессия: {name}\n😍   Зарплата: {salary_full}\n'
                        f'⚜   Ссылка: {link}\n🐯   /{types}/'
                        f'   -🌼-   дата публикации: {date}   -🌻-   '
                        f'график работы: {schedule}\n🚦   Количество'
                        f' откликов для вакансии: {counters_responses}\n🚘'
                        f'   Адрес: {address}\n{information}'
                )
                # print(output)
                if self.ui.checkbox_3.isChecked():
                    text = open('_hh_.txt', 'a', encoding='utf-8')
                    text.write(output.center(120, '*') + '\n')

                if self.ui.checkbox_4.isChecked():
                    _db.insert_hh(company, name, str(from_salary),
                                  str(to_salary), link, types, date,
                                  schedule, counters_responses, address)

                if self.ui.checkbox_12.isChecked():
                    save_xls.append([company, name, from_salary, to_salary,
                                     link, types, date, schedule,
                                     counters_responses, address])

                if self.ui.checkbox_11.isChecked():
                    if salary:
                        from_salary = (salary['from'] if isinstance(
                            salary['from'], int) else '*')
                        to_salary = (salary['to'] if isinstance(
                            salary['to'], int) else '*')
                    save_csv.append([company, name, from_salary, to_salary,
                                     link, types, date, schedule,
                                     counters_responses, address])

            if self.ui.checkbox_3.isChecked():
                text.close()

            if self.ui.checkbox_11.isChecked():
                save_to_csv('hh', save_csv)

            if self.ui.checkbox_12.isChecked():
                save_to_xls('hh', save_xls)

            if self.ui.checkbox_5.isChecked():
                from PyQt5 import QtGui
                pdf = QtGui.QPdfWriter('_hh_.pdf')
                self.ui.textBrowser.print(pdf)

            self.ui.textBrowser.scrollToAnchor("scroll")

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
        except Exception:
            pass

    def extract_trudvsem(self) -> None:
        """  Парсер вакансий с сайта trudvsem.ru """
        _db = Database('trudvsem')
        self.ui.textBrowser_2.clear()
        if self.ui.checkbox_24.isChecked():
            _db.drop_database()
            _db.initialize_database()
        try:
            text_profession = f'text={self.ui.lineEdit_20.displayText()}'
            if self.ui.comboButton_2.currentText() != 'выбор региона':
                self.ui.lineEdit_21.setText(
                    self.ui.comboButton_2.currentText().split(': ')[1])
            region = (f'/region/{self.ui.lineEdit_21.displayText()}00000000000'
                      if len(self.ui.lineEdit_21.displayText()) > 0 else '')

            day = int(self.ui.lineEdit_23.displayText())
            pd = dd.fromtimestamp(time() - 86400 * day)
            period = (f'&modifiedFrom={pd}T08:00:00Z'
                      if len(self.ui.lineEdit_23.displayText()) > 0 else '')

            page_count = (f'&limit={self.ui.lineEdit_22.displayText()}'
                          if len(self.ui.lineEdit_22.displayText()) else '')

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
            if count_vacancies > 0 < len(vacancies):
                for index in vacancies:
                    vacancy = index['vacancy']
                    company = vacancy['company']['name']
                    name = vacancy['job-name']
                    link = vacancy['vac_url']
                    date = vacancy['creation-date']
                    address = vacancy['addresses']['address'][0]['location']
                    schedule = vacancy.get('schedule', 'не указано').lower()
                    # salary = vacancy['salary']
                    from_salary = (vacancy['salary_min']
                                   if vacancy['salary_min'] != 0 else '😜')
                    to_salary = (vacancy['salary_max']
                                 if vacancy['salary_max'] != 0 else '🚀')
                    salary_full = ('{} - {}'.format(from_salary, to_salary)
                                   if not (
                            from_salary == '😜' and to_salary == '🚀')
                                   else 'не указана')

                    html = (f'<p align="center"><font color=#027132>'
                            f'<b>{company}</b></font>'
                            f'<ul><br><br>🚮   Профессия: <b>{name}</b></br>'
                            f'<br>😍   Зарплата: <b>{salary_full}</b></br>'
                            f'<br>⚜   Ссылка: <a href="{link}">{link}</a></br>'
                            f'<br>🐯   дата публикации: {date}   -🌻-   '
                            f'график работы: <b>{schedule}</b></br>'
                            f'<br>🚘   Адрес: {address}</br></p></ul>')
                    if not self.ui.checkbox_27.isChecked():
                        html = html.replace('</font>', '</font></p>')
                    self.ui.textBrowser_2.append(html)
                    sign = ''.center(100, '*')
                    self.ui.textBrowser_2.append(f'<html>{sign}</html>')

                    if self.ui.checkbox_24.isChecked():
                        _db.insert_trudvsem(company, name, str(from_salary),
                                            str(to_salary), link, date,
                                            schedule, address)

                    if self.ui.checkbox_26.isChecked():
                        save_xls.append([company, name, str(from_salary),
                                         str(to_salary), link, date,
                                         schedule, address])

                if self.ui.checkbox_26.isChecked():
                    save_to_xls('trudvsem', save_xls)

                if self.ui.checkbox_25.isChecked():
                    from PyQt5 import QtGui
                    pdf = QtGui.QPdfWriter('_trudvsem_.pdf')
                    self.ui.textBrowser_2.print(pdf)

            self.ui.textBrowser_2.scrollToAnchor("scroll")

        except OSError as error:
            if str(error).find('HTTPSConnection') != -1:
                # print(f'Статус: проблемы с доступом в интернет\n{error}')
                self.ui.textBrowser_2.append('\n\n\n' +
                                             '  Статус: проблемы с доступом в '
                                             'интернет  '.center(142, '-'))
            else:
                # print(f'Статус: не хватает прав доступа\n{error}')
                self.ui.textBrowser_2.append(
                    '\n\n\n' + '  Статус: не хватает прав доступа создания '
                               'лог файла (базы данных)  '.center(130, '-'))
        except Exception:
            pass
