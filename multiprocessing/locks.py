from multiprocessing import Process, Lock, Value
import time

def add_500_no_mp(total):
    for i in range(100):
        time.sleep(0.01)
        total+=1
    return total

def sub_500_no_mp(total):
    for i in range(100):
        time.sleep(0.01)
        total-=1
    return total

def add_500_no_lock(total):
    for i in range(100):
        time.sleep(0.01)
        total.value+=1
    return total

def sub_500_no_lock(total):
    for i in range(100):
        time.sleep(0.01)
        total.value-=1
    return total

def add_500_lock(total, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        total.value+=1
        lock.release()
    return total

def sub_500_lock(total, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        total.value-=2
        lock.release()
    return total

if __name__ == '__main__':
    # total = 500
    # print(total)
    # total = add_500_no_mp(total)
    # print(total)
    # total = sub_500_no_mp(total)
    # print(total)

    # Sharing Value without lock
    # total = Value('i', 500)
    # add_process = Process(target=add_500_no_lock, args=(total,))
    # sub_process = Process(target=sub_500_no_lock, args=(total,))
    # add_process.start()
    # sub_process.start()
    # add_process.join()
    # sub_process.join()

    # print(total.value)

    # Sharing value with lock
    total = Value('i', 500)
    lock = Lock()
    add_process = Process(target=add_500_lock, args=(total,lock))
    sub_process = Process(target=sub_500_lock, args=(total,lock))
    add_process.start()
    sub_process.start()
    add_process.join()
    sub_process.join()

    print(total.value)