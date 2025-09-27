from multiprocessing import Process, Queue
import os
import time
def sender(q):
    messages = ["Hello", "How are you?", "This is IPC using Message Queue", "STOP"]
    for msg in messages:
        print(f"[Sender PID {os.getpid()}] Sending: {msg}")
        q.put(msg) 
        time.sleep(1)  
def receiver(q):
    while True:
        msg = q.get()
        print(f"[Receiver PID {os.getpid()}] Received: {msg}")
        if msg == "STOP": 
            break
if __name__ == "__main__":
    q = Queue()
    p1 = Process(target=sender, args=(q,))
    p2 = Process(target=receiver, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Message Queue IPC Demo Completed.")
