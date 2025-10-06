import threading
import time

# Function to run in a thread
def print_numbers():
    for i in range(1, 6):
        print(f"Numbers Thread: {i}")
        time.sleep(1)

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letters Thread: {letter}")
        time.sleep(1.5)

if __name__ == "__main__":
    # Create threads
    t1 = threading.Thread(target=print_numbers)
    t2 = threading.Thread(target=print_letters)

    # Start threads
    t1.start()
    t2.start()

    # Wait for both threads to complete
    t1.join()
    t2.join()

    print("Main Thread: All threads have finished.")
