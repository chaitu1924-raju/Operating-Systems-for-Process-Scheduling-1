def sjf_scheduling(processes, burst_times):
    n = len(processes)
    bt = burst_times.copy()
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completed = [False] * n
    current_time = 0
    completed_count = 0
    while completed_count < n:
        idx = -1
        min_bt = float('inf')
        for i in range(n):
            if not completed[i] and bt[i] < min_bt:
                min_bt = bt[i]
                idx = i
        waiting_time[idx] = current_time
        current_time += bt[idx]
        turnaround_time[idx] = waiting_time[idx] + bt[idx]
        completed[idx] = True
        completed_count += 1
    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i]}\t{burst_times[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
    avg_wt = sum(waiting_time) / n
    avg_tt = sum(turnaround_time) / n
    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tt:.2f}")
processes = ['P1', 'P2', 'P3', 'P4']
burst_times = [6, 8, 7, 3]
sjf_scheduling(processes, burst_times)
