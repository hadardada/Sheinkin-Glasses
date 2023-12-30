import json
import xlsxwriter
from datetime import datetime
import openpyxl
import os

Path = "all_history/"
filelist = os.listdir(Path)
json_trans = []
for i in filelist:
    if i.endswith(".json"):
        f = open (Path + i, 'r', encoding='utf-8')
        his_json = json.load(f)
        json_trans += his_json
        f.close

workbook = xlsxwriter.Workbook('tipulim.xlsx')
worksheet = workbook.add_worksheet()


#iterate over history of transections and create xl file (to align with the input format):
row_num = 1
cols = range (20)
for i in json_trans:
    if i['customer']: #if customer is not empty
        first_name = ""
        last_name = ""
        if i['customer']['name'] != None and i['customer']['name'] != '': 
            first_name = " ".join(i['customer']['name'].split()[:-1])
            last_name = i['customer']['name'].split()[-1]
        #looping over all products of each transaction
        for j in i['products']:
            col_num = iter(cols)
            next(col_num) #teudat zehut
            worksheet.write(row_num, next(col_num), i['customer']['id']) #filename
            worksheet.write(row_num, next(col_num), first_name) # first name
            worksheet.write(row_num, next(col_num), last_name) # last name
            worksheet.write(row_num, next(col_num), i['employee']['name']) #employee name
            category = j['categories'][0] if j['categories'] else " "
            worksheet.write(row_num, next(col_num), category) #categories
            next(col_num) #traetment code
            worksheet.write(row_num, next(col_num), j['name']) #name of product
            worksheet.write(row_num, next(col_num), "branch: " + i['branch']['name']) #description
            worksheet.write(row_num, next(col_num), str(j['documentAmount'])) #price
            worksheet.write(row_num, next(col_num), datetime.fromisoformat(i['executedAt']).strftime("%d/%m/%y")) #date
            worksheet.write(row_num, next(col_num), datetime.fromisoformat(i['executedAt']).strftime("%H:%M")) #time
            next(col_num) #duration
            worksheet.write(row_num, next(col_num), i['payment']['receiptNumber']) #receiptNumber

            row_num += 1
  
workbook.close()
