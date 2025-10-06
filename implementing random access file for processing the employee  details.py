import struct
import os

# Employee record format
# 'i' -> integer (ID), '20s' -> string of 20 bytes, 'f' -> float (salary)
record_format = 'i20sf'
record_size = struct.calcsize(record_format)
file_name = 'employees.dat'

# Function to write employee record at specific position
def write_employee(emp_id, name, salary, position=None):
    with open(file_name, 'r+b' if os.path.exists(file_name) else 'wb') as f:
        name_bytes = name.encode('utf-8')
        name_bytes = name_bytes.ljust(20, b'\x00')  # pad to 20 bytes
        packed_data = struct.pack(record_format, emp_id, name_bytes, salary)
        
        if position is not None:
            f.seek(position * record_size)
        else:
            f.seek(0, os.SEEK_END)
        f.write(packed_data)
        print(f"Employee {name} written successfully.")

# Function to read employee record at specific position
def read_employee(position):
    with open(file_name, 'rb') as f:
        f.seek(position * record_size)
        record_data = f.read(record_size)
        if not record_data:
            print("No record found at this position.")
            return
        emp_id, name_bytes, salary = struct.unpack(record_format, record_data)
        name = name_bytes.decode('utf-8').rstrip('\x00')
        print(f"Employee ID: {emp_id}, Name: {name}, Salary: {salary}")

# Function to display all employee records
def display_all_employees():
    if not os.path.exists(file_name):
        print("No employee records found.")
        return
    with open(file_name, 'rb') as f:
        position = 0
        while True:
            record_data = f.read(record_size)
            if not record_data:
                break
            emp_id, name_bytes, salary = struct.unpack(record_format, record_data)
            name = name_bytes.decode('utf-8').rstrip('\x00')
            print(f"Position {position} -> ID: {emp_id}, Name: {name}, Salary: {salary}")
            position += 1

# Menu-driven program
def main():
    while True:
        print("\n--- Random Access Employee File ---")
        print("1. Add Employee")
        print("2. Read Employee by Position")
        print("3. Display All Employees")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            emp_id = int(input("Enter Employee ID: "))
            name = input("Enter Employee Name: ")
            salary = float(input("Enter Salary: "))
            write_employee(emp_id, name, salary)
        elif choice == '2':
            position = int(input("Enter record position: "))
            read_employee(position)
        elif choice == '3':
            display_all_employees()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
