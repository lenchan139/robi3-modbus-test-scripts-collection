from pymodbus.client.sync import ModbusSerialClient
from common_modbus_client_init import getModbusClient

client = getModbusClient()
addr = int(0x1A)
# client.write_coil(int(addr), True)
result = client.read_holding_registers(int(addr),1) # 讀取 1A 的資料
print(result)
client.close()
