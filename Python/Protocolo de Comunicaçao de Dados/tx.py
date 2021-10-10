
a = input("informe o primeiro número: ")
b = input("Informe o segundo número: ")
c = '+'

import serial
ser1=serial.Serial('/dev/pts/23')


ser1.write(a.encode())
ser1.write(c.encode())
ser1.write(b.encode())

ser1.write(a.encode())
ser1.write(b.encode())

print(ser1.read(2).decode())
