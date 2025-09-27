class Process:
    def __init__(self, pid, burst_time, priority):
        self.pid = pid
        self.burst_time = burst_time
        self.priority = priority
        self.waiting_time = 0
        self.turnaround_time = 0
def priority_scheduling(processes):
    processes.sort(key=lambda x: x.priority)
    total_waiting_time = 0
    total_turnaround_time = 0
    processes[0].waiting_time = 0
    for i in range(1, len(processes)):
        processes[i].waiting_time = processes[i - 1].waiting_time + processes[i - 1].burst_time
        total_waiting_time += processes[i].waiting_time
    for i in range(len(processes)):
        processes[i].turnaround_time = processes[i].waiting_time + processes[i].burst_time
        total_turnaround_time += processes[i].turnaround_time
    print("PID\tPriority\tBurst Time\tWaiting Time\tTurnaround Time")
    for p in processes:
        print(f"{p.pid}\t{p.priority}\t\t{p.burst_time}\t\t{p.waiting_time}\t\t{p.turnaround_time}")

    print("\nAverage Waiting Time:", total_waiting_time / len(processes))
    print("Average Turnaround Time:", total_turnaround_time / len(processes))
if __name__ == "__main__":
    processes = [
        Process(1, 10, 3),
        Process(2, 1, 1),
        Process(3, 2, 4),
        Process(4, 1, 5),
        Process(5, 5, 2)
    ]
    priority_scheduling(processes)
