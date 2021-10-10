import threading


def primeira():
    for i in range(10):
        print("Ola mundo")

def segunda():
    for j in range(10):
        print("Ola mundo")

threading.Thread(target=primeira).start()
threading.Thread(target=segunda).start()

