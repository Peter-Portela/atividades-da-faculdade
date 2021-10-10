rxtxX2.py 
import serial
import threading

def tx():
    while(True):
      global serOUT
      E = input('Endereco : ')
      if (E==""):
        continue
      msg =  input('Mensagem : ')
      if (msg==""):
        continue
      ser2.write((E+';'+msg+'\n').encode())

def rxtx12():
    global ser1
    global ser2
    global END
    while(True):
      pkt=ser1.readline().decode()
      p = pkt.split(';')
      if not (p[0]=="A" or  p[0]=="B" or p[0]=="C" or p[0]=="D"):
        continue
      print("[ "+pkt+" ]")
      if (p[0] == END):
        print("\n\n"+p[1])
      else:
        ser2.write((pkt+'\n').encode())

def rxtx21():
    global ser1
    global ser2
    global END
    while(True):
      pkt=ser2.readline().decode()
      p = pkt.split(';')
      if not (p[0]=="A" or  p[0]=="B" or p[0]=="C" or p[0]=="D"):
        continue
      print("[ "+pkt+" ]")
      if (p[0] == END):
        print("\n\n"+p[1])
      else:
        ser1.write((pkt+'\n').encode())

porta1=input('porta 1 : ')
global ser1
ser1=serial.Serial(porta1)
porta2=input('porta 2 : ')
global ser2
ser2=serial.Serial(porta2)
global END
END=input('endereco local : ')  

t1=threading.Thread(target=tx)
t2=threading.Thread(target=rxtx12)
t3=threading.Thread(target=rxtx21)
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()


