# pip3 install PyMySQL
import json
import uuid
import pymysql

from datetime import datetime
import time

Int_TimeStamp = int(time.time())
TmpDate = datetime.fromtimestamp(Int_TimeStamp).strftime('%Y-%m-%d %H:%M:%S')


db = pymysql.connect(
    host='127.0.0.1', port=3306,
    user='PLC', password='123123123',
    db='graphiccontrol'
)
db.autocommit = True

# 用pythom建立PHPmyadmin的檔案

# with db.cursor() as cursor:
#     sql = """
#     CREATE TABLE `graphiccontrol`.`User` (
# 	 `Guid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL ,
# 	 `Name` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL ,
# 	 `Age` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL ,
# 	 `Postal_Guid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL ,
# 	 `City_Guid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL ,
# 	 PRIMARY KEY (`Guid`),
# 	 INDEX (`Name`),
# 	 INDEX (`Age`),
# 	 UNIQUE (`Postal_Guid`),
# 	 UNIQUE (`City_Guid`)
#    ) ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;
#
#     """
#     cursor.execute(sql)
#     db.close()

##建GUID

# with db.cursor() as cursor:
#     sql="""
#     INSERT INTO `User`(`Guid`, `Name`, `Age`, `Postal_Guid`, `City_Guid`) VALUES
#     ('f3546da5-e6ac-472a-94e9-cd5ea10a6762','B1','16','320','中壢')
#
#     """
#     try:
#         cursor.execute(sql)
#         db.commit()
#     except:
#         db.rollback()
#     db.close()


# with db.cursor() as cursor:
#     sql = "INSERT INTO `User`(`Guid`, `Name`, `Age`, `Postal_Guid`, `City_Guid`) VALUES(%s,%s,%s,%s,%s)"
#
#     try:
#
#           # ['a','b','c','d','e'],['a1','b1','c1','d1','e1'],['a2','b2','c2','d2','e2']]:
#           #  cursor.execute(sql, (n[0],n[1],n[2],n[3],n[4]))
#         cursor.execute(sql, ('1', '2', '3', '4', '5'))  ##方便
#         db.commit()
#     except:
#       print('1')
#         db.rollback()
#      db.close()


# with db.cursor() as cursor:
#     command='SELECT*FROM `user` order by name desc '
#     cursor.execute(command)
#     db.commit()
#     vals=cursor.fetchone()  #fetchone 取回一筆 fetchall取回多筆
#     print(vals)
#
#     db.close()

# tmp = []
# tmp1 = 5
# for n in range(5):
#     tmp.append([str(uuid.uuid4()), tmp1 * n, tmp1 * n + 1, tmp1 * n + 2])
#     tmp1 += 1
# with db.cursor() as cursor:
#      sql = "INSERT INTO `User`(`Guid`, `Name`, `Age`, `Postal_Guid`, `City_Guid`) VALUES(%s,%s,%s,%s,%s)"
#      try:
#         for n in tmp:
#             cursor.execute(sql, (n[0],n[1],n[2],n[3],n[4]))
#             db.commit()
#      except:
#          db.rollback()
#      db.close()

# with db.cursor() as cursor:
#     command = "SELECT * FROM `user` where `Name` <=15"
#     cursor.execute(command)
#     db.commit()
#     for n in cursor.fetchall():
#         print(n)
#
#     db.close()

# with db.cursor() as cursor:
#     SQL = """
#         CREATE TABLE `graphiccontrol`.`ITOrder` (
#         `Guid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '唯一碼',
#         `Name` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '姓名',
#         `Price` INT UNSIGNED NOT NULL COMMENT '價錢',
#         `weight` INT UNSIGNED NOT NULL COMMENT '重量',
#         PRIMARY KEY (`Guid`),
#         INDEX (`Name`),
#         INDEX (`Price`),
#         INDEX (`weight`)
#     ) ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;
#     """
#     cursor.execute(SQL)
#
#
# tmp = []
# TmpI = 5
# for n in range(20):
#     tmp.append([str(uuid.uuid4()), 'd{}'.format(n), n * 5 + 1, n * 5 + 2])
#     TmpI += 1
#
# with db.cursor() as cursor:
#     SQL = "INSERT INTO `ITOrder` (`Guid`, `Name`,`Price`,`weight`) values (%s, %s , %s, %s)"
#     for n in tmp:
#         cursor.execute(SQL, (n[0], n[1], int(n[2]), int(n[3])))
#         db.commit()

# with db.cursor() as cursor:
#     # SQL = "select * from `ITOrder` order by Price desc"
#     SQL = "select * from `ITOrder` where Price < 46"
#     # SQL = "select * from `ITOrder` where `Price` < 46 order by `Price` desc"
#     # SQL = "select * from `ITOrder` where (`Price` < 46) and (`weight` > 17)"
#     # SQL = "select * from `ITOrder` where (`Price` < 46) and (`weight` > 17) order by `Price` desc"
#     cursor.execute(SQL)
#     TmpX = cursor.fetchall()
#     print('(`Guid`, `Name`,`Price`,`weight`)')
#     for n in TmpX:
#         print(n)
# exit(0)

# update更新.1
# with db.cursor() as cursor:
#     command = " UPDATE `itorder` SET `Name`='H2' where `Guid` ='00e594e0-fff2-4d58-8631-be61de2ec8bf'"
#
#     cursor.execute(command)
#     db.commit()
#     db.close()
#
 # update更新.2
# with db.cursor() as cursor:
#     command=" UPDATE `itorder` SET `Name`= 'H3' where `Guid`=%s"
#     cursor.execute(command,'14f83984-fa4d-4d28-bae1-1db13c1f957c')
#     db.commit()
#     db.close()
#
# # #刪除delete
# with db.cursor() as cursor:
#     command=" Delete FROM `itorder` where `Guid` = %s"
#     cursor.execute(command,'00e594e0-fff2-4d58-8631-be61de2ec8bf')
#     db.commit()
#     db.close()

# with db.cursor() as cursor:
#     sql = """
#         CREATE TABLE `graphiccontrol`.`bit_cells`(
#         `Guid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '唯一碼Name',
#         `Name` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '元件名稱',
#         `Address` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '元件地址',
#         `NowValue` TINYINT NOT NULL COMMENT '當下數值',
#         `HandTrigger` TINYINT NOT NULL DEFAULT '99' COMMENT '有人為操控時狀態',
#         `HandTriggerValue` TINYINT NOT NULL DEFAULT '99' COMMENT '人為操控切換後數值',
#         `CollectData` LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '數據集合',
#         `NotifyStatus` TINYINT NOT NULL COMMENT '是否警示',
#         `NotifyCollectData` LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '數據集合',
#         `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#         `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#         PRIMARY KEY (`Guid`(40)),
#         INDEX (`Name`(40)),
#         INDEX (`Address`(40)),
#         INDEX (`NowValue`),
#         INDEX (`HandTrigger`),
#         INDEX (`HandTriggerValue`)
#     ) ENGINE=InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;
#     """
#
#     cursor.execute(sql)
#     db.close()

# with db.cursor() as cursor:
#     sql = """
#     INSERT INTO `bit_cells`(
#     `Guid`, `Name`, `Address`, `NowValue`, `HandTrigger`, `HandTriggerValue`,
#     `CollectData`, `NotifyStatus`, `NotifyCollectData`, `created_at`, `updated_at`)
#
#     VALUES(
#         '06fea5f1-5426-4470-b05b-30f3307c0639', 'Y0', '500',
#         0, 99, 99, '{}', 0,
#         '{\"NotifyType\": 0, \"NotifyPlatFrom\": 0, \"NotifyTimeStamp\": 0, \"NotifyDateTime\": 0}',
#         '2023-05-16 05:18:26', '2023-07-11 16:16:16');
#     """
#     try:
#         cursor.execute(sql)
#         db.commit()
#     except:
#         print('1')
#         db.rollback()
#     db.close()




# with db.cursor() as cursor:
#     sql = """
#     CREATE TABLE `graphiccontrol`.`v_strings`(
#     `Guid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '唯一碼Name',
#     `Name` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '元件名稱',
#     `Address` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '元件地址',
#     `NowValue` TINYINT NOT NULL COMMENT '當下數值',
#     `HandTrigger` TINYINT NOT NULL DEFAULT '99' COMMENT '有人為操控時狀態',
#     `HandTriggerValue` TINYINT NOT NULL DEFAULT '99' COMMENT '人為操控切換後數值',
#     `CollectData` LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '數據集合',
#     `NotifyStatus` TINYINT NOT NULL COMMENT '是否警示',
#     `NotifyCollectData` LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '數據集合',
#     `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     PRIMARY KEY (`Guid`(40)),
#     INDEX (`Name`(40)),
#     INDEX (`Address`(40)),
#     INDEX (`NowValue`),
#     INDEX (`HandTrigger`),
#     INDEX (`HandTriggerValue`)
#     ) ENGINE=InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;
#     """
#     cursor.execute(sql)
#     db.close()

# with db.cursor() as cursor:
#     sql = """
#     INSERT INTO `v_strings`(
#     `Guid`, `Name`, `Address`, `NowValue`, `HandTrigger`, `HandTriggerValue`,
#     `CollectData`, `NotifyStatus`, `NotifyCollectData`, `created_at`, `updated_at`)
#
#
#     VALUES (
#     '75253ca3-378b-479d-afb6-3f6152f5a3a4',
#     'D2006','17D6','0',99,'99',
#     '{\"WordType\":\"String\",\"SignedType\":true,\"NumberOfRegisters\":1,\"MaxValue\":0,\"MinValue\":0,\"HLValueConvert\":0}',
#     0,'{\"NotifyPlatFrom\": 0, \"NotifyTimeStamp\": 0, \"NotifyDateTime\": 0}',
#     '2023-05-16 05:35:15','2023-07-11 16:16:32'
#     """
#     try:
#         cursor.execute(sql)
#         db.commit()
#     except:
#         print('1')
#         db.rollback()
#     db.close()

# with db.cursor() as cursor:
#     sql = """
#     CREATE TABLE `graphiccontrol`.`v_words`(
#     `Guid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '唯一碼Name',
#     `Name` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '元件名稱',
#     `Address` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '元件地址',
#     `NowValue` TINYINT NOT NULL COMMENT '當下數值',
#     `HandTrigger` TINYINT NOT NULL DEFAULT '99' COMMENT '有人為操控時狀態',
#     `HandTriggerValue` TINYINT NOT NULL DEFAULT '99' COMMENT '人為操控切換後數值',
#     `CollectData` LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '數據集合',
#     `NotifyStatus` TINYINT NOT NULL COMMENT '是否警示',
#     `NotifyCollectData` LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '數據集合',
#     `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     PRIMARY KEY (`Guid`(40)),
#     INDEX (`Name`(40)),
#     INDEX (`Address`(40)),
#     INDEX (`NowValue`),
#     INDEX (`HandTrigger`),
#     INDEX (`HandTriggerValue`)
#     ) ENGINE=InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;
#     """
#     cursor.execute(sql)
#     db.close()

# with db.cursor() as cursor:
#     sql = """
#     INSERT INTO `v_words`(
#     `Guid`, `Name`, `Address`, `NowValue`, `HandTrigger`, `HandTriggerValue`,
#     `CollectData`, `NotifyStatus`, `NotifyCollectData`, `created_at`, `updated_at`)
#
#
#     VALUES (
#     '5ecf9959-8327-4e1f-b23d-26b682ea9466',
#     'D2000','17D0','0',99,'99',
#     '{\"WordType\":\"Word\",\"SignedType\":true,\"NumberOfDecimals\":0,\"MaxValue\":0,\"MinValue\":0,\"HLValueConvert\":0}',
#     0,
#     '{\"NotifyPlatFrom\": 2, \"NotifyTimeStamp\": 1685327881, \"NotifyDateTime\": \"2023-05-29 10:38:01\"}',
#     '2023-05-16 05:31:07','2023-07-11 16:16:27'
# )
#     """
#     try:
#         cursor.execute(sql)
#         db.commit()
#     except:
#         print('1')
#         db.rollback()
#     db.close()

# with db.cursor() as cursor:
#     sql = """
#     CREATE TABLE `graphiccontrol`.`chart_collects`(
#     `Guid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '唯一碼',
#     `Address` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '元件地址集合',
#     `Data` LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '數據集合',
#     `Collect` LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '參數集合',
#     `Remark` TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '備注',
#     `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     PRIMARY KEY (`Guid`(40))
# ) ENGINE=InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;
#     """
#     cursor.execute(sql)
#     db.close()


# with db.cursor() as cursor:
#     sql = """
#     INSERT INTO `chart_collects` (`Guid`, `Address`, `Data`, `Collect`, `Remark`, `created_at`, `updated_at`) VALUES
#     ('130e6ad1-6d02-4b95-a9dc-3413ebe47919','17E8,17E9', '{}', '{}', '折線圖', '2023-05-17 01:47:39', '2023-05-29 03:06:54'),
#     ('eb0f27a7-1384-4ad4-a0c1-230dcf93b8df','17E5,17E6,17E7', '{}', '{}', '圓餅圖','2023-05-17 02:27:32', '2023-05-17 02:27:32');
#     """
#     try:
#         cursor.execute(sql)
#         db.commit()
#     except:
#         print('1')
#         db.rollback()
#     db.close()


# with db.cursor() as cursor:
#     sql = """
#     CREATE TABLE `graphiccontrol`.`chart_values`(
#     `Guid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '唯一碼',
#     `ChartCollectsGuid` VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '圖表設定唯一碼',
#     `TimeStamp` INT UNSIGNED NOT NULL COMMENT '當下秒數',
#     `Collect` LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '數據集合',
#     `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     PRIMARY KEY (`Guid`(40)), INDEX (`ChartCollectsGuid`(40)),
#     INDEX (`TimeStamp`)
# ) ENGINE=InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;
#     """
#     cursor.execute(sql)
#     db.close()
#

# with db.cursor() as cursor:
#     sql = """
#     CREATE TABLE `graphiccontrol`.`settings`(
#     `Guid` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '全局唯一識別元',
#     `Name` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '元件名稱',
#     `CollectData` longtext COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '數據集合',
#     `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     PRIMARY KEY (`Guid`(40))
# ) ENGINE=InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;
#     """
#     cursor.execute(sql)
#     db.close()

# with db.cursor() as cursor:
#     sql = """
#    INSERT INTO `settings` (`Guid`, `Name`, `CollectData`, `created_at`, `updated_at`) VALUES
#     ('427841f6-a5b5-4658-a4d7-105a5730124c', 'LoopTimes', '{\"ReTry\":3,\"LineNotifyLimitTime\":60}', '2023-05-16 05:28:18', '2023-05-29 04:28:28'),
#     ('4605e414-192f-4667-82d1-fcbd2766255f', 'SMS', '{\"OwnPhone\":\"0972153032\",\"OwnPassword\":\"~!QAZ2wsx\",\"Group\":[{\"Phone\":\"0972153032\"}]}', '2023-05-16 05:28:18', '2023-05-31 02:02:10'),
#     ('4650c0d7-ae99-40f0-9572-a3375c03e68d', 'Line', '{\"Group\":[{\"Token\":\"1FP4CFtj7O7cCX59jAfdLiu8GCqOu6Xe26Kd2v5ZgYk\"}]}', '2023-05-16 05:28:18', '2023-05-29 04:24:36'),
#     ('e972137f-347a-41c7-b662-9a378de35211', 'Email', '{\"OwnEmail\":\"nexstar1436@gmail.com\",\"OwnPassword\":\"pzhuiybsqjrbbdgk\",\"Group\":[{\"ToEmail\":\"nexstar1436@gmail.com\"}]}', '2023-05-16 05:28:18', '2023-05-31 02:05:47');
#      """
#     try:
#         cursor.execute(sql)
#         db.commit()
#     except:
#         print('1')
#         db.rollback()
#     db.close()

# with db.cursor() as cursor:
#     sql = "INSERT INTO `bit_cells`VALUES(%s,%s)"
#
#     try:
#
#         cursor.execute(sql, ('1', '2', '3', '4', '5'))  ##方便
#         db.commit()
#     except:
#       print('1')
#         db.rollback()
#      db.close()

#######################################  bit_cells  #########################################################

# with db.cursor() as cursor:
#     SQL = """
#         INSERT INTO `bit_cells`(
#             `Guid`,`Name`,`Address`,`NowValue`,`HandTrigger`,`HandTriggerValue`,
#             `CollectData`,`NotifyStatus`,`NotifyCollectData`,`created_at`,`updated_at`
#         ) VALUES (
#             %s,%s,%s,0,99,99,'{}',0,
#             '{\"NotifyType\": 0, \"NotifyPlatFrom\": 0, \"NotifyTimeStamp\": 0, \"NotifyDateTime\": 0}',
#             %s,%s
#         );
#     """
#     for n in [
#         ['M0', '800'], ['M1', '801'], ['M2', '802'], ['M3', '803'], ['M4', '804']
#         , ['M5', '805'], ['M6', '806'], ['Y0', '500'], ['Y1', '501'], ['Y2', '502']
#         , ['Y3', '503'], ['Y4', '504'], ['Y5', '505'], ['Y6', '506'], ['Y7', '507']
#         , ['Y10', '508'], ['Y11', '509'], ['Y12', '50A']
#     ]:
#         cursor.execute(SQL, (str(uuid.uuid4()), n[0], n[1], TmpDate, TmpDate))
#         db.commit()
#     db.close()

#######################################  v_strings  #########################################################


# with db.cursor() as cursor:
#     SQL = """
#          INSERT INTO `v_strings`(
#             `Guid`,`Name`,`Address`,`NowValue`,`HandTrigger`,`HandTriggerValue`,
#             `CollectData`,`NotifyStatus`,`NotifyCollectData`,`created_at`,`updated_at`
#         ) VALUES (
#             %s,%s,%s,'0',99,'99',
#             '{\"WordType\":\"String\",\"SignedType\":true,\"NumberOfRegisters\":1,\"MaxValue\":0,\"MinValue\":0,\"HLValueConvert\":0}',
#             0,'{\"NotifyPlatFrom\": 0, \"NotifyTimeStamp\": 0, \"NotifyDateTime\": 0}',
#             %s,%s
#         )
#     """
#     for n in [
#         ['D2006', '17D6'], ['D2007', '17D7'], ['D2008', '17D8'], ['D2009', '17D9'], ['D2010', '17DA']
#     ]:
#         cursor.execute(SQL, (str(uuid.uuid4()), n[0], n[1], TmpDate, TmpDate))
#         db.commit()
#     db.close()

#######################################  v_words  #########################################################

# with db.cursor() as cursor:
#     SQL = """
#         INSERT INTO `v_words`(
#             `Guid`,`Name`,`Address`,`NowValue`,`HandTrigger`,`HandTriggerValue`,
#             `CollectData`,`NotifyStatus`,`NotifyCollectData`,`created_at`,`updated_at`
#         ) VALUES (
#             %s,%s,%s,'0',99,'99',
#             '{\"WordType\":\"Word\",\"SignedType\":true,\"NumberOfDecimals\":0,\"MaxValue\":0,\"MinValue\":0,\"HLValueConvert\":0}',
#             0,
#             '{\"NotifyPlatFrom\": 2, \"NotifyTimeStamp\": 1685327881, \"NotifyDateTime\": \"2023-05-29 10:38:01\"}', #警示
#             %s,%s
#         )
#     """
#     for n in [
#         ['D2000', '17D0'], ['D2001', '17D1'], ['D2002', '17D2'], ['D2004', '17D4'],
#         ['D2021', '17E5'], ['D2022', '17E6'], ['D2023', '17E7'], ['D2024', '17E8'], ['D2025', '17E9']
#     ]:
#         cursor.execute(SQL, (str(uuid.uuid4()), n[0], n[1], TmpDate, TmpDate))
#         db.commit()
#     db.close()

##****

with db.cursor() as cursor:
    command = "SELECT * FROM `bit_cells`"
    cursor.execute(command)
    db.commit()
    tmp = cursor.fetchall()

    for n in tmp:
        if n[1] == 'M5' and n[7]==1:
            print(n)
            tmp = json.loads(n[8])
            tmpNotifyPlatFrom=int(tmp["NotifyPlatFrom"])
            tmpNotifyType=int(tmp["NotifyType"])
            if tmpNotifyType == 1 and tmpNotifyPlatFrom == 2:
                print('Line')
#
#
#     db.close()

# with db.cursor() as corsor:
#     command="select * from `bit_cells`"
#     corsor.execute(command)
#     db.commit()
#     asd=corsor.fetchall()
#     for n in asd:
#         if n[1] == 'Y6' and n[7] == 1:
#             print(n)
#             tmp= json.loads(n[8])
#             tmp1=int(tmp["NotifyType"])
#             tmp2=int(tmp["NotifyPlatFrom"])
#             if tmp1 == 1 and tmp2 == 1:
#                 print('line')
#
#     db.close()


while True:

 with db.cursor() as corsor:
    command="select * from `bit_cells`"
    corsor.execute(command)
    db.commit()
    asd=corsor.fetchall()
    Int_TimeStamp = int(time.time())
    TmpDate = datetime.fromtimestamp(Int_TimeStamp).strftime('%Y-%m-%d %H:%M:%S')
    # print(asd)

    for n in asd:

        if  n[7] == 1:
            # print(n)
            tmp=json.loads(n[8])
            tmp1=int(tmp["NotifyType"])
            tmp2=int(tmp["NotifyPlatFrom"])
            if tmp1 == 1 and tmp2 == 1:
                print(n[1],"email",TmpDate)
            elif tmp1 == 1 and tmp2 == 2:
                print(n[1],'line',TmpDate)
            elif tmp1 == 1 and tmp2 == 0:
                print(n[1],'SMS',TmpDate)
            else:
                print('NULL')
            if n[7] == 0:
             break
    time.sleep(1)














