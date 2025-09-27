def round_robin(processes, n, bt, quantum):
    wt = [0] * n 
    tat = [0] * n  
    rem_bt = bt[:]
    t = 0  
    while True:
        done = True
        for i in range(n):
            if rem_bt[i] > 0:
                done = False
                if rem_bt[i] > quantum:
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t += rem_bt[i]
                    wt[i] = t - bt[i]
                    rem_bt[i] = 0
        if done:
            break
    for i in range(n):
        tat[i] = bt[i] + wt[i]
    print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"P{i+1}\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}")
    print(f"\nAverage Waiting Time = {sum(wt)/n:.2f}")
    print(f"Average Turnaround Time = {sum(tat)/n:.2f}")
if __name__ == "__main__":
    n = int(input("Enter number of processes: "))
    processes = [i+1 for i in range(n)]
    bt = []
    for i in range(n):
        bt.append(int(input(f"Enter Burst Time for Process P{i+1}: ")))
    quantum = int(input("Enter Time Quantum: "))
    round_robin(processes, n, bt, quantum)
