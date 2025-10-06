def calculate_need(maximum, allocation):
    """Calculate Need matrix"""
    need = []
    for i in range(len(maximum)):
        need.append([maximum[i][j] - allocation[i][j] for j in range(len(maximum[0]))])
    return need

def is_safe_state(processes, available, maximum, allocation):
    need = calculate_need(maximum, allocation)
    work = available.copy()
    finish = [False] * len(processes)
    safe_sequence = []

    while len(safe_sequence) < len(processes):
        allocated_in_this_round = False
        for i in range(len(processes)):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(len(work))):
                # Pretend to allocate resources
                for j in range(len(work)):
                    work[j] += allocation[i][j]
                finish[i] = True
                safe_sequence.append(processes[i])
                allocated_in_this_round = True
        if not allocated_in_this_round:
            break

    if len(safe_sequence) == len(processes):
        print("System is in a SAFE state.")
        print("Safe sequence:", " -> ".join(safe_sequence))
        return True
    else:
        print("System is NOT in a safe state. Deadlock may occur.")
        return False

def main():
    # Input
    processes = ['P0', 'P1', 'P2', 'P3', 'P4']
    available = [3, 3, 2]  # Available resources of each type

    maximum = [
        [7, 5, 3],  # Max demand for P0
        [3, 2, 2],  # P1
        [9, 0, 2],  # P2
        [2, 2, 2],  # P3
        [4, 3, 3]   # P4
    ]

    allocation = [
        [0, 1, 0],  # Currently allocated to P0
        [2, 0, 0],  # P1
        [3, 0, 2],  # P2
        [2, 1, 1],  # P3
        [0, 0, 2]   # P4
    ]

    # Check safe state
    is_safe_state(processes, available, maximum, allocation)

if __name__ == "__main__":
    main()
