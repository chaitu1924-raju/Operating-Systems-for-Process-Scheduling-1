def fifo_page_replacement(pages, frame_size):
    """
    Simulate FIFO page replacement algorithm.
    
    :param pages: List of page references
    :param frame_size: Number of frames in memory
    :return: Number of page faults and memory state after each step
    """
    memory = []
    page_faults = 0
    fifo_queue = []

    print("Page Reference\tMemory State\tPage Fault")
    print("-" * 50)

    for page in pages:
        page_fault = False
        if page not in memory:
            page_fault = True
            page_faults += 1
            if len(memory) < frame_size:
                memory.append(page)
                fifo_queue.append(page)
            else:
                # Remove the oldest page (FIFO)
                oldest = fifo_queue.pop(0)
                memory.remove(oldest)
                memory.append(page)
                fifo_queue.append(page)
        print(f"{page}\t\t{memory}\t{'Yes' if page_fault else 'No'}")

    return page_faults

# ---------------- Main Program ----------------
if __name__ == "__main__":
    # Input page reference string and frame size
    pages = list(map(int, input("Enter page reference string (space-separated): ").split()))
    frame_size = int(input("Enter number of frames in memory: "))

    faults = fifo_page_replacement(pages, frame_size)
    print(f"\nTotal Page Faults: {faults}")
