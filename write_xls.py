import openpyxl


def save_to_xls(data):
    """ Создание xlsx файла и запись в него """
    book = openpyxl.Workbook()
    book.remove(book.active)
    sheet = book.create_sheet("Вакансии")
    sheet.column_dimensions["A"].width = 40
    sheet.column_dimensions["B"].width = 50
    sheet.column_dimensions["C"].width = 10
    sheet.column_dimensions["D"].width = 10
    sheet.column_dimensions["E"].width = 30
    sheet.column_dimensions["F"].width = 13
    sheet.column_dimensions["G"].width = 13
    sheet.column_dimensions["H"].width = 18
    sheet.column_dimensions["I"].width = 5
    sheet.column_dimensions["J"].width = 50
    [sheet.append(i) for i in data]
    book.save("_vacancies.xlsx")
