from openpyxl import workbook, Workbook

workbook = Workbook()
sheet =workbook.active
sheet.title = 'samplesheet'
data_list = [
    ['mani','50','hyd'],
    ['pri','67','hub']
]
for row in data_list:
    sheet.append(row)

workbook.save('emp_list.xlsx')