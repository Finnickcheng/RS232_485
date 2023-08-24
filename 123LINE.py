import json

import requests

Message = '0933916108'
LineToken = 'VJP8K1yPEiUZjatYCQJZq6pBtkWj916ocMhfKBdL69S'
n=requests.post('https://notify-api.line.me/api/notify',
              params={"message": Message}, #params=body 表單
              headers={  #標頭
                  "Authorization": "Bearer " + LineToken,
                  "content-Type": "application/x-www-form-urlencoded"}
              )
print(n.text)
print(type(n.text))
print(json.loads(n.text))
print(type(json.loads(n.text)))
print(json.loads(n.text)['status'])