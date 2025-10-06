import threading
import time
import random

# Shared resource
shared_data = 0

# Semaphores
mutex = threading.Semaphore(1)   # Protects read_count
rw_mutex = threading.Semaphore(1)  # Ensures exclusive access for writers

# Number of readers currently reading
read_count = 0

# Reader function
def reader(reader_id):
    global read_count, shared_data
    for _ in range(5):
        mutex.acquire()          # Protect read_count
        read_count += 1
        if read_count == 1:
            rw_mutex.acquire()   # First reader locks the resource for writing
        mutex.release()

        # Reading section
        print(f"Reader {reader_id} reads value: {shared_data}")
        time.sleep(random.uniform(0.5, 1.5))

        mutex.acquire()
        read_count -= 1
        if read_count == 0:
            rw_mutex.release()   # Last reader releases the resource
        mutex.release()
        time.sleep(random.uniform(0.5, 1))

# Writer function
def writer(writer_id):
    global shared_data
    for _ in range(5):
        rw_mutex.acquire()      # Exclusive access for writing
        shared_data += random.randint(1, 10)
        print(f"Writer {writer_id} writes value: {shared_data}")
        time.sleep(random.uniform(1, 2))
        rw_mutex.release()
        time.sleep(random.uniform(0.5, 1))

if __name__ == "__main__":
    # Create reader and writer threads
    readers = [threading.Thread(target=reader, args=(i,)) for i in range(3)]
    writers = [threading.Thread(target=writer, args=(i,)) for i in range(2)]

    # Start threads
    for w in writers:
        w.start()
    for r in readers:
        r.start()

    # Wait for all threads to finish
    for w in writers:
        w.join()
    for r in readers:
        r.join()

    print("Reader-Writer simulation completed.")
