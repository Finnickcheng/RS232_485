import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header

messege = MIMEMultipart()



# def UploadFileToByte(Name=):
#     with open('upload/ASCII字元表.docx',"rb") as file:
#         part = MIMEApplication(file.read(), Name=Name)
#         part['content-Disposition'] = 'attachment; filename={name}'.format(name=Name)  # 名稱定義
#     return part

# TmpCC=['?@','?@gmail.com'] #CC

messege["Subject"] = Header('Subject', 'utf-8')  # 竄寫郵件標題
messege["From"] = Header('FromName', 'utf-8')  # 寄件者
messege["To"] = Header('ToName', 'utf-8')  # 收件者

# messege["Cc"]='?@gmail.com,?@gmail.com'#副本收件人1,副本收件人2

messege.attach(MIMEText('Words', 'plain', 'utf-8'))  # 文字呈現
# 第一變數放置:資料來源
# 第二變數放置:資料來源類型
# 第三變數放置:格式


TestHtml = """
<!DOCTYPE html>
<html>
<body>

<h2>HTML Table</h2>

<h2>Absolute URLs</h2>
<p><a href="https://www.w3.org/">W3C</a></p>
<p><a href="https://www.google.com/">Google</a></p>

<h2>Relative URLs</h2>
<p><a href="html_images.asp">HTML Images</a></p>
<p><a href="/css/default.asp">CSS Tutorial</a></p>

<svg width="100" height="100">
  <circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" />
  Sorry, your browser does not support inline SVG.
</svg>

<p>Here is a quote from WWF's website:</p>
<blockquote cite="http://www.worldwildlife.org/who/index.html">
For 50 years, WWF has been protecting the future of nature. The world's leading conservation organization, WWF works in 100 countries and is supported by 1.2 million members in the United States and close to 5 million globally.
</blockquote>


<table style="font-family: arial, sans-serif;border-collapse: collapse;width: 100%;">
  <tr>
    <th style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Company</th>
    <th style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Contact</th>
    <th style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Country</th>
  </tr>
  <tr style="background-color: #dddddd;">
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Alfreds Futterkiste</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;"><span style="font-size:100px">🐰🤞🤖👽🕜🕝🀄🔞</span></td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Germany</td>
  </tr>
  <tr>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Centro comercial Moctezuma</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Francisco Chang</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Mexico</td>
  </tr>
  <tr style="background-color: #dddddd;">
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Ernst Handel</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Roland Mendel</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Austria</td>
  </tr>
  <tr>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Island Trading</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Helen Bennett</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">UK</td>
  </tr>
  <tr style="background-color: #dddddd;">
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Laughing Bacchus Winecellars</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Yoshi Tannamuri</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Canada</td>
  </tr>
  <tr>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Magazzini Alimentari Riuniti</td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;"><img src="https://www.w3schools.com/html/img_girl.jpg" alt="Girl in a jacket" style="width:100%;height:500px;"></td>
    <td style="border: 1px solid #dddddd;text-align: left;padding: 8px;">Italy</td>
  </tr>
</table>

</body>
</html>

"""
#網頁呈現
messege.attach(MIMEText(TestHtml,"html","utf-8"))

# messege.attach(UploadFileToByte()) #副件檔案


######################################

msg = messege.as_string()  # 將MSG將Text轉乘str
smtp = smtplib.SMTP('smtp.gmail.com', 587)  # smtp伺服器名稱 587:PORT
smtp.ehlo()
smtp.starttls()
smtp.login('finnick37@gmail.com', 'jinznqzaasdbwqtk')
from_addr = 'finnick37@gmail.com'
to_addr = 'finnick37@gmail.com'
status = smtp.sendmail(from_addr, to_addr, msg)
# status = smtp.sendmail(from_addr, (to_addr+TmpCC), msg)
#  加密文件,避免私密信息被截取
DoneStatus = False
if status == {}:
    DoneStatus = True
    smtp.quit()
print(DoneStatus)
