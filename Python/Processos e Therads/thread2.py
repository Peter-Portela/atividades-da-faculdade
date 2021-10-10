import threading


def primeira():
    for i in range(10):
        print(i)

def segunda():

    for j in range(10):
        print(j)

threading.Thread(target=primeira).start()
threading.Thread(target=segunda).start()

