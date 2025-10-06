def scan_disk_scheduling(requests, head_start, disk_size, direction):
    print("\n--- SCAN Disk Scheduling ---")
    print(f"Initial Head Position: {head_start}, Direction: {direction}")

    requests.sort()
    total_seek_time = 0
    seek_sequence = []

    # Split requests into left and right of head
    left = [req for req in requests if req < head_start]
    right = [req for req in requests if req >= head_start]

    left.sort(reverse=True)
    right.sort()

    # SCAN movement: head moves right first
    if direction == "right":
        # Service right side first
        for req in right:
            total_seek_time += abs(head_start - req)
            head_start = req
            seek_sequence.append(req)

        # Move to the end of disk if not already
        if head_start != disk_size - 1:
            total_seek_time += abs(head_start - (disk_size - 1))
            head_start = disk_size - 1
            seek_sequence.append(head_start)

        # Then move left
        for req in left:
            total_seek_time += abs(head_start - req)
            head_start = req
            seek_sequence.append(req)

    # SCAN movement: head moves left first
    elif direction == "left":
        # Service left side first
        for req in left:
            total_seek_time += abs(head_start - req)
            head_start = req
            seek_sequence.append(req)

        # Move to the start of disk if not already
        if head_start != 0:
            total_seek_time += abs(head_start - 0)
            head_start = 0
            seek_sequence.append(head_start)

        # Then move right
        for req in right:
            total_seek_time += abs(head_start - req)
            head_start = req
            seek_sequence.append(req)

    print("\nSeek Sequence:", seek_sequence)
    print("Total Seek Time:", total_seek_time)
    print("Average Seek Time:", total_seek_time / len(requests))


# ---------------- Main Program ----------------
if __name__ == "__main__":
    n = int(input("Enter number of disk requests: "))
    requests = []
    for i in range(n):
        req = int(input(f"Enter request {i+1}: "))
        requests.append(req)

    head_start = int(input("Enter initial head position: "))
    disk_size = int(input("Enter disk size (number of tracks): "))
    direction = input("Enter initial direction (left/right): ").lower()

    scan_disk_scheduling(requests, head_start, disk_size, direction)
