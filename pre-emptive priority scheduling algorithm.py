# Preemptive Priority Scheduling Program in Python

# Input: Process IDs, Arrival Times, Burst Times, and Priorities
n = int(input("Enter number of processes: "))
processes = []

for i in range(n):
    at = int(input(f"Enter Arrival Time for Process P{i+1}: "))
    bt = int(input(f"Enter Burst Time for Process P{i+1}: "))
    pr = int(input(f"Enter Priority for Process P{i+1} (lower number = higher priority): "))
    processes.append({"pid": f"P{i+1}", "at": at, "bt": bt, "priority": pr, "remaining_bt": bt})

time = 0
completed = 0
waiting_time = [0] * n
turnaround_time = [0] * n
completion_time = [0] * n

# Keep running until all processes are completed
while completed < n:
    # Select process with highest priority that has arrived and is not finished
    eligible = [p for p in processes if p["at"] <= time and p["remaining_bt"] > 0]
    
    if eligible:
        # Select process with highest priority (lowest number)
        current = min(eligible, key=lambda x: x["priority"])
        idx = processes.index(current)
        
        # Execute for 1 unit of time
        processes[idx]["remaining_bt"] -= 1
        time += 1
        
        # If process is completed
        if processes[idx]["remaining_bt"] == 0:
            completed += 1
            completion_time[idx] = time
            turnaround_time[idx] = completion_time[idx] - processes[idx]["at"]
            waiting_time[idx] = turnaround_time[idx] - processes[idx]["bt"]
    else:
        # If no process has arrived yet, just move time forward
        time += 1

# Display results
print("\nProcess\tAT\tBT\tPriority\tCT\tTAT\tWT")
for i in range(n):
    print(f"{processes[i]['pid']}\t{processes[i]['at']}\t{processes[i]['bt']}\t{processes[i]['priority']}\t\t{completion_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")

# Calculate averages
avg_wt = sum(waiting_time) / n
avg_tat = sum(turnaround_time) / n
print(f"\nAverage Waiting Time: {avg_wt:.2f}")
print(f"Average Turnaround Time: {avg_tat:.2f}")
