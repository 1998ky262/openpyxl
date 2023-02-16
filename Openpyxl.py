import openpyxl
way = openpyxl.load_workbook("openpyxl_test.xlsx")
sheet = way.worksheets[0]
way.save("openpyxl_test.xlsx")
way.close()
