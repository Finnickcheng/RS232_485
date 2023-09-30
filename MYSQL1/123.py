from pyModbusTCP.client import ModbusClient     #PLC TCP/IP
from datetime import  datetime
import json
import pymysql                                  #MySQL
import time
#PLC TCP/IP
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
        # 讀出多筆Bits
        # -----------------------------
        s = c.read_coils(
            bit_addr=int(address, 16),
            bit_nb=20
        )
        return s
    except:
        print("PLC Connect Error!")
def PLCTCPWords(host, port, address):
    try:
        c = ModbusClient(
            host=host,
            port=port,
            auto_open=True,
            unit_id=1,
            timeout=1,
            debug=False
        )
        # 讀取16位寄存器
        s = c.read_holding_registers(
            reg_addr=int(address, 16),
            reg_nb=1
        )
        return s
    except:
        print("PLC Connect Error!")
start_time = time.time()
#MySQL
db = pymysql.connect(
    host="127.0.0.1", port=3306,#192.168.137.1為本機IP，3306為MySQL用
    user="PLC", password="123123123",
    db="testgraphiccontrol"
)
db.autocommit = True
#取回所有
ipandport = []
while True:
    ipandportlist = []
    loop = 0
    with db.cursor() as cursor:
        # 讀取SQL抓取ip以及port
        # ---------------------------------------------------------------------------------------------------
        command = "SELECT * FROM `machines` ORDER BY `Serial` ASC"
        cursor.execute(command)
        for machine in cursor.fetchall():
            collect = json.loads(machine[6])
            ipandport = [machine[3], collect["Port"], machine[0]]
            ipandportlist.append(ipandport)
        # 讀取SQL抓取ip
        # ---------------------------------------------------------------------------------------------------
        for tcp in ipandportlist:
            TmpOccurTimeStamp = int(time.time())
            TmpOccurDate = datetime.fromtimestamp(TmpOccurTimeStamp).strftime("%Y-%m-%d %H:%M:%S")
            #查看現有IP及PORT
            # print(tcp)
            # loop += 1
            # if loop == len(ipandportlist):
            #     print("------------------------------------")
            # 讀取PLC Coils寫入資料表
            # ---------------------------------------------------------------------------------------------------


            command = "SELECT * FROM `coils` WHERE `MachineGuid` = %s order by Serial;"
            cursor.execute(command,machine[0])
            theaddress_bit = list(cursor.fetchall())
            db.commit()
            print("Running......", TmpOccurDate)
            print(f"IP : {tcp[0]}, Port : {tcp[1]} Write Coils...\n")
            PLCStatus = PLCTCPBits(tcp[0], tcp[1], "0A00")
            for serial, data in enumerate(theaddress_bit):
                TmpOccurTimeStamp = int(time.time())
                TmpOccurDate = datetime.fromtimestamp(TmpOccurTimeStamp).strftime("%Y-%m-%d %H:%M:%S")
                # 更新資料
                try:

                    if str(PLCStatus[serial]) == "False":
                        statu = "0"
                    else:
                        statu = "1"
                    command = "UPDATE `coils` SET `Value` = %s , `updated_at` = %s WHERE `coils`.`Guid` = %s;"
                    cursor.execute(command, (statu, TmpOccurDate, data[0]))
                    db.commit()
                except:
                    print(f"PLC Connect Error!, {TmpOccurDate}\n")
                    successornot = "Fail!"
                    break
        # 讀取PLC Coils寫入資料表
        # ---------------------------------------------------------------------------------------------------
            command = "SELECT * FROM `registers` WHERE `MachineGuid` = %s order by Serial;"
            cursor.execute(command, machine[0])
            theaddress_word = list(cursor.fetchall())
            db.commit()
            print(f"IP : {tcp[0]}, Port : {tcp[1]} Write Words...\n")
            for address_2 in theaddress_word:
                TmpOccurTimeStamp = int(time.time())
                TmpOccurDate = datetime.fromtimestamp(TmpOccurTimeStamp).strftime("%Y-%m-%d %H:%M:%S")
                try:
                    word = str(PLCTCPWords(tcp[0], tcp[1], address_2[4])[0])
                    command = "UPDATE `registers` SET `Value` = %s , `updated_at` = %s WHERE `registers`.`Guid` = %s;"
                    cursor.execute(command, (word, TmpOccurDate, address_2[0]))
                    db.commit()
                except:
                    print(f"PLC Connect Error!, {TmpOccurDate}\n")
                    break
            # db.close()