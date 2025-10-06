import threading
import time
import random

# Buffer (shared resource)
buffer = []
buffer_size = 5

# Semaphores for synchronization
empty = threading.Semaphore(buffer_size)  # Count empty slots
full = threading.Semaphore(0)             # Count full slots
mutex = threading.Lock()                   # Mutual exclusion lock

# Producer thread
def producer():
    global buffer
    for i in range(10):  # Produce 10 items
        item = random.randint(1, 100)
        empty.acquire()     # Wait if buffer is full
        mutex.acquire()     # Enter critical section

        buffer.append(item)
        print(f"Producer produced: {item} | Buffer: {buffer}")

        mutex.release()     # Exit critical section
        full.release()      # Signal that buffer has an item
        time.sleep(random.random())  # Simulate production time

# Consumer thread
def consumer():
    global buffer
    for i in range(10):  # Consume 10 items
        full.acquire()      # Wait if buffer is empty
        mutex.acquire()     # Enter critical section

        item = buffer.pop(0)
        print(f"Consumer consumed: {item} | Buffer: {buffer}")

        mutex.release()     # Exit critical section
        empty.release()     # Signal that buffer has a free slot
        time.sleep(random.random())  # Simulate consumption time

# Main program
if __name__ == "__main__":
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Producer-Consumer simulation finished.")
