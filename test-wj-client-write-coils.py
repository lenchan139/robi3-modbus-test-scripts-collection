from pymodbus.client.sync import ModbusSerialClient
from common_modbus_client_init import getModbusClient

client = getModbusClient()
addr = int(0x0202)
client.write_coil(int(addr), True)# 寫入 1 到 0F
result = client.read_coils(int(addr),1) # 讀取之
print(result.bits[0])
client.close()
