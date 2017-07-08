#This is about use python manipulate excel file
#https://raspberrypi.stackexchange.com/questions/44434/accessing-excel-sheet-using-python-in-raspbian

pip intall xlrd

import xlrd
workbook=xlrd.open_workbook('filename.csv')
first_sheet=xlrd.sheet_by_index(0)
def get_cell_range(start_col,start_row,end_col,end_row):
	return [sheet.row_slice(row,start_colx=start_col,end_colx=end_col+1) for row in xrange(start_row,end_row+1)]	#A3 to D7
