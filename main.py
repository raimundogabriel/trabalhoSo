import threading

N = 10
buf = [0] * N

fill_count = threading.Semaphore(0)
empty_count = threading.Semaphore(N)
mutex = threading.Lock()

def produce():
    print("One item produced!")
    return 1

def consume(y):
    print("One item consumed!")

def producer():
    front = 0
    while True:
        x = produce()
        empty_count.acquire()
        mutex.acquire()
        buf[front] = x
        front = (front + 1) % N
        mutex.release()
        fill_count.release()

def consumer():
    rear = 0
    while True:
        fill_count.acquire()
        mutex.acquire()
        y = buf[rear]
        rear = (rear + 1) % N
        mutex.release()
        empty_count.release()
        consume(y)

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()