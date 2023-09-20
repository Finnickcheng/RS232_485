import os
import json
import time
import pymysql
import uuid
import math
import minimalmodbus
from pyModbusTCP.client import ModbusClient
from datetime import datetime
def PLCTCPBits(host,port,address):
    try:
        c=ModbusClient(
            host=host,
            port=port,
            auto_open=True,
            unit_id=1,
            timeout=1,
            debug=False
        )
        s = c.read_coils(
            bit_addr=int(address, 16),
            bit_nb=20
        )

        return s
    except:
        print('connect error')
def PLCTCPword(host,port,address):
    try:
        c=ModbusClient(
            host=host,
            port=port,
            auto_open=True,
            unit_id=1,
            timeout=1,
            debug=False
        )
        x = c.read_holding_registers(
            reg_addr=int(address, 16),
            reg_nb=100
        )
        return x
    except:
        print('connect error')
def unsigned_16(asd,agv_decimal):
    n=int(agv_decimal)
    if n<0:
        n=asd._16bits +n
    return n
def signed_16(asd,agv_decimal):
    n=int(agv_decimal)
    if n>32767:
        n=n-asd._16Bits
    return n
#16Bits=65536
start_time = time.time()
db = pymysql.connect(
host='127.0.0.1', port=3306,
user='PLC', password='123123123',
db='testgraphiccontrol'
)

db.autocommit = True
Tmplist=[]
while db.open:
    TmpArray = []
    # 讀取SQL抓取ip以及port
    # ---------------------------------------------------------------------------------------------------
    with db.cursor() as cursor:
        command="SELECT * FROM `machines` ORDER BY `Serial`ASC;"
        cursor.execute(command)
        db.commit()
        vals = cursor.fetchall()
        for machine in vals:
            collect=json.loads(n[6])
            Tmplist=machine[n[3],collect["port"],machine[0]]
            TmpArray.append(Tmplist)




        command="SELECT * FROM `coils` WHERE `MachineGuid`='e19aec11-9b51-4d01-b877-f38b33495414' ORDER BY `Serial` asc;"
        cursor.execute(command)
        db.commit()
        vals = cursor.fetchall()
        TmpOccurTimeStamp = int(time.time())
        TmpOccurDate = datetime.fromtimestamp(TmpOccurTimeStamp).strftime("%Y-%m-%d %H:%M:%S")
        # TmpReadCoils=ct.read
        # CommentTitle=''
        # CommentValue=''
        # for key , n in enumerate(vals):
        #     tmp = json.loads(n[7])
        #     CommentTitle=tmp['Comment'] + ','
        #     tmpx=tmp['Value']
        #     tmpX= '0'
        #     if TmpReadCoils[key]:
        #         tmpX ='1'
        #     CommentValue += tmpX +','
        for n in vals:
            tmp=json.loads(n[7])
            tmp1=int(tmp["Value"])
            tmp2=int(tmp["Comment"])
            tmp3=int(tmp['Status'])
            if tmp1 == 1:
              print('TRUE')
            command = "UPDATE `coils` SET `Status`=%s,`value` = %s,`updated_at` = %s WHERE `Guid` = %s"
            cursor.execute(command, (9,tmp1, TmpOccurDate,n[0]))
            db.commit()
        # CommentTitle = CommentTitle[:-1]
        # CommentValue = CommentValue[:-1]
        # 'value':CommentValue



        command1="SELECT * FROM `registers` WHERE `MachineGuid`='e19aec11-9b51-4d01-b877-f38b33495414'AND`IsEnable`=1 ORDER BY `Serial`ASC;"
        cursor.execute(command1)
        db.commit()
        asd = cursor.fetchall()
        for x in asd:
            print(x)
        # Update registers演算
        #     command1 = "UPDATE `registers` SET `value` = %s,`updated_at` = %s WHERE `Guid` = %s"
        #     cursor.execute(command1, (x['value'], TmpOccurDate,x['RegisterGuid']))
        #     db.commit()


    time.sleep(1)
    print('Running... {}'.format(TmpOccurDate))

exit(0)
end_time=time.time()