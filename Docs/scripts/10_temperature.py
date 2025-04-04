import machine
import time

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

def print_temperature():
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    print("Temp: {:.2f}°C" .format(temperature))
    
if __name__ == '__main__':
    try:
        while True:
            print_temperature()
            time.sleep(2)
    except KeyboardInterrupt:
        pass
