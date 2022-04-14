from pymodbus.client.sync import ModbusSerialClient
from pymodbus.client.sync import ModbusTcpClient
import os 
from dotenv import load_dotenv

load_dotenv()

env_mode =  os.environ['modbus_connection_mode']
env_addr = os.environ['modbus_connection_addr'] 
env_port = os.environ['modbus_connection_port']
def getModbusClient():
    if(env_mode.lower() == 'tcp'):
        return ModbusTcpClient(host=env_addr, port=env_port)
    elif(env_mode.lower() == 'com'):
        return ModbusSerialClient(method='rtu', port=env_addr, dataBits=env_port) 
    
    