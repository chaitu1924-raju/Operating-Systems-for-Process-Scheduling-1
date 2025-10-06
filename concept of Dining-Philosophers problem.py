import threading
import time
import random

# Number of philosophers
NUM_PHILOSOPHERS = 5

# Create a lock for each fork
forks = [threading.Lock() for _ in range(NUM_PHILOSOPHERS)]

# Philosopher function
def philosopher(id):
    left_fork = forks[id]
    right_fork = forks[(id + 1) % NUM_PHILOSOPHERS]
    
    while True:
        # Thinking
        print(f"Philosopher {id} is thinking.")
        time.sleep(random.uniform(1, 3))
        
        # Try to pick up forks (lowest-numbered fork first to avoid deadlock)
        first_fork, second_fork = (left_fork, right_fork) if id % 2 == 0 else (right_fork, left_fork)
        
        with first_fork:
            print(f"Philosopher {id} picked up first fork.")
            time.sleep(0.5)
            with second_fork:
                print(f"Philosopher {id} picked up second fork.")
                # Eating
                print(f"Philosopher {id} is eating.")
                time.sleep(random.uniform(1, 2))
                print(f"Philosopher {id} finished eating and put down forks.")

if __name__ == "__main__":
    threads = []
    for i in range(NUM_PHILOSOPHERS):
        t = threading.Thread(target=philosopher, args=(i,))
        threads.append(t)
        t.start()

    # Let philosophers run for some time (e.g., 20 seconds)
    time.sleep(20)
    
    print("Simulation finished.")
