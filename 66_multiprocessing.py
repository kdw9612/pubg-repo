# ****************************
# Python multiprocessing
# ****************************
# multiprocessing = running tasks in parellel on different cpu cores, bypass GIL
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound (waiting around)

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    a = Process(target=counter, args=(1000000000,))
    a.start()
    
    a.join()
    
main()
