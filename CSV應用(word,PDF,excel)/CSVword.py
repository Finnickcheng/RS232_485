import csv

# data =[
#     ['Name','Age','Location'],
#     ['John','25','New York'],
#     ['Jane','30','Los Angeles']
# ]
#
# path='output.csv'

# #write
# with open(path, 'w', newline='') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerows(data)
#
# #Read
# with open(path,'r') as file:
#     csv_reader = csv.reader(file)
#     for row in csv_reader:
#         print(row)


# with open('output.csv','a',encoding='utf-8-sig') as file:
#     file.write('姓名,年齡,地點')
#     file.write('\nNB,18,ABC')

# pip3 install python-docx
##WORD

# from docx import Document
# #創建一個新的文檔
# doc = Document()
# #添加標題
# doc.add_heading('示範檔案',level=1)
# #添加段落
# doc.add_paragraph('使用 docx 所建立的word')
# #保存文檔
# doc.save('示範檔案.docx')

### https://python-docx.readthedocs.io/en/latest/

# from docx import Document
# from docx.shared import Inches
#
# document = Document()
#
# document.add_heading('Document Title', 0)
#
# p = document.add_paragraph('A plain paragraph having some ')
# p.add_run('bold').bold = True
# p.add_run(' and some ')
# p.add_run('italic.').italic = True
#
# document.add_heading('Heading, level 1', level=1)
# document.add_paragraph('Intense quote', style='Intense Quote')
#
# document.add_paragraph(
#     'first item in unordered list', style='List Bullet'
# )
# document.add_paragraph(
#     'first item in ordered list', style='List Number'
# )
#
# # document.add_picture('monty-truth.png', width=Inches(1.25))
#
# records = (
#     (3, '101', 'Spam'),
#     (7, '422', 'Eggs'),
#     (4, '631', 'Spam, spam, eggs, and spam')
# )
#
# table = document.add_table(rows=1, cols=3)
# hdr_cells = table.rows[0].cells
# hdr_cells[0].text = 'Qty'
# hdr_cells[1].text = 'Id'
# hdr_cells[2].text = 'Desc'
# for qty, id, desc in records:
#     row_cells = table.add_row().cells
#     row_cells[0].text = str(qty)
#     row_cells[1].text = id
#     row_cells[2].text = desc
#
# document.add_page_break()
#
# document.save('demo.docx')



# PDF
# pip3 install reportlab
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

#創建一個PDF文件

c=canvas.Canvas('Test.pdf',pagesize=letter)

pdfmetrics.registerFont(TTFont('kaiu','kaiu.ttf'))

#增加文件
c.setFont('kaiu',14)
c.drawString(100,750,'哈摟')

#增加圖形
c.setStrokeColorRGB(0.2,0.5,0.3) #設定邊框為綠色
c.rect(50,650,400,100,fill=0) #繪製矩形

#保存PDF文件
c.showPage()
c.save()



