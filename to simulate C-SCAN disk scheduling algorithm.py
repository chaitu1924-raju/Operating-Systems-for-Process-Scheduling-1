def cscan_disk_scheduling(requests, head_start, disk_size, direction):
    print("\n--- C-SCAN Disk Scheduling ---")
    print(f"Initial Head Position: {head_start}, Direction: {direction}")

    requests.sort()
    total_seek_time = 0
    seek_sequence = []

    left = [req for req in requests if req < head_start]
    right = [req for req in requests if req >= head_start]

    left.sort()
    right.sort()

    if direction == "right":
        # Service the right side first
        for req in right:
            total_seek_time += abs(head_start - req)
            head_start = req
            seek_sequence.append(req)

        # Jump to end then to start
        if head_start != disk_size - 1:
            total_seek_time += abs(head_start - (disk_size - 1))
            head_start = disk_size - 1
            seek_sequence.append(head_start)

        # Jump to start of disk
        total_seek_time += abs(head_start - 0)
        head_start = 0
        seek_sequence.append(head_start)

        # Service remaining left side
        for req in left:
            total_seek_time += abs(head_start - req)
            head_start = req
            seek_sequence.append(req)

    elif direction == "left":
        # Service the left side first
        for req in reversed(left):
            total_seek_time += abs(head_start - req)
            head_start = req
            seek_sequence.append(req)

        # Jump to start then to end
        if head_start != 0:
            total_seek_time += abs(head_start - 0)
            head_start = 0
            seek_sequence.append(head_start)

        # Jump to end of disk
        total_seek_time += abs(head_start - (disk_size - 1))
        head_start = disk_size - 1
        seek_sequence.append(head_start)

        # Service remaining right side
        for req in reversed(right):
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

    cscan_disk_scheduling(requests, head_start, disk_size, direction)
