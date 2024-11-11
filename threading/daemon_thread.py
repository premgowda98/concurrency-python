import threading
import time

total = 4

def creates_items():
    global total
    for i in range(10):
        time.sleep(2)
        print('added item')
        total += 1
    print('creation is done')


def creates_items_2():
    global total
    for i in range(7):
        time.sleep(1)
        print('added item')
        total += 1
    print('creation is done')


def limits_items():
    
    #print('finished sleeping')
    
    global total
    while True:
        if total > 5:

            print ('overload')
            total -= 3
            print('subtracted 3')
        else:
            time.sleep(1)
            print('waiting')


creator1 = threading.Thread(target  = creates_items)
creator2 = threading.Thread(target = creates_items_2)
limitor = threading.Thread(target = limits_items, daemon = True)

print(limitor.isDaemon())


creator1.start()
creator2.start()
limitor.start()


creator1.join()
creator2.join()

# In the above lines we have not added limitor.join() impleing that it will not block the below print command
# and we also want to kill it after creator1 and 2. SO we have made limitor thread as Daemon, meaning it will 
# killed as soon as the main thread is killed.

print('our ending value of total is' , total)