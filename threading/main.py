import time
import threading

def  myfunc():
    print("hello")
    time.sleep(5)
    print("done")
    return True

def  myfunc():
    print("My func started")
    time.sleep(5)
    print("My func ended")
    return True

if __name__ == '__main__':
    print("Started")
    t = threading.Thread(target=myfunc)
    t.start()
    t.join() # will make sure the below code is executed only after the threading operation is successful
    print("Ended")
    # myfunc()