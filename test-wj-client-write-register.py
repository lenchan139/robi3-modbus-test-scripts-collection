from pymodbus.client.sync import ModbusSerialClient
from common_modbus_client_init import getModbusClient

from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian

client = getModbusClient()
addr = int(0x1A)
client.write_register(int(addr), 113) # 寫入 113 到 0x1A
result = client.read_holding_registers(int(addr),32) #讀取
decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Big)
print(decoder.decode_32bit_int())
client.close()
