# pip3 install PyMySQL
import uuid

import pymysql


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
