# ---------------- Linked File Allocation ----------------

class Block:
    """Represents a disk block"""
    def __init__(self, data):
        self.data = data
        self.next_block = None  # Pointer to the next block

class LinkedFile:
    """Represents a file using linked allocation"""
    def __init__(self, file_name):
        self.file_name = file_name
        self.first_block = None
        self.last_block = None
        self.block_count = 0

    def add_record(self, data):
        """Add a record as a new block"""
        new_block = Block(data)
        if self.first_block is None:
            # First block of the file
            self.first_block = self.last_block = new_block
        else:
            # Link new block to the last block
            self.last_block.next_block = new_block
            self.last_block = new_block
        self.block_count += 1
        print(f"Record '{data}' added as block {self.block_count}.")

    def display_records(self):
        """Display all records sequentially by following links"""
        if self.first_block is None:
            print(f"File '{self.file_name}' is empty.")
            return
        print(f"\nRecords in file '{self.file_name}':")
        current = self.first_block
        block_no = 1
        while current:
            print(f"Block {block_no}: {current.data}")
            current = current.next_block
            block_no += 1

    def access_record(self, block_no):
        """Access a specific block by following links"""
        if block_no < 1 or block_no > self.block_count:
            print("Invalid block number!")
            return
        current = self.first_block
        count = 1
        while count < block_no:
            current = current.next_block
            count += 1
        print(f"\nAccessing block {block_no}: {current.data}")

# ---------------- Main Program ----------------

def main():
    file_name = input("Enter file name: ")
    linked_file = LinkedFile(file_name)

    while True:
        print("\n--- Linked File Operations ---")
        print("1. Add Record")
        print("2. Display All Records")
        print("3. Access Specific Record")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            data = input("Enter record data: ")
            linked_file.add_record(data)
        elif choice == "2":
            linked_file.display_records()
        elif choice == "3":
            block_no = int(input("Enter block number to access: "))
            linked_file.access_record(block_no)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
