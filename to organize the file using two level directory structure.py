# Two-Level Directory Simulation in Python

class TwoLevelDirectory:
    def __init__(self):
        self.directories = {}  # Dictionary: {username: [files]}

    # Create a file in a specific directory
    def create_file(self, username, filename):
        if username not in self.directories:
            self.directories[username] = []
        if filename in self.directories[username]:
            print(f"File '{filename}' already exists in directory '{username}'.")
        else:
            self.directories[username].append(filename)
            print(f"File '{filename}' created successfully in directory '{username}'.")

    # Delete a file from a specific directory
    def delete_file(self, username, filename):
        if username in self.directories and filename in self.directories[username]:
            self.directories[username].remove(filename)
            print(f"File '{filename}' deleted successfully from directory '{username}'.")
        else:
            print(f"File '{filename}' not found in directory '{username}'.")

    # Search for a file in a specific directory
    def search_file(self, username, filename):
        if username in self.directories and filename in self.directories[username]:
            print(f"File '{filename}' found in directory '{username}'.")
        else:
            print(f"File '{filename}' not found in directory '{username}'.")

    # Display all files in all directories
    def display_files(self):
        if not self.directories:
            print("No directories found.")
            return
        for username, files in self.directories.items():
            print(f"\nDirectory '{username}':")
            if files:
                for f in files:
                    print(f" - {f}")
            else:
                print("  (No files)")

# Menu-driven program
def main():
    dir_system = TwoLevelDirectory()

    while True:
        print("\n--- Two Level Directory ---")
        print("1. Create File")
        print("2. Delete File")
        print("3. Search File")
        print("4. Display Files")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice in ['1', '2', '3']:
            username = input("Enter directory/user name: ")
            filename = input("Enter file name: ")
            if choice == '1':
                dir_system.create_file(username, filename)
            elif choice == '2':
                dir_system.delete_file(username, filename)
            elif choice == '3':
                dir_system.search_file(username, filename)
        elif choice == '4':
            dir_system.display_files()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
