def lru_page_replacement(pages, frame_size):
    """
    Simulate LRU page replacement algorithm.
    
    :param pages: List of page references
    :param frame_size: Number of frames in memory
    :return: Number of page faults and memory state after each step
    """
    memory = []
    page_faults = 0
    recent_usage = []  # Track usage order

    print("Page Reference\tMemory State\tPage Fault")
    print("-" * 50)

    for page in pages:
        page_fault = False
        if page not in memory:
            page_fault = True
            page_faults += 1
            if len(memory) < frame_size:
                memory.append(page)
            else:
                # Find least recently used page (first in recent_usage list)
                lru_page = recent_usage.pop(0)
                memory.remove(lru_page)
                memory.append(page)
        else:
            # If page already in memory, remove it from recent_usage to update
            recent_usage.remove(page)
        # Update recent usage
        recent_usage.append(page)
        print(f"{page}\t\t{memory}\t{'Yes' if page_fault else 'No'}")

    return page_faults

# ---------------- Main Program ----------------
if __name__ == "__main__":
    # Input page reference string and frame size
    pages = list(map(int, input("Enter page reference string (space-separated): ").split()))
    frame_size = int(input("Enter number of frames in memory: "))

    faults = lru_page_replacement(pages, frame_size)
    print(f"\nTotal Page Faults: {faults}")
