# ---------------- Indexed File Allocation ----------------

class IndexedFile:
    def __init__(self, file_name):
        self.file_name = file_name
        self.index_block = []  # Stores pointers (indices) to data blocks
        self.data_blocks = []  # Actual data blocks

    def add_record(self, record):
        """Add a record to a new data block and update index block"""
        block_number = len(self.data_blocks)
        self.data_blocks.append(record)      # Store record in a data block
        self.index_block.append(block_number)  # Pointer to the block in index block
        print(f"Record '{record}' added at block {block_number} (indexed).")

    def display_records(self):
        """Display all records using index block"""
        if not self.index_block:
            print(f"File '{self.file_name}' has no records.")
            return
        print(f"\nAll records in file '{self.file_name}' (via index block):")
        for i, block_no in enumerate(self.index_block, start=1):
            print(f"{i}. {self.data_blocks[block_no]} (Block {block_no})")

    def access_record(self, record_no):
        """Access a specific record using index block"""
        if record_no < 1 or record_no > len(self.index_block):
            print("Invalid record number!")
            return
        block_no = self.index_block[record_no - 1]
        print(f"\nAccessing record {record_no} via index block:")
        print(f"Record Data: {self.data_blocks[block_no]} (Block {block_no})")

# ---------------- Main Program ----------------

def main():
    file_name = input("Enter file name: ")
    file = IndexedFile(file_name)

    while True:
        print("\n--- Indexed File Operations ---")
        print("1. Add Record")
        print("2. Display All Records")
        print("3. Access Specific Record")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            record = input("Enter record data: ")
            file.add_record(record)
        elif choice == "2":
            file.display_records()
        elif choice == "3":
            record_no = int(input("Enter record number to access: "))
            file.access_record(record_no)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
