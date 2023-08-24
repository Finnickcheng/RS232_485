import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header

messege = MIMEMultipart()


def UploadFileToByte(path, Name):
    with open('{}/{}'.format(path, Name), "rb") as file:
        part = MIMEApplication(file.read(), Name=Name)
        part['content-Disposition'] = 'attachment; filename={name}'.format(name=Name)  # 名稱定義
    return part


messege["Subject"] = Header('Subject', 'utf-8')  # 竄寫郵件標題
messege["From"] = Header('FromName', 'utf-8')  # 寄件者
messege["To"] = Header('ToName', 'utf-8')  # 收件者

# messege["Cc"]='?@gmail.com,?@gmail.com'#副本收件人1,副本收件人2

messege.attach(MIMEText('EEEEE', 'plain', 'utf-8'))  # 文字呈現
# 第一變數放置:資料來源
# 第二變數放置:資料來源類型
# 第三變數放置:格式


# TestHtml = """_____""" #網頁呈現
# messege.attach(MIMEText(TestHtml,"html","utf-8"))
#
tmp = [['upload', '12.doc'], ['upload', 'ASCII字元表.docx'], ['upload', '簡報2.pptx']]
for n in range(0, len(tmp)):
    messege.attach(UploadFileToByte(tmp[n][0], tmp[n][1]))  # 副件檔案

######################################

msg = messege.as_string()  # 將MSG將Text轉乘str
smtp = smtplib.SMTP('smtp.gmail.com', 587)  # smtp伺服器名稱 587:PORT
smtp.ehlo()
smtp.starttls()
smtp.login('finnick37@gmail.com', 'jinznqzaasdbwqtk')
from_addr = 'finnick37@gmail.com'
to_addr = 'finnick37@gmail.com'
status = smtp.sendmail(from_addr, to_addr, msg)
# 加密文件,避免私密信息被截取
DoneStatus = False
if status == {}:
    DoneStatus = True
    smtp.quit()
print(DoneStatus)
