# Non-Preemptive Shortest Job First (SJF) Scheduling in Python

# Input: Process IDs, Arrival Times, and Burst Times
n = int(input("Enter number of processes: "))
processes = []

for i in range(n):
    at = int(input(f"Enter Arrival Time for Process P{i+1}: "))
    bt = int(input(f"Enter Burst Time for Process P{i+1}: "))
    processes.append({"pid": f"P{i+1}", "at": at, "bt": bt})

# Initialize tracking arrays
waiting_time = [0] * n
turnaround_time = [0] * n
completion_time = [0] * n
is_completed = [False] * n

time = 0
completed = 0

# Scheduling loop
while completed < n:
    # Find processes that have arrived and are not yet completed
    eligible = [p for p in processes if p["at"] <= time and not is_completed[processes.index(p)]]
    
    if eligible:
        # Select process with the shortest burst time
        current = min(eligible, key=lambda x: x["bt"])
        idx = processes.index(current)
        
        # Update times
        time += processes[idx]["bt"]
        completion_time[idx] = time
        turnaround_time[idx] = completion_time[idx] - processes[idx]["at"]
        waiting_time[idx] = turnaround_time[idx] - processes[idx]["bt"]
        
        # Mark as completed
        is_completed[idx] = True
        completed += 1
    else:
        # If no process has arrived yet, move time forward
        time += 1

# Display results
print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"{processes[i]['pid']}\t{processes[i]['at']}\t{processes[i]['bt']}\t{completion_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")

# Calculate averages
avg_wt = sum(waiting_time) / n
avg_tat = sum(turnaround_time) / n
print(f"\nAverage Waiting Time: {avg_wt:.2f}")
print(f"Average Turnaround Time: {avg_tat:.2f}")
