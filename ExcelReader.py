import xlrd
ExcelFileNmae = raw_input()
workbook = xlrd.open_workbook(ExcelFileName)
ExcelSheetName = raw_input()
worksheet = workbook.sheet_by_name(ExcelSheetName)

num_rows = worksheet.nrows
num_cols = worksheet.ncols

result_data = []
for curr_row in range(0,num_rows , 1):
    row_data = []
    for curr_col in range(0,num_cols,1):
        data = worksheet.cell_value(curr_row,curr_col)
        row_data.append(data)
    result_data.append(row_data)    
