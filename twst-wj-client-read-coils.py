from pymodbus.client.sync import ModbusSerialClient
from common_modbus_client_init import getModbusClient

client = getModbusClient()
addr = int(0x0F) # 定義地址
# client.write_coil(int(addr), True)
result = client.read_coils(int(addr),1) # 讀取 0F 的內容
print(result.bits[0])
client.close()
