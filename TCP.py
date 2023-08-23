from pyModbusTCP.client import ModbusClient

c=ModbusClient(
    host='192.168.1.5',
    port=502,
    auto_open=True,
    unit_id=1,
    timeout=1,
    debug=False
)
#寫入單筆
# s=c.write_single_coil(
#     bit_addr=int('500',16),
#     bit_value=False
# )
# print(s)

#寫入多筆
#
# bits_value=[True,False,True]
# s=c.write_multiple_coils(
#     bits_addr=int('500',16),
#     bits_value=bits_value
# )
# print(s)
#
# #讀出多筆
#
# s=c.read_coils(
#     bit_addr=int('500',16),
#     bit_nb=3
# )
# print(s)

# s=c.write_single_register(
#     reg_addr=int('17D0',16),
#     reg_value=18489
# )
# print(s)

import time
start_time=time.time()
tmp=[]
for xx in range(0,100):

    tmp.append(5)
print(tmp)


s = c.write_multiple_registers(
  regs_addr=int('17D0', 16),
  regs_value=tmp
)
end_time=time.time()
print('end-start:',end_time-start_time)



