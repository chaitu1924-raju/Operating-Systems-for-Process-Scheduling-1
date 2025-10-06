# Priority Scheduling Program (Non-Preemptive)

# Input: Process IDs, Burst Times, and Priorities
processes = []
num_processes = int(input("Enter number of processes: "))

for i in range(num_processes):
    bt = int(input(f"Enter Burst Time for Process P{i+1}: "))
    pr = int(input(f"Enter Priority for Process P{i+1} (lower number = higher priority): "))
    processes.append({"pid": f"P{i+1}", "bt": bt, "priority": pr})

# Sort processes based on Priority (highest first)
processes.sort(key=lambda x: x["priority"])

# Initialize waiting time and turnaround time
waiting_time = [0] * num_processes
turnaround_time = [0] * num_processes

# Calculate waiting time
for i in range(1, num_processes):
    waiting_time[i] = waiting_time[i-1] + processes[i-1]["bt"]

# Calculate turnaround time
for i in range(num_processes):
    turnaround_time[i] = waiting_time[i] + processes[i]["bt"]

# Display results
print("\nProcess\tBurst Time\tPriority\tWaiting Time\tTurnaround Time")
for i in range(num_processes):
    print(f"{processes[i]['pid']}\t{processes[i]['bt']}\t\t{processes[i]['priority']}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

# Calculate average times
avg_wt = sum(waiting_time) / num_processes
avg_tat = sum(turnaround_time) / num_processes

print(f"\nAverage Waiting Time: {avg_wt:.2f}")
print(f"Average Turnaround Time: {avg_tat:.2f}")
