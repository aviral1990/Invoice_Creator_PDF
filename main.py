import pandas as pd
import os
PATH='E:\Tutorials\DOCUMENTS & SOURCE CODES\Python Projects Pycharm\Invoice_Creator'

invoice_list=[]

#get file names of invoices in the folder
for x in os.listdir():
    if(x.endswith('.xlsx')):
        invoice_list.append(x)

for item in invoice_list:
    df=pd.read_excel(item,index_col=0)
    print(df)