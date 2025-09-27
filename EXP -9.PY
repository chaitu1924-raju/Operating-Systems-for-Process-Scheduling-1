from multiprocessing import Process, Value, Array
import time

def producer(shared_num, shared_array):
    print("[Producer] Starting...")
    shared_num.value = 42
    for i in range(len(shared_array)):
        shared_array[i] = i * 2  
    print("[Producer] Data written to shared memory.")
    time.sleep(2) 

def consumer(shared_num, shared_array):
    time.sleep(1) 
    print("[Consumer] Reading from shared memory...")
    print("Shared number:", shared_num.value)
    print("Shared array:", list(shared_array))

if __name__ == "__main__":
 
    shared_num = Value('i', 0)    
    shared_array = Array('i', 5)    
    p1 = Process(target=producer, args=(shared_num, shared_array))
    p2 = Process(target=consumer, args=(shared_num, shared_array))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("[Main] Program finished.")
