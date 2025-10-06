import multiprocessing

def child_process():
    print("\n--- Child Process ---")
    print(f"Child PID: {multiprocessing.current_process().pid}")
    print(f"Child's Parent PID: {multiprocessing.parent_process().pid}")

def main():
    print("\n--- Parent Process ---")
    print(f"Parent PID: {multiprocessing.current_process().pid}")
    print(f"Parent's Parent PID: {multiprocessing.parent_process()}")  # Will be None (since top-level process has no parent)

    # Create a new process
    p = multiprocessing.Process(target=child_process)
    p.start()
    p.join()

if __name__ == "__main__":
    main()

