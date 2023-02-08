import pandas as pd
import glob
from fpdf import FPDF

#get filepaths of excel files, and store in list
invoice_list=glob.glob("Invoices/*.xlsx")

#Iterate through filepath
for item in invoice_list:
    df=pd.read_excel(item,'Sheet 1')
    total=0
    for index,row in df.iterrows():
        print(row['total_price'])
        total=total+float(row['total_price'])

    #create PDF invoice
    pdf=FPDF(orientation='P',unit='mm',format="A4")
    pdf.set_font(family="Times", style="B", size=12)
    invoice_no=item.split('\\')[1].split('-')[0]     #Invoice Number
    invoice_date=item.split('\\')[1].split('-')[1]     #Invoice Date
    pdf.add_page()
    pdf.cell(w=0, h=3, txt=f"Invoice No. - {invoice_no}", border=0, ln=1, align="L")
    pdf.ln(3)
    pdf.cell(w=0, h=3, txt=f"Date - {invoice_date[:-5]}", border=0, ln=1, align="L")
    filename_output_pdf = item.split('\\')[1][:-5]
    pdf.output(f"PDFs/{filename_output_pdf}.pdf")