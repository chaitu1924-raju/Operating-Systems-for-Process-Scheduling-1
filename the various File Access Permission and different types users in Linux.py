import os
import stat

# ------------------ 1. Create file and show default permissions ------------------
filename = "example.txt"

with open(filename, "w") as f:
    f.write("Hello Linux file permissions!\n")

# get file status
file_stat = os.stat(filename)
print("Step 1: File created")
print(f"File: {filename}")
print(f"Permissions: {stat.filemode(file_stat.st_mode)}")  # e.g. -rw-r--r--
print(f"Owner UID: {file_stat.st_uid}, Group GID: {file_stat.st_gid}")
print("-" * 50)

# ------------------ 2. Change permissions using chmod ------------------
print("Step 2: Changing permissions to 754 (rwxr-xr--)")
os.chmod(filename, 0o754)

file_stat = os.stat(filename)
print(f"Updated Permissions: {stat.filemode(file_stat.st_mode)}")  # -rwxr-xr--
print("-" * 50)

# ------------------ 3. Restrict access (owner only) ------------------
print("Step 3: Restricting access to owner only (600 => rw-------)")
os.chmod(filename, 0o600)

file_stat = os.stat(filename)
print(f"Updated Permissions: {stat.filemode(file_stat.st_mode)}")  # -rw-------
print("-" * 50)

# Show final result using Linux command
print("Step 4: Verify with 'ls -l'")
os.system(f"ls -l {filename}")
