#threading and multiprocessing


from threading import Thread
import os 
import time 
def square_number():
    for i in range(100):
        i *i
        time.sleep(0.1)


thread = []

num_thread = os.cpu_count()

for i in range(num_thread):
    p  = Thread(target=square_number)
    thread.append(p) 

for t in thread:
    t.start()
for t in thread:
    t.join()

print("end main")
