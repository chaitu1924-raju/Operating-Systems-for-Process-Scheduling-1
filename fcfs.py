#4 FCFS CPU Scheduling Program

# Input: Process IDs and their Burst Times
processes = []
num_processes = int(input("Enter number of processes: "))

for i in range(num_processes):
    bt = int(input(f"Enter Burst Time for Process P{i+1}: "))
    processes.append({"pid": f"P{i+1}", "bt": bt})

# Initialize
waiting_time = [0] * num_processes
turnaround_time = [0] * num_processes

# FCFS Calculation
# Since all processes arrive at time 0, waiting time is sum of previous burst times
for i in range(1, num_processes):
    waiting_time[i] = waiting_time[i-1] + processes[i-1]["bt"]

# Turnaround time = Waiting time + Burst time
for i in range(num_processes):
    turnaround_time[i] = waiting_time[i] + processes[i]["bt"]

# Display results
print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
for i in range(num_processes):
    print(f"{processes[i]['pid']}\t{processes[i]['bt']}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

# Calculate average times
avg_wt = sum(waiting_time) / num_processes
avg_tat = sum(turnaround_time) / num_processes

print(f"\nAverage Waiting Time: {avg_wt:.2f}")
print(f"Average Turnaround Time: {avg_tat:.2f}")
