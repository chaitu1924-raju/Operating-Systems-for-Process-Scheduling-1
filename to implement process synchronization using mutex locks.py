import threading

# Shared resource
counter = 0

# Mutex lock
mutex = threading.Lock()

# Number of iterations per thread
NUM_ITERATIONS = 100000

# Thread function to increment counter
def increment():
    global counter
    for _ in range(NUM_ITERATIONS):
        mutex.acquire()      # Acquire the mutex before accessing shared resource
        counter += 1         # Critical section
        mutex.release()      # Release the mutex

if __name__ == "__main__":
    # Create threads
    t1 = threading.Thread(target=increment)
    t2 = threading.Thread(target=increment)

    # Start threads
    t1.start()
    t2.start()

    # Wait for threads to finish
    t1.join()
    t2.join()

    print("Final counter value:", counter)
