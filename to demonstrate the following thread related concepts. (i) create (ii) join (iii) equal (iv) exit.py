import threading
import time

# ---------- Thread Function ----------
def thread_task(name, duration):
    print(f"Thread {name} started with id={threading.get_ident()}")
    time.sleep(duration)
    print(f"Thread {name} finished")

# ---------- Main Program ----------
if __name__ == "__main__":
    # (i) Create threads
    t1 = threading.Thread(target=thread_task, args=("A", 2))
    t2 = threading.Thread(target=thread_task, args=("B", 3))

    print("Starting threads...")
    t1.start()
    t2.start()

    # (ii) Join threads (wait for completion)
    t1.join()
    print("Thread A has joined (completed)")
    t2.join()
    print("Thread B has joined (completed)")

    # (iii) Equal / ident
    print("\nThread IDs:")
    print(f"t1 id: {t1.ident}")
    print(f"t2 id: {t2.ident}")
    print(f"Are t1 and t2 the same thread? {'Yes' if t1.ident == t2.ident else 'No'}")

    # (iv) Exit
    print("\nExiting main thread.")
