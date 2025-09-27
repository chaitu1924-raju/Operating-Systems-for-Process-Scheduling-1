def priority_preemptive_scheduling(processes):
    n = len(processes)
    processes.sort(key=lambda x: x[1])
    pid = [p[0] for p in processes]
    arrival = [p[1] for p in processes]
    burst = [p[2] for p in processes]
    priority = [p[3] for p in processes]
    remaining_time = burst[:]
    completion = [0] * n
    waiting = [0] * n
    turnaround = [0] * n
    is_completed = [False] * n

    time = 0
    completed = 0

    while completed != n:
        idx = -1
        max_priority = -1
        for i in range(n):
            if arrival[i] <= time and not is_completed[i]:
                if priority[i] > max_priority:
                    max_priority = priority[i]
                    idx = i
                elif priority[i] == max_priority:
                    if arrival[i] < arrival[idx]:
                        idx = i

        if idx != -1:
            remaining_time[idx] -= 1
            time += 1

            if remaining_time[idx] == 0:
                completion[idx] = time
                turnaround[idx] = completion[idx] - arrival[idx]
                waiting[idx] = turnaround[idx] - burst[idx]
                is_completed[idx] = True
                completed += 1
        else:
            time += 1 
    print("PID\tAT\tBT\tPRI\tCT\tTAT\tWT")
    for i in range(n):
        print(f"{pid[i]}\t{arrival[i]}\t{burst[i]}\t{priority[i]}\t"
              f"{completion[i]}\t{turnaround[i]}\t{waiting[i]}")

    avg_tat = sum(turnaround) / n
    avg_wt = sum(waiting) / n
    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")
processes = [
    [1, 0, 7, 2],
    [2, 1, 4, 3],
    [3, 2, 1, 4],
    [4, 3, 4, 5]
]

priority_preemptive_scheduling(processes)
