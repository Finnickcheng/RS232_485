import requests
# Url = 'https://{Domain}/API21/HTTP/SendSMS.ashx'.format(Domain='api.e8d.tw')
# tmp= requests.post(Url, data={
#     'UID':'0972153032',
#     'PWD':'~!QAZ2wsx',
#     'SB':'',
#     'MSG':'-400$'.encode('utf-8'),
#     'DEST':'0972153032,0937950891,0971816355,0933916108',
#     'ST':'',
#     'RETRYTIME':1400
#      },headers={}, timeout=5)
# print(tmp.text)
#550.00,4,4,0,50419075-9858-4d0f-a4ba-d793a787472c

# Url = 'https://{DoMain}/API21/HTTP/GetDeliveryStatus.ashx'.format(DoMain='api.e8d.tw')
# tmp = requests.post(Url, data={
#     'UID': '0972153032',
#     'PWD': '~!QAZ2wsx',
#     'BID': '6a8c8ad1-f7c3-42e9-80b1-2f605ff56cc6',
#     'PNO': 1,
#     'RESPFORMAT': 1
# }, headers={}, timeout=5)
# print(tmp.text)  ###確認發送的人有沒有收到

Url = 'https://{DoMain}/API21/HTTP/GetCredit.ashx'.format(DoMain='api.e8d.tw')  #網站最後一個檔案 GetCredit吃的參數
tmp = requests.post(Url, data={
    'UID': '0972153032',
    'PWD': '~!QAZ2wsx',
}, headers={}, timeout=5) #### 吃的參數
print(tmp.text)  #### 查看餘額