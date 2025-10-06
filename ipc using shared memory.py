from multiprocessing import Process, Queue
import time

# Writer process
def writer(queue):
    messages = ["Hello", "from", "the", "Writer", "STOP"]
    for msg in messages:
        print(f"[Writer] Sending: {msg}")
        queue.put(msg)  # send message to queue
        time.sleep(0.5)

# Reader process
def reader(queue):
    while True:
        msg = queue.get()  # receive message
        if msg == "STOP":  # termination signal
            print("[Reader] Received STOP. Exiting...")
            break
        print(f"[Reader] Received: {msg}")

if _name_ == "_main_":
    q = Queue()  # create message queue

    # Create writer and reader processes
    p1 = Process(target=writer, args=(q,))
    p2 = Process(target=reader, args=(q,))

    # Start processes
    p1.start()
    p2.start()

    # Wait for processes to complete
    p1.join()
    p2.join()

    print("\n[Main] Message Queue IPC completed.")