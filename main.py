import pandas as pd
import glob
PATH='E:\Tutorials\DOCUMENTS & SOURCE CODES\Python Projects Pycharm\Invoice_Creator'

#get filepaths of excel files, and store in list
invoice_list=glob.glob("Invoices/*.xlsx")

print(invoice_list)


for item in invoice_list:
    df=pd.read_excel(item,'Sheet 1')
    total=0
    for index,row in df.iterrows():
        print(row['total_price'])
        total=total+float(row['total_price'])
    print(total)
