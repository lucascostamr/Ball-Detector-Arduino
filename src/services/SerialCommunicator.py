import serial
import time

class SerialCommunicator:
    def __init__(self, serial_device: str, baudrate: int, timeout:int =.1 ):
        self.device = serial.Serial(port=serial_device, baudrate=baudrate, timeout=timeout)
        time.sleep(2)

    def send_data(self, data: str):
        self.device.write(data.encode())
    
    def close(self):
        self.device.close()