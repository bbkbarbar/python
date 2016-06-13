from multiprocessing import Process
import time

def doWork():
    while True:
        print "working...."
        time.sleep(1)



p = Process(target=doWork)
p.start()

while True:
    time.sleep(6)