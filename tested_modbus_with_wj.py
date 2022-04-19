from pymodbus.client.sync import ModbusSerialClient
from pymodbus.client.sync import ModbusTcpClient
import os
from dotenv import load_dotenv

from pymodbus.transaction import ModbusRtuFramer

load_dotenv()

env_mode =  os.environ['modbus_connection_mode']
env_addr = os.environ['modbus_connection_addr']
env_port = os.environ['modbus_connection_port']

print(env_mode)
print(env_addr)
print(env_port)

UNIT = 0x1
client = ModbusSerialClient(method='rtu', port='COM6', baudrate=9600,  stopbits=2, bytesize=8,  )

if not client.connect():
    print("Unable to connect  ")


addr = int(0x00) # 定義地址
#client.write_coil(0, True, unit=UNIT)
client.write_registers(0x202, 0x2, unit=UNIT)

result = client.read_holding_registers(0x202,2, unit=UNIT) # 讀取 0F 的內容
print(result.registers)
client.close()
