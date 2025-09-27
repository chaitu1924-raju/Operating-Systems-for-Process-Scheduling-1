import os

def copy_file(src, dest):
    try:
        src_fd = os.open(src, os.O_RDONLY)
    except FileNotFoundError:
        print(f"Source file '{src}' not found!")
        return
    dest_fd = os.open(dest, os.O_WRONLY | os.O_CREAT | os.O_TRUNC)
    while True:
        data = os.read(src_fd, 1024)
        if not data:
            break
        os.write(dest_fd, data)
    os.close(src_fd)
    os.close(dest_fd)
    print(f" File '{src}' successfully copied to '{dest}'")
if __name__ == "__main__":
    src_file = input("Enter source file name: ")
    dest_file = input("Enter destination file name: ")
    copy_file(src_file, dest_file)

