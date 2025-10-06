def worst_fit(memory_blocks, process_sizes):
    allocation = [-1] * len(process_sizes)  # Stores allocated block index
    blocks = memory_blocks.copy()           # Copy of memory blocks

    for i, size in enumerate(process_sizes):
        worst_idx = -1
        for j, block in enumerate(blocks):
            if block >= size:
                if worst_idx == -1 or blocks[j] > blocks[worst_idx]:
                    worst_idx = j
        if worst_idx != -1:
            allocation[i] = worst_idx
            blocks[worst_idx] -= size

    return allocation, blocks

# Input memory blocks and process sizes
memory_blocks = [100, 500, 200, 300, 600]
process_sizes = [212, 417, 112, 426]

allocation, remaining_blocks = worst_fit(memory_blocks, process_sizes)

# Display allocation
print("Process No. | Process Size | Block Allocated")
for i, size in enumerate(process_sizes):
    if allocation[i] != -1:
        print(f"{i+1:^11} | {size:^12} | {allocation[i]+1:^14}")
    else:
        print(f"{i+1:^11} | {size:^12} | {'Not Allocated':^14}")

print("\nRemaining Memory Blocks:", remaining_blocks)
