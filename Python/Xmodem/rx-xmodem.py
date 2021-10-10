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

def grava_DATA(arq,DATA):
    arq.write(DATA)

def calcula_FCS(DATA):
    FCS=0
    LDATA=list(DATA)
    for i in range(128):
       FCS=FCS+ord(LDATA[i])
    FCS=FCS%256
    return FCS

def recebe_pacote(SEQ,ser):
    while True:
      DATA=""
      r=ser.read(1)			# le SOH
      if (r==SOH):
         r=ser.read(1)			# le SEQ
         if (r==bytes([SEQ])):
           r=ser.read(1)			# le ~SEQ
           if (r==bytes([~SEQ&0xff])):
              DATA=ser.read(128).decode()	# le DATA
              FCS=ser.read(1)		# le FCS
              FCS2=calcula_FCS(DATA)	# recalcula FCS
              if (FCS==bytes([FCS2])):	# verifica FCS
                 ser.write(ACK)		# envia ACK
                 print ("recebido")
                 return DATA
              else:
                 print("ERRO1\n")
                 ser.write(NAK)		# ERRO envia NAK
           else:
              print ("ERRO2\n")
              ser.write(NAK)		# ERRO envia NAK
         else:
           print ("ERRO3\n")
           ser.write(NAK)			# ERRO envia NAK
      elif (r==EOT):
   	   ser.write(ACK)			# ERRO envia ACK
   	   print ("EOT - Fim da transmissao")
   	   return DATA
      elif (r==CAN):
           ser.write(ACK)			# envia ACK
           print ("CAN - Cancelamento")
           return DATA
      else:
           print ("ERRO4\n")
           ser.write(NAK)			# ERRO envia NAK

narq = input("entre com o nome do arquivo : ")
arq = open(narq,"w")
ser = serial.Serial(port='/dev/pts/2')
print(ser.portstr)
ser.write(NAK)
while True:
  DATA=recebe_pacote(SEQ,ser)
  if (DATA==""):
    break
  else:
    SEQ=SEQ+1
    arq.write(DATA)
ser.close()
