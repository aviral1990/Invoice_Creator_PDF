import pandas as pd
import glob
from fpdf import FPDF

#get filepaths of excel files, and store in list
invoice_list=glob.glob("Invoices/*.xlsx")

#Iterate through each filepath
for item in invoice_list:
    #create PDF invoice
    pdf=FPDF(orientation='P',unit='mm',format="A4")
    pdf.set_font(family="Times", style="B", size=12)
    invoice_no=item.split('\\')[1].split('-')[0]     #Invoice Number
    invoice_date=item.split('\\')[1].split('-')[1]     #Invoice Date
    pdf.add_page()
    pdf.cell(w=0, h=3, txt=f"Invoice No. - {invoice_no}", border=0, ln=1, align="L")
    pdf.ln(3)
    pdf.cell(w=0, h=3, txt=f"Date - {invoice_date[:-5]}", border=0, ln=1, align="L")
    pdf.ln(3)


    #Read Excel and convert to pdf
    df = pd.read_excel(item, 'Sheet 1')
    column_headers=list(df.columns)
    # Column Headers
    pdf.set_font(family="Times", style="B", size=12)
    pdf.cell(w=30, h=8, txt=column_headers[0].title(), align="C", border=1)
    pdf.cell(w=60, h=8, txt=column_headers[1].title(), align="C", border=1)
    pdf.cell(w=40, h=8, txt=column_headers[2].title(), align="C", border=1)
    pdf.cell(w=30, h=8, txt=column_headers[3].title(), align="C", border=1)
    pdf.cell(w=30, h=8, txt=column_headers[4].title(), align="C", border=1, ln=1)
    # pdf.ln(10)
    total = 0
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=30,h=8,txt=str(row['product_id']),align="C",border=1)
        pdf.cell(w=60, h=8, txt=row['product_name'],align="C",border=1)
        pdf.cell(w=40, h=8, txt=str(row['amount_purchased']),align="C",border=1)
        pdf.cell(w=30, h=8, txt=str(row['price_per_unit']),align="C",border=1)
        pdf.cell(w=30, h=8, txt=str(row['total_price']),align="C",border=1,ln=1) #ln=1,after call,move to next line
        #pdf.ln(10)
        total = total + float(row['total_price'])

    #Write the total
    pdf.cell(w=30, h=8, txt='', align="C")
    pdf.cell(w=60, h=8, txt='', align="C")
    pdf.cell(w=40, h=8, txt='', align="C")
    pdf.set_font(family="Times", size=12,style="B")
    pdf.cell(w=30, h=8, txt='TOTAL', align="C",border=1)
    pdf.set_font(family="Times", size=12)
    pdf.cell(w=30, h=8, txt=str(total), align="C",border=1)

    filename_output_pdf = item.split('\\')[1][:-5]
    pdf.output(f"PDFs/{filename_output_pdf}.pdf")

