# ----- Method1 ----- #
# import xlrd
# import csv

# def csv_from_excel():
#     wb = xlrd.open_workbook('PM_Label_and_Fovea_Location.xlsx')
#     sh = wb.sheet_by_name('sheet1')
#     your_csv_file = open('PM_Label_and_Fovea_Location.csv', 'w')
#     wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

#     for rownum in range(sh.nrows):
#         wr.writerow(sh.row_values(rownum))

#     your_csv_file.close()

# # runs the csv_from_excel function:
# csv_from_excel()


# ----- Method2 ----- #
import pandas as pd

data_xls = pd.read_excel('PM_Label_and_Fovea_Location.xlsx', 'sheet1', dtype=str, index_col=None)
data_xls.to_csv('PM_Label_and_Fovea_Location.csv', encoding='utf-8', index=False)