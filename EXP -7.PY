def sjf_scheduling(processes):
    n = len(processes)
    processes.sort(key=lambda x: (x[1], x[0]))

    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n
    completion_time[0] = processes[0][1]
    turnaround_time[0] = completion_time[0]
    waiting_time[0] = turnaround_time[0] - processes[0][1]
    for i in range(1, n):
        completion_time[i] = completion_time[i-1] + processes[i][1]
        turnaround_time[i] = completion_time[i] - processes[i][0]
        waiting_time[i] = turnaround_time[i] - processes[i][1]
    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    total_wt, total_tat = 0, 0
    for i in range(n):
        total_wt += waiting_time[i]
        total_tat += turnaround_time[i]
        print(f"P{processes[i][0]}\t{processes[i][1]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {total_wt/n:.2f}")
    print(f"Average Turnaround Time: {total_tat/n:.2f}")
processes = [
    (1, 6),
    (2, 8),
    (3, 7),
    (4, 3)
]
sjf_scheduling(processes)
