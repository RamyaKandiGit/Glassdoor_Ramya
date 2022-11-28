import xlrd
from Library.config import Config


def read_locators():
    workbook=xlrd.open_workbook(Config.DATA_PATH)
    worksheet=workbook.sheet_by_name("glsdr_login")
    rows=worksheet.get_rows()
    print(rows)
    d={}

    for row in rows:
        d[row[0].value]= (row[1].value,row[2].value)

    return d

# print(read_locators())

def read_data():
    workbook = xlrd.open_workbook(Config.DATA_PATH)
    worksheet = workbook.sheet_by_name('data')
    rows = worksheet.get_rows()
    column = worksheet.ncols
    header = next(rows)
    data = []

    for row in rows:
        value = ()
        for j in range(column):
            value += (row[j].value,)
        data.append(value)

    return data

print(read_data())


