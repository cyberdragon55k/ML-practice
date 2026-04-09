#threading and multiprocessing


from multiprocessing import Process
import os 
processes = []

num_processes = os.cpu_count{}

for i in range(num_processes):
    p  = Process(target=)