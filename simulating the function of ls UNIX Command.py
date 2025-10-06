import os
import stat
import time

def simulate_ls(directory="."):
    """
    Simulate UNIX 'ls' command:
    Lists files and directories with details.
    """
    try:
        entries = os.listdir(directory)
        print(f"Listing of directory: {directory}\n")
        print(f"{'Name':<25} {'Type':<10} {'Size(Bytes)':<12} {'Permissions':<12} {'Last Modified':<20}")
        print("-" * 80)

        for entry in entries:
            path = os.path.join(directory, entry)
            # Determine type
            entry_type = "Directory" if os.path.isdir(path) else "File"
            # Get size
            size = os.path.getsize(path)
            # Get permissions
            perms = oct(os.stat(path).st_mode)[-3:]
            # Get last modified time
            mod_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(path)))

            print(f"{entry:<25} {entry_type:<10} {size:<12} {perms:<12} {mod_time:<20}")

    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
    except PermissionError:
        print(f"Permission denied to access '{directory}'.")

# ---------------- Main Program ----------------

if __name__ == "__main__":
    dir_name = input("Enter directory to list (default current directory): ") or "."
    simulate_ls(dir_name)
