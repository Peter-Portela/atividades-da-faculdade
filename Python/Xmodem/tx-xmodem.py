import serial
SOH=bytes([0x01])
ACK=bytes([0x06])
NAK=bytes([0x15])
CAN=bytes([0x18])
EOT=bytes([0x04])
CPE=chr(0x1A)
SEQ=1
DATA=""
FCS=0

def ler_DATA(arq):
    i=0
    DATA=""
    c=arq.read(1)
    while (c!='' and i<128):
      DATA=DATA+c
      c=arq.read(1)
      i=i+1
    if (c==''and i==0):
      return DATA
    elif (c=='' and i<128):
         while (i<128):
           DATA=DATA+CPE
           i=i+1
    return DATA

def calcula_FCS(DATA):
    FCS=0
    LDATA=list(DATA)
    for i in range(128):
       FCS=FCS+ord(LDATA[i])
    FCS=FCS%256
    return FCS

def envia_pacote(SEQ,DATA,ser):
    FCS=calcula_FCS(DATA)
    while True:
      ser.write(SOH)			# envia SOH
      ser.write(bytes([SEQ]))		# envia SEQ
      ser.write(bytes([~SEQ&0xff]))  	# envia ~SEQ
      ser.write(DATA.encode())		# envia DATA
      ser.write(bytes([FCS]))		# envia FCS
      r=ser.read(1)	# recebe resposta
      if (r==ACK):	# verifica resposta OK
        return True
      elif (r==CAN):
        return False
  
narq = input("entre com o nome do arquivo : ")
arq = open(narq,"r")
ser = serial.Serial('/dev/pts/1')
print(ser.portstr)
DATA=ler_DATA(arq)
while (DATA!=""):
  print("envia pacote ",SEQ,"\n")
  if (envia_pacote(SEQ,DATA,ser)==False):
    print("CAN - Cancelamento\n")
    quit()
  DATA=ler_DATA(arq)
  SEQ=(SEQ+1)%256
while True:
  print ("EOT - Fim da transmissao\n")
  ser.write(EOT)	# envia EOT
  r=ser.read(1)	# recebe resposta
  if (r==ACK):	# verifica resposta OK
     break
ser.close()
