import openpyxl
way = openpyxl.load_workbook("openpyxl_test.xlsx")
way.save("openpyxl_test.xlsx")
way.close()
