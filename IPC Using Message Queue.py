from multiprocessing import Process, Queue
import time

# Writer process function
def writer(queue):
    messages = ["Hello", "IPC using Queue", "Python"]
    for msg in messages:
        print(f"Writer: Sending message -> {msg}")
        queue.put(msg)  # send message to queue
        time.sleep(1)  # simulate processing time

# Reader process function
def reader(queue):
    for _ in range(3):
        msg = queue.get()  # receive message from queue
        print(f"Reader: Received message -> {msg}")

if __name__ == "__main__":
    # Create a Queue
    q = Queue()

    # Create writer and reader processes
    writer_process = Process(target=writer, args=(q,))
    reader_process = Process(target=reader, args=(q,))

    # Start processes
    writer_process.start()
    reader_process.start()

    # Wait for completion
    writer_process.join()
    reader_process.join()
