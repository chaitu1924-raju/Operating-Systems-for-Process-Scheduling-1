import os
import stat

# ---------------- File Operations ----------------

def create_and_write_file(file_name, content):
    """Create a file and write content using open/write"""
    with open(file_name, "w+") as f:  # 'w+' creates file and allows read/write
        f.write(content)
    print(f"File '{file_name}' created and written successfully.")

def read_file(file_name):
    """Read file content"""
    with open(file_name, "r") as f:
        f.seek(0)  # Move file pointer to beginning
        content = f.read()
    print("\nFile Content:")
    print(content)

def file_status(file_name):
    """Get file metadata using os.stat"""
    s = os.stat(file_name)
    print("\nFile Status:")
    print(f"Size: {s.st_size} bytes")
    print(f"Last Modified: {s.st_mtime}")
    print(f"Permissions: {oct(s.st_mode)}")

# ---------------- Directory Operations ----------------

def list_directory(dir_name="."):
    """List files and directories (like opendir/readdir)"""
    print("\nDirectory Listing:")
    try:
        entries = os.listdir(dir_name)
        for entry in entries:
            path = os.path.join(dir_name, entry)
            entry_type = "File" if os.path.isfile(path) else "Directory"
            print(f"{entry} - {entry_type}")
    except FileNotFoundError:
        print("Directory not found.")

# ---------------- Main Program ----------------

if __name__ == "__main__":
    file_name = "example_unix_alt.txt"
    content = "Hello, this is a safe UNIX I/O demo in Python.\n"

    # File operations
    create_and_write_file(file_name, content)
    read_file(file_name)
    file_status(file_name)

    # Directory operations
    list_directory(".")




