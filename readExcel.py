#coding:utf-8
import xlrd
import food
from datetime import date,datetime
#readExcel is used to get food information
def read_excel(name):
    # 打开文件
    workbook = xlrd.open_workbook(filename=name)
    # 获取所有sheet
    #print workbook.sheet_names() # [u'sheet1', u'sheet2']
    #sheet2_name = workbook.sheet_names()[1]

    # 根据sheet索引或者名称获取sheet内容
    #sheet1 = workbook.sheet_by_index(0) # sheet索引从0开始
    #sheet2 = workbook.sheet_by_name('sheet2')

    # sheet的名称，行数，列数
    #print sheet2.name,sheet2.nrows,sheet2.ncols

    # 获取整行和整列的值（数组）
    #rows = sheet2.row_values(3) # 获取第四行内容
    #cols = sheet2.col_values(2) # 获取第三列内容
    #print rows
    #print cols

    # 获取单元格内容
    #print sheet2.cell(1,0).value.encode('utf-8')
    #print sheet2.cell_value(1,0).encode('utf-8')
    #print sheet2.row(1)[0].value.encode('utf-8')
    
    # 获取单元格内容的数据类型
    #print sheet2.cell(1,0).ctype

    #put information to FOOD
    FOOD = []
    information = []
    sheet1 = workbook.sheet_by_index(0)
    for i in range(1,sheet1.nrows):
        for j in range(0,sheet1.ncols):
            information.append(sheet1.cell(i,j).value)
        FOOD.append(food.ItemFD(information[0],information[1],information[2],information[3],information[4],information[5],information[6]))
        information = []
    print(FOOD[0].R)
    return FOOD
    

