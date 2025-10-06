import os

def copy_file(src, dest):
    try:
        # Open source file (read-only)
        fd_src = os.open(src, os.O_RDONLY)
    except FileNotFoundError:
        print(f"Error: Source file '{src}' not found!")
        return
    
    # Open/create destination file (write-only)
    fd_dest = os.open(dest, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    
    while True:
        # Read 1024 bytes from source
        data = os.read(fd_src, 1024)
        if not data:  # If no more data → end of file
            break
        # Write data to destination
        os.write(fd_dest, data)
    
    # Close both files
    os.close(fd_src)
    os.close(fd_dest)
    print(f"✅ File copied from {src} → {dest}")

# ------------------------
# Example usage
# ------------------------
# First create a test file
with open("source.txt", "w") as f:
    f.write("Hello, this is a test file.\nThis content will be copied!")

# Now copy it
copy_file("source.txt", "destination.txt")

# Verify the content
with open("destination.txt", "r") as f:
    print("\nContents of destination.txt:")
    print(f.read())