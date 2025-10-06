def fcfs_disk_scheduling(requests, head_start):
    print("\n--- FCFS Disk Scheduling ---")
    print(f"Initial Head Position: {head_start}")
    total_seek_time = 0
    current_position = head_start

    # Process requests in the order they arrive
    for req in requests:
        distance = abs(req - current_position)
        print(f"Move from {current_position} → {req} (Seek: {distance})")
        total_seek_time += distance
        current_position = req

    print("\nTotal Seek Time:", total_seek_time)
    print("Average Seek Time:", total_seek_time / len(requests))


# ---------------- Main Program ----------------
if __name__ == "__main__":
    # Input: Disk request queue
    n = int(input("Enter number of disk requests: "))
    requests = []
    for i in range(n):
        req = int(input(f"Enter request {i+1}: "))
        requests.append(req)

    head_start = int(input("Enter initial head position: "))

    # Run FCFS scheduling
    fcfs_disk_scheduling(requests, head_start)
