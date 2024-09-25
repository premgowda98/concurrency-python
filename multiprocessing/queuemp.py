from multiprocessing import Process, Queue

def square(numbers, queueds):
    for i in numbers:
        queueds.put(i*i)

def cube(numbers, queueds):
    for i in numbers:
        queueds.put(i*i*i)

if __name__ == '__main__':
    numbers = range(5)
    queue_ds = Queue()

    square_process=Process(target=square, args=(numbers, queue_ds))
    cube_process=Process(target=cube, args=(numbers, queue_ds))
    square_process.start()
    cube_process.start()

    square_process.join()
    cube_process.join()

    while not queue_ds.empty():
        print(queue_ds.get())
