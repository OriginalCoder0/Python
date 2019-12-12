import time
import threading

def fun():
    print('a')
    threading.Timer(1,fun).start()

timer = threading.Timer(1,fun)
timer.start()

#while True:
#    time.sleep(1)
