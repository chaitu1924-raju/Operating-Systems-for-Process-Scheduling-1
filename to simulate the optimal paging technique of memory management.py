def optimal_page_replacement(pages, frame_size):
    """
    Simulate Optimal page replacement algorithm.
    
    :param pages: List of page references
    :param frame_size: Number of frames in memory
    :return: Number of page faults and memory state after each step
    """
    memory = []
    page_faults = 0

    print("Page Reference\tMemory State\tPage Fault")
    print("-" * 50)

    for i in range(len(pages)):
        page = pages[i]
        page_fault = False

        if page not in memory:
            page_fault = True
            page_faults += 1
            if len(memory) < frame_size:
                memory.append(page)
            else:
                # Find page to replace: the one not used for the longest future time
                future_uses = []
                for mem_page in memory:
                    if mem_page in pages[i+1:]:
                        future_index = pages[i+1:].index(mem_page)
                    else:
                        future_index = float('inf')  # Not used again
                    future_uses.append(future_index)
                # Replace page with maximum future use index
                replace_index = future_uses.index(max(future_uses))
                memory[replace_index] = page

        print(f"{page}\t\t{memory}\t{'Yes' if page_fault else 'No'}")

    return page_faults

# ---------------- Main Program ----------------
if __name__ == "__main__":
    # Input page reference string and frame size
    pages = list(map(int, input("Enter page reference string (space-separated): ").split()))
    frame_size = int(input("Enter number of frames in memory: "))

    faults = optimal_page_replacement(pages, frame_size)
    print(f"\nTotal Page Faults: {faults}")
