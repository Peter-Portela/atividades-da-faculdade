import threading

global s
s = threading.Semaphore(1)

global x

def f1():
  global x
  global s
  s.acquire()
  x = 0
  for i in range(14):
    x = x + i
    print(f'O numero atual eh {x}')
  s.release()
def f2():
  global x
  global s
  s.acquire()
  x = 0
  for i in range(14):
    x = x + i
    print(f'O numero atual eh {x}')
  s.release()
def f3():
  global x
  global s
  s.acquire()
  x = x * x
  print(f'O ultimo valor de x ao quadrado eh {x}')
  s.release()

t1=threading.Thread(target=f1,args=())
t2=threading.Thread(target=f2,args=())
t3=threading.Thread(target=f3,args=())
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

print("Fim do programa\n")


