#invoking the appropriate system call. Get the process identifier of the
#currently running process and its respective parent using system calls and display
import os
from multiprocessing import Process

def child_process():
    print("\nChild Process:")
    print(f"PID: {os.getpid()}")
    print(f"Parent PID: {os.getppid()}")

def main():
    p = Process(target=child_process)
    p.start()
    print("Parent Process:")
    print(f"PID: {os.getpid()}")
    print(f"Parent PID: {os.getppid()}")
    print(f"Child PID: {p.pid}")

    p.join()

if __name__ == "__main__":
    main()
