# Single-Level Directory Simulation in Python

class SingleLevelDirectory:
    def __init__(self):
        self.files = []  # list to store file names

    # Create a new file
    def create_file(self, filename):
        if filename in self.files:
            print(f"File '{filename}' already exists.")
        else:
            self.files.append(filename)
            print(f"File '{filename}' created successfully.")

    # Delete an existing file
    def delete_file(self, filename):
        if filename in self.files:
            self.files.remove(filename)
            print(f"File '{filename}' deleted successfully.")
        else:
            print(f"File '{filename}' not found.")

    # Search for a file
    def search_file(self, filename):
        if filename in self.files:
            print(f"File '{filename}' found in directory.")
        else:
            print(f"File '{filename}' not found.")

    # Display all files
    def display_files(self):
        if self.files:
            print("Files in directory:")
            for f in self.files:
                print(f" - {f}")
        else:
            print("Directory is empty.")

# Menu-driven program
def main():
    dir_system = SingleLevelDirectory()

    while True:
        print("\n--- Single Level Directory ---")
        print("1. Create File")
        print("2. Delete File")
        print("3. Search File")
        print("4. Display Files")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            filename = input("Enter file name to create: ")
            dir_system.create_file(filename)
        elif choice == '2':
            filename = input("Enter file name to delete: ")
            dir_system.delete_file(filename)
        elif choice == '3':
            filename = input("Enter file name to search: ")
            dir_system.search_file(filename)
        elif choice == '4':
            dir_system.display_files()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
