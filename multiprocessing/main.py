import os
from multiprocessing import Process, current_process
import time

global_var  = 0

def square(num):
    global global_var
    global_var += 1
    pid = os.getpid()
    # time.sleep(5)
    print("Squared", num, "on process id", pid, global_var, "process name", current_process().name)

if __name__=="__main__":
    processes = []
    numbers = [1,2,3,4,5]

    for num in numbers:
        process = Process(target=square, args=(num,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join() # this join method makes sure the below code is executed only when all process are completed

    print(global_var)
