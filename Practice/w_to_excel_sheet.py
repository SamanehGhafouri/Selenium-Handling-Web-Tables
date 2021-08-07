import xlwt
from xlwt import Workbook

style = xlwt.easyxf('font: bold 1, color red')
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

sheet1.write(0, 0, 'First Name', style)
sheet1.write(0, 1, 'Last Name', style)
sheet1.write(0, 2, 'Ages', style)

# First name
sheet1.write(1, 0, 'Samaneh')
sheet1.write(2, 0, 'Stefan')


# Last name
sheet1.write(1, 1, 'Ghafouri')
sheet1.write(2, 1, 'Agapie')

# Ages
sheet1.write(1, 2, '31')
sheet1.write(2, 2, '44')
wb.save('example.xls')
