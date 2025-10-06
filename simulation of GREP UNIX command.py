import os
import re

def grep_simulate(pattern, file_name):
    """
    Simulate UNIX grep command.
    Search for a pattern in the given file and display matching lines.
    """
    if not os.path.exists(file_name):
        print(f"File '{file_name}' does not exist.")
        return

    with open(file_name, "r") as f:
        lines = f.readlines()

    print(f"\nSearching for pattern '{pattern}' in file '{file_name}':\n")
    found = False
    for i, line in enumerate(lines, start=1):
        if re.search(pattern, line):
            print(f"{i}: {line.strip()}")
            found = True

    if not found:
        print("No matching lines found.")

# ---------------- Main Program ----------------

if __name__ == "__main__":
    file_name = input("Enter file name to search: ")
    pattern = input("Enter search pattern: ")
    grep_simulate(pattern, file_name)
