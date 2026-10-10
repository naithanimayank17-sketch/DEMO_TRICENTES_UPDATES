import openpyxl

def get_login_data():
    workbook = openpyxl.load_workbook('D://NOIDA CLASSES//DemowebshopTricentis//test_data//loginData.xlsx')
    sheet = workbook['LoginData']

    data = []

    for row in sheet.iter_rows(min_row=1,values_only=True):
        data.append(row)

    return data