import os
from multiprocessing import Process, current_process, Pool
import time


def square(num):
    s=0
    for i in range(num):
        s+=i*i
    return s 

print(__name__)

if __name__ == '__main__':
    
    # numbers = [1,2,3]
    # p = Pool()
    # result = p.map(square, numbers)
    # print(result)
    # p.close()
    # p.join()

    with Pool(4) as pool:
        # Submit tasks using map
        numbers = [1, 2, 3, 4, 5]
        results = pool.map(square, numbers)
        print(results)

    print(os.cpu_count())
    