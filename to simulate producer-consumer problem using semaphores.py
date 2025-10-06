import threading
import time
import random

# Buffer size
BUFFER_SIZE = 5
buffer = []

# Semaphores
empty = threading.Semaphore(BUFFER_SIZE)  # Initially, buffer is empty
full = threading.Semaphore(0)             # No items initially
mutex = threading.Semaphore(1)            # Binary semaphore for mutual exclusion

# Producer function
def producer():
    global buffer
    for i in range(10):
        item = random.randint(1, 100)
        empty.acquire()    # Wait if buffer is full
        mutex.acquire()    # Enter critical section
        buffer.append(item)
        print(f"Producer produced: {item} | Buffer: {buffer}")
        mutex.release()    # Exit critical section
        full.release()     # Signal that buffer has new item
        time.sleep(random.uniform(0.5, 1.5))

# Consumer function
def consumer():
    global buffer
    for i in range(10):
        full.acquire()     # Wait if buffer is empty
        mutex.acquire()    # Enter critical section
        item = buffer.pop(0)
        print(f"Consumer consumed: {item} | Buffer: {buffer}")
        mutex.release()    # Exit critical section
        empty.release()    # Signal that buffer has empty slot
        time.sleep(random.uniform(0.5, 2))

if __name__ == "__main__":
    # Create producer and consumer threads
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    # Start threads
    producer_thread.start()
    consumer_thread.start()

    # Wait for threads to finish
    producer_thread.join()
    consumer_thread.join()

    print("Producer-Consumer simulation completed.")
