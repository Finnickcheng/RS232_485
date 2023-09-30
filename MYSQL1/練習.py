import os
import json
import time
import pymysql
import uuid
import math
import minimalmodbus
from pyModbusTCP.client import ModbusClient
from datetime import datetime


def PLCTCPBits(host, port, address):
    try:
        c = ModbusClient(
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


def PLCTCPword(host, port, address):
    try:
        c = ModbusClient(
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


def unsigned_16(agv_decimal):
    n = int(agv_decimal)
    if n < 0:
        n = 65536 + n
    return n


def signed_16(agv_decimal):
    n = int(agv_decimal)
    if n > 32767:
        n = n - 65536
    return n


# 16Bits=65536
start_time = time.time()
db = pymysql.connect(
    host='127.0.0.1', port=3306,
    user='PLC', password='123123123',
    db='testgraphiccontrol'
)

db.autocommit = True
Tmplist = []
while db.open:
    TmpArray = []

    # 讀取SQL抓取ip以及port
    with db.cursor() as cursor:

        command = "SELECT * FROM `machines` ORDER BY `Serial`ASC;"
        cursor.execute(command)
        db.commit()
        for machine in cursor.fetchall():
            collect = json.loads(machine[6])
            Tmplist = [machine[3], collect["Port"], machine[0]]
            TmpArray.append(Tmplist)
        # 抓IP 讀PLC寫入資料表
        for tcp in TmpArray:
            TmpOccurTimeStamp = int(time.time())
            TmpOccurDate = datetime.fromtimestamp(TmpOccurTimeStamp).strftime("%Y-%m-%d %H:%M:%S")

            command = "SELECT * FROM `coils` WHERE `MachineGuid` = %s order by Serial;"
            cursor.execute(command, machine[0])
            X = list(cursor.fetchall())
            db.commit()

            print('Running... {}'.format(TmpOccurDate))
            print('Ip:{},Port:{}....coil'.format(tcp[0], tcp[1]))

            PlCstatus = PLCTCPBits(tcp[0], tcp[1], "0A00")
            for key, n in enumerate(X):
                TmpOccurTimeStamp = int(time.time())
                TmpOccurDate = datetime.fromtimestamp(TmpOccurTimeStamp).strftime("%Y-%m-%d %H:%M:%S")

                # 更新資料
                try:
                    if str(PlCstatus[key]) == "False":
                        tmp = "0"
                    else:
                        tmp = "1"
                    command = "UPDATE `coils` SET `Value` = %s , `updated_at` = %s WHERE `coils`.`Guid` = %s;"
                    cursor.execute(command, (tmp, TmpOccurDate, n[0]))
                    db.commit()
                except:
                    print(f" Connect Error!, {TmpOccurDate}\n")

                    break

            # 讀取PLC registers 寫入資料表

            command = "SELECT * FROM `registers` WHERE `MachineGuid` = %s order by Serial asc;"
            cursor.execute(command, machine[0])
            vals = cursor.fetchall()
            db.commit()
            vals_total_len=len(vals)
            print('IP:{},Port:{}....word'.format(tcp[0], tcp[1]))
            Tmpreadvals={}
            if vals_total_len !=0:

                Tmpanyindex=0
                while Tmpanyindex >=0:
                    Address=vals[Tmpanyindex == 100][4]
                    if Tmpanyindex == 0:
                        Address =vals[0][4]
                    if vals_total_len < 100:

                        Tmpreadvals = {
                             'MachineName':address[3],
                             'MachineGuid':address[2],
                             'Type':'Register',
                             'Address':Address,
                             'Length':vals_total_len,
                             'Time':10,
                             'OverTimes':0
                        }
                    if len(Tmpreadvals) != 0:
                        Arrayregister += Tmpreadvals
                        Tmpanyindex = -1
                        continue
                    else:
                        Arrayregister = []
                        Tmpanyindex = -1
                        continue

                for asd in vals:
                    Tmpreadvals = {
                        'MachineName': asd[3],
                        'MachineGuid': asd[2],
                        'Type': 'Register',
                        'Address': Address,
                        'Length': 100,
                        'Times': 10,
                        'OverTimes': 0
                    }

                    if len(Tmpreadvals) != 0:
                        Arrayregister += Tmpreadvals
                        vals_total_len -= 100
                        Tmpanyindex += 1
                    else:
                        Arrayregister=[]
                        Tmpanyindex = -1



            for address in vals:

                try:
                    word = signed_16(PLCTCPword(tcp[0], tcp[1], address[4])[0])
                    command = "UPDATE `registers` SET `Value` = %s , `updated_at` = %s WHERE `registers`.`Guid` = %s;"
                    cursor.execute(command, (word, TmpOccurDate, address[0]))
                    # db.commit()
                    # print('{}'.format(word))

                    db.commit()
                except:
                    print(f"Connect Error!, {TmpOccurDate}\n")

                    break
        time.sleep(20)

exit(0)
