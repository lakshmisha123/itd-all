import shutil
import os


def copy_file(source_file, destination_dir):
    shutil.copy(source_file, destination_dir)


def delete_file(file_path):
    os.remove(file_path)


def rename_file(old_name, new_name):
    os.rename(old_name, new_name)


def move_file(source_file, destination_dir):
    shutil.move(source_file, destination_dir)


# Example usage:
source_file = '/path/to/source/file.txt'
destination_dir = '/path/to/destination/'
new_file_name = '/path/to/destination/new_file_name.txt'

# Copy file
copy_file(source_file, destination_dir)

# Delete file
delete_file(source_file)

# Rename file
rename_file(destination_dir + 'file.txt', new_file_name)

# Move file
move_file(new_file_name, '/new/destination/directory/')
