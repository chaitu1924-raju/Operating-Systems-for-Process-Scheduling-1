import os

def create_file(file_name, content=""):
    """Create a new file and write initial content"""
    fd = os.open(file_name, os.O_RDWR | os.O_CREAT)  # Open or create file
    os.write(fd, content.encode())
    os.close(fd)
    print(f"File '{file_name}' created successfully.")

def read_file(file_name):
    """Read content from a file"""
    fd = os.open(file_name, os.O_RDONLY)
    content = os.read(fd, 1024)  # Read up to 1024 bytes
    os.close(fd)
    print(f"Content of '{file_name}':")
    print(content.decode())

def write_file(file_name, content):
    """Write content to a file (append mode)"""
    fd = os.open(file_name, os.O_RDWR | os.O_APPEND)
    os.write(fd, content.encode())
    os.close(fd)
    print(f"Content appended to '{file_name}'.")

def rename_file(old_name, new_name):
    """Rename a file"""
    os.rename(old_name, new_name)
    print(f"File '{old_name}' renamed to '{new_name}'.")

def delete_file(file_name):
    """Delete a file"""
    os.remove(file_name)
    print(f"File '{file_name}' deleted successfully.")

def list_files(directory="."):
    """List files in the directory"""
    files = os.listdir(directory)
    print(f"Files in directory '{directory}': {files}")

# Menu-driven program
def main():
    while True:
        print("\n--- UNIX File Management using System Calls ---")
        print("1. Create File")
        print("2. Read File")
        print("3. Write File")
        print("4. Rename File")
        print("5. Delete File")
        print("6. List Files in Directory")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            file_name = input("Enter file name: ")
            content = input("Enter initial content (optional): ")
            create_file(file_name, content)
        elif choice == "2":
            file_name = input("Enter file name to read: ")
            read_file(file_name)
        elif choice == "3":
            file_name = input("Enter file name to write: ")
            content = input("Enter content to append: ")
            write_file(file_name, content)
        elif choice == "4":
            old_name = input("Enter old file name: ")
            new_name = input("Enter new file name: ")
            rename_file(old_name, new_name)
        elif choice == "5":
            file_name = input("Enter file name to delete: ")
            delete_file(file_name)
        elif choice == "6":
            directory = input("Enter directory (default '.'): ") or "."
            list_files(directory)
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

