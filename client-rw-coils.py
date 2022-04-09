from pymodbus.client.sync import ModbusSerialClient

client = ModbusSerialClient(method='rtu', port="/dev/ttySS0")
client.write_coil(1, True)
result = client.read_coils(1,1)
print(result.bits[0])
client.close()
