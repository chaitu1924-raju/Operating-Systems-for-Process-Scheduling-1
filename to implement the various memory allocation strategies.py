def first_fit(memory_blocks, process_sizes):
    allocation = [-1] * len(process_sizes)
    blocks = memory_blocks.copy()

    for i, size in enumerate(process_sizes):
        for j, block in enumerate(blocks):
            if block >= size:
                allocation[i] = j
                blocks[j] -= size
                break
    return allocation

def best_fit(memory_blocks, process_sizes):
    allocation = [-1] * len(process_sizes)
    blocks = memory_blocks.copy()

    for i, size in enumerate(process_sizes):
        best_idx = -1
        for j, block in enumerate(blocks):
            if block >= size:
                if best_idx == -1 or blocks[j] < blocks[best_idx]:
                    best_idx = j
        if best_idx != -1:
            allocation[i] = best_idx
            blocks[best_idx] -= size
    return allocation

def worst_fit(memory_blocks, process_sizes):
    allocation = [-1] * len(process_sizes)
    blocks = memory_blocks.copy()

    for i, size in enumerate(process_sizes):
        worst_idx = -1
        for j, block in enumerate(blocks):
            if block >= size:
                if worst_idx == -1 or blocks[j] > blocks[worst_idx]:
                    worst_idx = j
        if worst_idx != -1:
            allocation[i] = worst_idx
            blocks[worst_idx] -= size
    return allocation

# Input memory blocks and process sizes
memory_blocks = [100, 500, 200, 300, 600]
process_sizes = [212, 417, 112, 426]

# First Fit
ff_alloc = first_fit(memory_blocks, process_sizes)
print("First Fit Allocation:", ff_alloc)

# Best Fit
bf_alloc = best_fit(memory_blocks, process_sizes)
print("Best Fit Allocation:", bf_alloc)

# Worst Fit
wf_alloc = worst_fit(memory_blocks, process_sizes)
print("Worst Fit Allocation:", wf_alloc)
