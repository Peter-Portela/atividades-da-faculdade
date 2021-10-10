

d = ''

import serial
ser2=serial.Serial('/dev/pts/24')
print(ser2.read(2).decode())
print(ser2.read(1).decode())
print(ser2.read(2).decode())

a = ser2.read(2).decode()
b = ser2.read(2).decode()

d = int(a) + int(b)
d = str(d)

ser2.write(d.encode())
