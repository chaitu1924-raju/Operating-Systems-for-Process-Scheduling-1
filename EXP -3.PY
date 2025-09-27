n = int(input("Enter number of processes: "))
burst_times = []
for i in range(n):
    bt = int(input(f"Enter Burst Time for Process P{i+1}: "))
    burst_times.append(bt)
waiting_times = [0] * n
turnaround_times = [0] * n
for i in range(1, n):
    waiting_times[i] = waiting_times[i-1] + burst_times[i-1]
for i in range(n):
    turnaround_times[i] = waiting_times[i] + burst_times[i]
print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
for i in range(n):
    print(f"P{i+1}\t{burst_times[i]}\t\t{waiting_times[i]}\t\t{turnaround_times[i]}")
avg_wait = sum(waiting_times) / n
avg_turnaround = sum(turnaround_times) / n
print(f"\nAverage Waiting Time: {avg_wait:.2f}")
print(f"Average Turnaround Time: {avg_turnaround:.2f}")
