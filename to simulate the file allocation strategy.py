# ---------------- Sequential File Allocation ----------------

class SequentialFile:
    def __init__(self, file_name):
        self.file_name = file_name
        self.records = []  # Stores records sequentially

    def add_record(self, record):
        """Add a new record to the file (sequentially)"""
        self.records.append(record)
        print(f"Record '{record}' added to file '{self.file_name}'.")

    def display_records(self):
        """Display all records sequentially"""
        if not self.records:
            print(f"File '{self.file_name}' is empty.")
            return
        print(f"\nAll records in file '{self.file_name}':")
        for i, record in enumerate(self.records, start=1):
            print(f"{i}. {record}")

    def access_record(self, record_no):
        """
        Access a specific record sequentially.
        record_no starts from 1.
        """
        if record_no < 1 or record_no > len(self.records):
            print("Invalid record number!")
            return
        print(f"\nAccessing record {record_no}:")
        # Simulate sequential access by reading all previous records
        for i in range(record_no):
            print(f"Reading record {i+1}: {self.records[i]}")

# ---------------- Main Program ----------------

def main():
    file_name = input("Enter file name: ")
    file = SequentialFile(file_name)

    while True:
        print("\n--- Sequential File Operations ---")
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
