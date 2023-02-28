from xlsxwriter import Workbook


def save_to_xls(name, data):
    workbook = Workbook(f'_{name}_.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.set_column('A:A', 40)
    worksheet.set_column('B:B', 50)
    worksheet.set_column('C:C', 10)
    worksheet.set_column('D:D', 10)
    worksheet.set_column('E:E', 30)
    worksheet.set_column('F:F', 13)
    worksheet.set_column('G:G', 13)
    worksheet.set_column('H:H', 18)
    worksheet.set_column('I:I', 5)
    worksheet.set_column('J:J', 50)
    [worksheet.write_row(i, 0, data[i]) for i in range(len(data))]
    workbook.close()
