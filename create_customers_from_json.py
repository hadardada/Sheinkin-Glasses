import json
import xlsxwriter
from datetime import datetime

f = open("all_customers.json", 'r', encoding='utf-8')
cus_dicts =  json.load(f)
workbook = xlsxwriter.Workbook('all-customers.xlsx') # raw json objects, were scrapped from Practi using Postmen 
worksheet = workbook.add_worksheet()

date_from = datetime.fromisoformat('2022-12-07T12:19:02.622Z')

row_num = 0
cols = range (15)
for i in cus_dicts:

    creation_date = datetime.fromisoformat(i['created'])
    if creation_date > date_from:
        
        first_name = ""
        last_name = ""
        gender =""
        col_num = iter(cols)

        if i['name'] is not None and i['name'] is not '':
            first_name = i['name'].split()[0]
            last_name = " ".join(i['name'].split()[1:])
        worksheet.write(row_num, 0, first_name) # first name
        worksheet.write(row_num, 1, last_name) # last name
        worksheet.write(row_num, 2, i['phone'] if i['phone'] is not None else "") # phone number
        worksheet.write(row_num, 5, i['id']) #file name 
        worksheet.write(row_num, 6, i['birthDate']) #birth date
        if i['gender'] is not None:
            gender = "זכר" if i['gender'] == "M" else "נקבה"
        worksheet.write(row_num, 7, gender) #gender
        worksheet.write(row_num, 15, i['email']) #email address
        worksheet.write(row_num, 16, i['address']) #address
        worksheet.write(row_num, 17, i['city']) #city
        worksheet.write(row_num, 20, i['notes']) #notes
        if i['customFields']: # if customFields is not empty
            curr_col_num = 28
            for j in i['customFields']:
                if j['fieldId'] == "cd616511-9cc1-44c0-bcb3-3e39f93152c3": #test 
                    worksheet.write(row_num, curr_col_num + 0, j['value']) 
                if j['fieldId'] == "8c399bc0-a4b1-4d19-a3b6-ac9a4a67579d": #glasses type
                    worksheet.write(row_num, curr_col_num + 1, j['value']) 
                if j['fieldId'] == "4005850e-3183-44b3-a10a-5122df53aca7": #R- SPH, CYL, AXIS
                    worksheet.write(row_num, curr_col_num + 2, j['value']) 
                if j['fieldId'] == "6e2d2344-903f-4c72-bce8-187ae0f1e9ac": #L- SPH, CYL, AXIS
                    worksheet.write(row_num, curr_col_num + 3, j['value'])
                if j['fieldId'] == "cf9c44f7-808c-4a4a-8a86-6348045db7a6": #ADD
                    worksheet.write(row_num, curr_col_num + 4, j['value']) 
                if j['fieldId'] == "177b78a9-2ea5-4426-a2af-c7cee5c706a1": #PD
                    worksheet.write(row_num, curr_col_num + 5, j['value']) 
                if j['fieldId'] == "409a215a-4ccd-4751-a9f4-c1a9c72e6800": #NOTES
                    worksheet.write(row_num, curr_col_num + 6, j['value']) 
                if j['fieldId'] == "6bfb0c3b-d900-41d7-8cd8-c75b7d46f909": #right lens
                    worksheet.write(row_num, curr_col_num + 7, j['value'])
                if j['fieldId'] == "fa20b349-c3bd-4d66-b6e2-39b3ce74f705": #left lens
                    worksheet.write(row_num, curr_col_num + 8, j['value'])      
        row_num += 1       
workbook.close()
