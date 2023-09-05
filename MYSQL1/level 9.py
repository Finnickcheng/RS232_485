import os
import json
import time
import pymysql
import uuid
import math
import minimalmodbus

from datetime import datetime

db_settings = {
    "host": '127.0.0.1',
    "port": 3306,
    "user": 'PLC',
    "password": '123123123',
    "db": "graphiccontrol",
    "charset": "utf8"
}

con = pymysql.connect(**db_settings)
con.autocommit = True


def Show(avg1, avg2, avg3):
    print('{} {} {}'.format(avg1, avg2, avg3))


class RS485:
    def __init__(self, port, SlaveAddress):
        self.minimalmodbus = minimalmodbus.Instrument(port=port, slaveaddress=SlaveAddress)
        self.minimalmodbus.serial.baudrate = 9600
        self.minimalmodbus.serial.bytesize = 7
        self.minimalmodbus.serial.parity = 'E'
        self.minimalmodbus.serial.stopbits = 1
        self.minimalmodbus.serial.timeout = 1
        self.minimalmodbus.mode = minimalmodbus.MODE_ASCII
        self.minimalmodbus.clear_buffers_before_each_transaction = True
        self.minimalmodbus.close_port_after_each_call = True

    def Read_Bit(self, TmpAddress):
        return self.minimalmodbus.read_bit(registeraddress=int(TmpAddress, 16), functioncode=2)

    def Write_Bit(self, TmpAddress, TmpBool):
        return self.minimalmodbus.write_bit(registeraddress=int(TmpAddress, 16), value=TmpBool, functioncode=5)

    def Read_Register(self, TmpAddress):
        return self.minimalmodbus.read_register(
            registeraddress=int(TmpAddress, 16),
            number_of_decimals=0,  # 1 2 3 4
            functioncode=3,
            signed=True
        )

    def Write_Register(self, TmpAddress, TmpValue):
        return self.minimalmodbus.write_register(
            registeraddress=int(TmpAddress, 16),
            value=TmpValue,
            number_of_decimals=0,  # 1 2 3 4
            functioncode=16,
            signed=True
        )


TmpRS485 = RS485('COM5', 1)
while con.open:
    TmpArray = {}
    with con.cursor() as cursor:
        command = "SELECT * FROM `v_words`"
        cursor.execute(command)
        con.commit()
        vals = cursor.fetchall()
        TmpOccurTimeStamp = int(time.time())
        TmpOccurDate = datetime.fromtimestamp(TmpOccurTimeStamp).strftime("%Y-%m-%d %H:%M:%S")
        for n in vals:
            TmpNotifyCollect = json.loads(n[8])
            Tmpvalue = TmpRS485.Read_Register(TmpAddress=n[2])
            TmpArray[n[2]] = {
                "GUID": n[0],  # 唯一碼
                "Name": n[1],  # 元件名稱
                "Address": n[2],  # 元件地址
                "NowStatus": n[3],
                'Value': int(Tmpvalue), 'Type': 'Word'

            }

        command = "SELECT * FROM `chart_collects`"
        cursor.execute(command)
        con.commit()
        for key1, value1 in enumerate(cursor.fetchall()):
            TmpOccurTimeStamp = int(time.time())
            TmpOccurDate = datetime.fromtimestamp(TmpOccurTimeStamp).strftime("%Y-%m-%d %H:%M:%S")
            TmpGuid = value1[0]
            TmpAddress = value1[1]
            NewChartValue = {}
            for key2, value2 in enumerate(TmpAddress.split(',')):
                NewChartValue[value2] = {
                    'Name': TmpArray[value2]['Name'],
                    'Address': TmpArray[value2]['Address'],
                    'Value': 0,
                }
                if not TmpArray.get(value2) is None:
                    NewChartValue[value2] = {
                        'Name': TmpArray[value2]['Name'],
                        'Address': TmpArray[value2]['Address'],
                        'Value': TmpArray[value2]['Value'],
                    }
            command = "INSERT INTO `chart_values`(`Guid`, `ChartCollectsGuid`, `TimeStamp`, `Collect`, `created_at`, `updated_at`)VALUES(%s, %s, %s, %s, %s, %s)"
            cursor.execute(command, (
                str(uuid.uuid4()), TmpGuid, TmpOccurTimeStamp, json.dumps(NewChartValue), TmpOccurDate, TmpOccurDate))
            con.commit()
    print('Running... {}'.format(TmpOccurDate))
