import os

# ---------- File Management Functions ----------

def create_file(file_name, content=""):
    """Create a new file with optional content"""
    with open(file_name, "w") as f:
        f.write(content)
    print(f"File '{file_name}' created successfully.")

def read_file(file_name):
    """Read and display file content"""
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            print(f"\nContent of '{file_name}':")
            print(f.read())
    else:
        print(f"File '{file_name}' does not exist.")

def write_file(file_name, content):
    """Append content to an existing file"""
    if os.path.exists(file_name):
        with open(file_name, "a") as f:
            f.write(content)
        print(f"Content appended to '{file_name}'.")
    else:
        print(f"File '{file_name}' does not exist.")

def rename_file(old_name, new_name):
    """Rename a file"""
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"File renamed from '{old_name}' to '{new_name}'.")
    else:
        print(f"File '{old_name}' does not exist.")

def delete_file(file_name):
    """Delete a file"""
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"File '{file_name}' deleted successfully.")
    else:
        print(f"File '{file_name}' does not exist.")

def list_files(directory="."):
    """List all files in the directory"""
    print(f"\nFiles in directory '{directory}':")
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    for f in files:
        print(f)

# ---------- Main Program ----------

def main():
    while True:
        print("\n--- File Management ---")
        print("1. Create File")
        print("2. Read File")
        print("3. Write to File")
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
            old_name = input("Enter current file name: ")
            new_name = input("Enter new file name: ")
            rename_file(old_name, new_name)
        elif choice == "5":
            file_name = input("Enter file name to delete: ")
            delete_file(file_name)
        elif choice == "6":
            directory = input("Enter directory path (default '.'): ") or "."
            list_files(directory)
        elif choice == "7":
            print("Exiting File Management...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
