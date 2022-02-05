import sys
import requests
from PyQt5 import QtWidgets
from job_desine import Ui_MainWindow


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setup_ui(self)
        self.ui.pushButton.clicked.connect(self.extract_jobs)

    def extract_jobs(self):
        self.ui.textBrowser.clear()
        period = self.ui.lineEdit_5.displayText()
        # professional_role = '96'  # программист
        professional_role = ''
        if len(self.ui.lineEdit_3.displayText().strip()) > 0:
            professional_role = '&professional_role=' + str(self.ui.lineEdit_3.displayText())
        text_profession = '&text=' + self.ui.lineEdit.displayText()
        page = self.ui.spinBox.value()
        count = self.ui.lineEdit_4.displayText()
        area = self.ui.lineEdit_2.displayText()
        # area = 1979 - Комсомольск-на-Амуре/ 1975 - Хабаровский край/ 102 - Хабаровск
        # area = 113 - Россия/ 1948 - Приморский край/ 22 - Владивосток
        # '&employer_id=3083859'  идентификатор компании Амурсталь
        # enable_snippets=true&
        url = f'https://api.hh.ru/vacancies?clusters=true&st=searchVacancy&' \
              f'period={period}&only_with_salary=false{professional_role}{text_profession}&' \
              f'page={page}&per_page={count}&area={area}&responses_count_enabled=true'

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
        try:
            print(f'Headhunter: парсинг страницы')
            result = requests.get(url, headers)
            results = result.json()
            print('Найдено результатов:', results.get('found'))
            print('\n' + '*' * 150 + '\n')
            self.ui.lcdNumber.display(results.get('found'))
            with open('_vacancies.txt', 'w', encoding='utf-8') as text:
                text.write('Найдено результатов:' + str(results.get('found')) + '\n\n')
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
                text = open('_vacancies.txt', 'a', encoding='utf-8')
                information = ''
                if self.ui.radioButton.isChecked():
                    count_vacancies = ''
                    # company_id = index['employer']['id']
                    # url_id = f'https://api.hh.ru/employers/{company_id}'
                    # count_vacancies = ('\n🚷   Всего количество вакансий у компании: ' + str(
                    #     requests.get(url_id, headers).json().get('open_vacancies', {})) + '\n')

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
                    text.write(output.center(120, '*') + '\n')
                else:
                    output = (f'  {company}  '.center(107, '*') + f'\n\n🚮   Профессия: {name}\n😍'
                              f'   Зарплата: не указана\n⚜   Ссылка: {link}\n🐯   /{types}/'
                              f'   -🌼-   дата публикации: {date}   -🌻-   график работы: '
                              f'{schedule.lower()}\n🚦   Количество откликов для вакансии: '
                              f'{counters_responses}\n🚘   Адрес: {address}\n{information}')
                    print(output)
                    self.ui.textBrowser.append(output)
                    text.write(output.center(120, '*') + '\n')
                text.close()
        except OSError as error:
            print(f'Статус: проблемы с доступом в интернет\n{error}')
            self.ui.textBrowser.append(
                '\n\n\n' + '  Статус: проблемы с доступом в интернет  '.center(142, '-'))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
