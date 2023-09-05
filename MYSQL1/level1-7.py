import os
import json
import time
import pymysql
import uuid
import math
import minimalmodbus

from datetime import datetime

db_settings = {
    "host": '192.168.0.163',
    "port": 3306,
    "user": 'PLC',
    "password": '123123123',
    "db": "graphiccontrol",
    "charset": "utf8"
}
db = pymysql.connect(
    host='127.0.0.1', port=3306,
    user='PLC', password='123123123',
    db='graphiccontrol'
)
db.autocommit = True


def Show(avg1, avg2, avg3):
    print('{} {} {}'.format(avg1, avg2, avg3))


# def RS485_read(TmpAddress):
#     c = minimalmodbus.Instrument(port='com5', slaveaddress=1)
#     c.serial.baudrate = 9600
#     c.serial.bytesize = 7
#     c.serial.parity = 'E'
#     c.serial.stopbits = 1
#     c.serial.timeout = 1
#     c.mode = minimalmodbus.MODE_ASCII
#     c.clear_buffers_before_each_transaction = True
#     c.close_port_after_each_call = True
#     return c.read_bit(registeraddress=int(TmpAddress, 16), functioncode=2)


# while db.open:
#     with db.cursor() as cursor:
#         command = "SELECT * FROM `bit_cells`"
#         cursor.execute(command)
#         db.commit()
#         vals = cursor.fetchall()
#         TmpOccurTimeStamp = int(time.time())
#         TmpOccurDate = datetime.fromtimestamp(TmpOccurTimeStamp).strftime("%Y-%m-%d %H:%M:%S")
#         for n in vals:
#             command = "UPDATE `bit_cells` SET `NowValue` = %s,`updated_at` = %s WHERE `Guid` = %s"
#             cursor.execute(command, (RS485_read(n[2]), TmpOccurDate, n[0]))
#             db.commit()
#     print('Running... {}'.format(TmpOccurDate))
#     time.sleep(1)
# exit(0)


# s=c.write_single_coil(
#
#
#     bit_addr=int('503',16),
#     bit_value=False
# )
# print(s)
# def RS485_Write(TmpAddress,tmpx):
#     c = minimalmodbus.Instrument(port='com5', slaveaddress=1)
#     c.serial.baudrate = 9600
#     c.serial.bytesize = 7
#     c.serial.parity = 'E'
#     c.serial.stopbits = 1
#     c.serial.timeout = 1
#     c.mode = minimalmodbus.MODE_ASCII
#     c.clear_buffers_before_each_transaction = True
#     c.close_port_after_each_call = True
#     return c.write_bit(registeraddress=int(TmpAddress, 16),value=tmpx,functioncode=5)

# while db.open: #如果有連線 try保護機制
#   with db.cursor() as cursor:
#         command = "SELECT * FROM `bit_cells`"
#         cursor.execute(command)
#         db.commit()
#         vals = cursor.fetchall()
#         TmpOccurTimeStamp = int(time.time())
#         TmpOccurDate = datetime.fromtimestamp(TmpOccurTimeStamp).strftime("%Y-%m-%d %H:%M:%S")
#         for n in vals:
#             if int(n[4]) != 1:
#                 continue
#             if int(n[5]) == 99:
#                 continue
#
#             RS485_Write(n[2],n[5])
#             command = "UPDATE `bit_cells` SET `HandTrigger` = %s,`HandTriggerValue` = %s,`updated_at` WHERE `Guid` = %s"
#             cursor.execute(command, (99,99, TmpOccurDate, n[0]))
#             db.commit()
#   print('Running... {}'.format(TmpOccurDate))
#   time.sleep(1)
#   exit(0)

# 先讀後寫 level6 自己做法
# def RS485_read(TmpAddress):
#     c = minimalmodbus.Instrument(port='com5', slaveaddress=1)
#     c.serial.baudrate = 9600
#     c.serial.bytesize = 7
#     c.serial.parity = 'E'
#     c.serial.stopbits = 1
#     c.serial.timeout = 1
#     c.mode = minimalmodbus.MODE_ASCII
#     c.clear_buffers_before_each_transaction = True
#     c.close_port_after_each_call = True
#     return c.read_bit(registeraddress=int(TmpAddress, 16), functioncode=2)
#
#
# def RS485_Write(TmpAddress, tmpx):
#     c = minimalmodbus.Instrument(port='com5', slaveaddress=1)
#     c.serial.baudrate = 9600
#     c.serial.bytesize = 7
#     c.serial.parity = 'E'
#     c.serial.stopbits = 1
#     c.serial.timeout = 1
#     c.mode = minimalmodbus.MODE_ASCII
#     c.clear_buffers_before_each_transaction = True
#     c.close_port_after_each_call = True
#     return c.write_bit(registeraddress=int(TmpAddress, 16), value=tmpx, functioncode=5)
#
#
# while db.open:
#     with db.cursor() as cursor:
#         command = "SELECT * FROM `bit_cells`"
#         cursor.execute(command)
#         db.commit()
#         vals = cursor.fetchall()
#         TmpOccurTimeStamp = int(time.time())
#         TmpOccurDate = datetime.fromtimestamp(TmpOccurTimeStamp).strftime("%Y-%m-%d %H:%M:%S")
#         for n in vals:
#             command = "UPDATE `bit_cells` SET `NowValue` = %s,`updated_at` = %s WHERE `Guid` = %s"
#             cursor.execute(command, (RS485_read(n[2]), TmpOccurDate, n[0]))
#             db.commit()
#
#             if int(n[4]) != 1:
#                 continue
#             if int(n[5]) == 99:
#                 continue
#             RS485_Write(n[2], n[5])
#             asd = "UPDATE `bit_cells` SET `HandTrigger` = %s,`HandTriggerValue` = %s,`updated_at`=%s WHERE `Guid` = %s"
#             cursor.execute(asd, (99, 99, TmpOccurDate, n[0]))
#             db.commit()
#     print('Running... {}'.format(TmpOccurDate))
#     time.sleep(1)
# exit(0)
###level7

# class RS485:
#     def __init__(self, port, SlaveAddress):
#         self.minimalmodbus = minimalmodbus.Instrument(port=port, slaveaddress=SlaveAddress)
#         self.minimalmodbus.serial.baudrate = 9600
#         self.minimalmodbus.serial.bytesize = 7
#         self.minimalmodbus.serial.parity = 'E'
#         self.minimalmodbus.serial.stopbits = 1
#         self.minimalmodbus.serial.timeout = 1
#         self.minimalmodbus.mode = minimalmodbus.MODE_ASCII
#         self.minimalmodbus.clear_buffers_before_each_transaction = True
#         self.minimalmodbus.close_port_after_each_call = True
#
#     def Read_Bit(self, TmpAddress):
#         return self.minimalmodbus.read_bit(registeraddress=int(TmpAddress, 16), functioncode=2)
#
#     def Write_Bit(self, TmpAddress, TmpBool):
#         return self.minimalmodbus.write_bit(registeraddress=int(TmpAddress, 16), value=TmpBool, functioncode=5)
#
#     def Read_Register(self, TmpAddress):
#         return self.minimalmodbus.read_register(
#             registeraddress=int(TmpAddress, 16),
#             number_of_decimals=0,
#             functioncode=3,
#             signed=True
#         )
#
#
#     def Write_Register(self, TmpAddress,Tmpvalue):
#         return self.minimalmodbus.write_register(
#             registeraddress=int(TmpAddress, 16),
#             number_of_decimals=0,
#             functioncode=16,
#             value=Tmpvalue,
#             signed=True
#         )
#
# def Show(avg1, avg2, avg3):
#     print('{} {} {}'.format(avg1, avg2, avg3))


# TmpRS485 = RS485('COM5', 1)
# while db.open:
#     with db.cursor() as cursor:
#         command = "SELECT * FROM `v_words`"
#         cursor.execute(command)
#         db.commit()
#         vals = cursor.fetchall()
#         TmpOccurTimeStamp = int(time.time())
#         TmpOccurDate = datetime.fromtimestamp(TmpOccurTimeStamp).strftime("%Y-%m-%d %H:%M:%S")
#         for n in vals:
#             # Read
#             command = "UPDATE `v_words` SET `NowValue` = %s,`updated_at` = %s WHERE `Guid` = %s"
#             cursor.execute(command, (TmpRS485.Read_Register(TmpAddress=n[2]), TmpOccurDate, n[0]))
#             db.commit()
#     print('Running... {}'.format(TmpOccurDate))
# exit(0)

#level7
# TmpRS485 = RS485('COM5',1)
# while db.open:
#     with db.cursor() as cursor:
#         command = "SELECT * FROM `v_words`"
#         cursor.execute(command)
#         db.commit()
#         vals = cursor.fetchall()
#         TmpOccurTimeStamp = int(time.time())
#         TmpOccurDate = datetime.fromtimestamp(TmpOccurTimeStamp).strftime("%Y-%m-%d %H:%M:%S")
#         for n in vals:
#             # Read
#             command = "UPDATE `v_words` SET `NowValue` = %s,`updated_at` = %s WHERE `Guid` = %s"
#             cursor.execute(command, (TmpRS485.Read_Register(TmpAddress=n[2]), TmpOccurDate, n[0]))
#             db.commit()
#             #write
#             if int(n[4]) !=1:
#                 continue
#             if int(n[5]) ==99:
#                 continue
#             TmpRS485.Write_Register(TmpAddress=n[2], TmpValue=int(n[5]))
#             command = "UPDATE `v_words` SET `HandTrigger` = %s,`HandTriggerValue` = %s,`updated_at` = %s WHERE Guid = %s"
#             cursor.execute(command, (99, 99, TmpOccurDate, n[0]))
#             db.commit()
#     print('Running... {}'.format(TmpOccurDate))
#     time.sleep(1)
# exit(0)





