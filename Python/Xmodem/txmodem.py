import serial
# definir bytes de controle de acordo com a tabela ascii em HEXA para possibilitar o write
SOH=bytes([0x01]) # inicio da trama
ACK=bytes([0x06]) # resposta que o receptor manda para o transmissor para confirmação
NAK=bytes([0x15]) # resposta que o receptor manda para o transmissor para trama com erro
CAN=bytes([0x18]) # possibilidade de cancelar transmissão
EOT=bytes([0x04]) # fim da transmissão 
CPE=chr(0x1A) # caractere de preenchimento (SUB)
SEQ=1
DATA=""
FCS=0

# funcoes para execução
def ler_DATA(arq): # DATA possui tamanho fixo de 128 bytes
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

# soma aritmetica dos dados%256
def calcula_FCS(DATA): # recebe DATA
    FCS=0
    LDATA=list(DATA) # transforma dados em uma lista
    for i in range(128):
       FCS=FCS+ord(LDATA[i])
    FCS=FCS%256 # calculo do modulo
    return FCS

def envia_pacote(SEQ,DATA,ser):
    FCS=calcula_FCS(DATA) # chama funcao FCS
    while True: #transforma em bytes para envio, elimina a necessidade do encode
      ser.write(SOH)			# envia SOH
      ser.write(bytes([SEQ]))		# envia SEQ
      ser.write(bytes([~SEQ&0xff]))  	# envia ~SEQ, 0xff = 255 para obter o inverso
      ser.write(DATA.encode())		# envia DATA
      ser.write(bytes([FCS]))		# envia FCS
      r=ser.read(1)	# recebe resposta
      if (r==ACK):	# verifica resposta OK
        return True
      elif (r==CAN):
        return False
  
narq = input("entre com o nome do arquivo : ") # arquivo que sera enviado
arq = open(narq,"r") # abrir arquivo como leitura
ser = serial.Serial('/dev/pts/0') # ajuste de portas
print(ser.portstr) # imprime porta serial
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
  (ser.write(EOT)) # envia EOT
  r=ser.read(1)    # recebe resposta
  if (r==ACK):     # verifica resposta
    break
ser.close()