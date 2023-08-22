import minimalmodbus

c = minimalmodbus.Instrument(port='COM5',slaveaddress=1)
c.serial.baudrate = 9600
c.serial.bytesize = 7
c.serial.parity = 'E'
c.serial.stopbits = 1
c.serial.timeout = 1
c.mode = minimalmodbus.MODE_ASCII
c.clear_buffers_before_each_transaction = True
c.close_port_after_each_call =True

#
# c.write_bit(
#     registeraddress=int('0800',16),
#     value=1,
#     functioncode=5
# )



# TmpX= c.read_bit(
#     registeraddress=int('0500',16),
#     functioncode=2
# )
# print(TmpX)

# TmpArray = []
# for index in range(0,4):
#     TmpArray.append(0)
#
# c.write_bits(
#     registeraddress=int('0500',16),
#     values=TmpArray
# )

# TmpX=c.read_bits(
#     registeraddress=int('0800',16),
#     number_of_bits=4,
#     functioncode=2
#
# #
# )
# print(TmpX)
# print(type(TmpX))

# c.write_bit(
#     registeraddress=int('800',16),
#     value=1,
#     functioncode=5
# )
#
# TmpX= c.read_bit(
#     registeraddress=int('800',16),
#     functioncode=2
# )
# print(TmpX)


#
# TmpX=c.read_bit(
#     registeraddress=int('800',16),
#     number_of+bits=20,
#     functioncode=2
# )
# print(TmpX)

# import time###################
# stat_time=time.time()
#
# tmpX=[]
# for index in range(0,31):
#     if index %2 == 0:
#         tmpX.append(1)
#
#     else:
#         tmpX.append(0)
#
# c.write_bits(
#     registeraddress=int('800',16), ################
#     values=tmpX
# )
#
# end_time=time.time()
# print(end_time,stat_time)############

# tmp=2
# c.write_register(
#     registeraddress=int('17D0',16),
#     value=tmp,
#     numbers_of_decimals=0,
#     signed=True,
#     functioncode=3
#
# )

###文字>十六進制>10進制

for xx in ['&','~','&~']: ##串列

    Tmp2=int(xx.encode('utf-8').hex(),16)
    print(Tmp2)

c.write_string(
    registeraddress=int('17D0',16),
    textstring='AC',
    number_of_registers=1
)
tmp=16706
c.write_register(
    registeraddress=int('17D0',16),
    value=tmp,
    number_of_decimals=0,
    signed=True,
    functioncode=6

)
tmp=c.read_string(
    registeraddress=int('17D0',16),
    nuber_of_=1,
    functioncode=3
)