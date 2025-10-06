# Round Robin Scheduling in Python

# Input: Process IDs, Arrival Times, and Burst Times
n = int(input("Enter number of processes: "))
processes = []

for i in range(n):
    at = int(input(f"Enter Arrival Time for Process P{i+1}: "))
    bt = int(input(f"Enter Burst Time for Process P{i+1}: "))
    processes.append({"pid": f"P{i+1}", "at": at, "bt": bt, "remaining_bt": bt})

# Time quantum
quantum = int(input("Enter Time Quantum: "))

# Initialize
time = 0
completed = 0
waiting_time = [0] * n
turnaround_time = [0] * n
completion_time = [0] * n

# Ready queue
queue = []
visited = [False] * n

# Add first process (those with AT=0)
for i in range(n):
    if processes[i]["at"] == 0:
        queue.append(i)
        visited[i] = True

# Run scheduling
while completed < n:
    if queue:
        idx = queue.pop(0)  # Get first process from queue
        if processes[idx]["remaining_bt"] > 0:
            if processes[idx]["remaining_bt"] > quantum:
                # Execute for quantum
                time += quantum
                processes[idx]["remaining_bt"] -= quantum
            else:
                # Finish process
                time += processes[idx]["remaining_bt"]
                processes[idx]["remaining_bt"] = 0
                completed += 1
                completion_time[idx] = time
                turnaround_time[idx] = completion_time[idx] - processes[idx]["at"]
                waiting_time[idx] = turnaround_time[idx] - processes[idx]["bt"]

        # Check for newly arrived processes
        for i in range(n):
            if processes[i]["at"] <= time and not visited[i] and processes[i]["remaining_bt"] > 0:
                queue.append(i)
                visited[i] = True

        # If process still has burst time left, put it back into queue
        if processes[idx]["remaining_bt"] > 0:
            queue.append(idx)
    else:
        time += 1  # No process is ready, move time forward

# Display results
print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"{processes[i]['pid']}\t{processes[i]['at']}\t{processes[i]['bt']}\t{completion_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")

# Averages
avg_wt = sum(waiting_time) / n
avg_tat = sum(turnaround_time) / n
print(f"\nAverage Waiting Time: {avg_wt:.2f}")
print(f"Average Turnaround Time: {avg_tat:.2f}")
