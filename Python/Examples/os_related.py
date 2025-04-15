import os
import datetime
import win32security


def list_directories(directory):
    all_items = os.listdir(directory)
    folders = []
    for item in all_items:
        if os.path.isdir(os.path.join(directory, item)):
            folders.append(item)

    print("Directories in", current_dir, "are:", folders)


def find_files(directory):
    all_items = os.listdir(directory)
    files = []
    for item in all_items:
        if os.path.isfile(os.path.join(directory, item)):
            files.append(item)

    print("Files in", current_dir, "are:", files)


def get_file_info(file_path):
    if os.path.exists(file_path):
        file_size = os.path.getsize(file_path)
        modified_timestamp = os.path.getmtime(file_path)
        modified_date = datetime.datetime.fromtimestamp(modified_timestamp)
        try:
            security_descriptor = win32security.GetFileSecurity(
                file_path, win32security.OWNER_SECURITY_INFORMATION
            )
            owner_sid = security_descriptor.GetSecurityDescriptorOwner()
            owner_name, domain, type = win32security.LookupAccountSid(None, owner_sid)
        except Exception as e:
            owner_name = "Unknown"

        print("File:", file_path)
        print("Size:", file_size, "bytes")
        print("Last modified:", modified_date)
        print("Owner:", owner_name)
    else:
        print("File", file_path, "does not exist.")


# ************ Find Folders ************
current_dir = os.getcwd()
list_directories(current_dir)

# ************ Find Files ************
current_dir = os.getcwd()
find_files(current_dir)

# ************ File Meta Data ************
file_path = "example.txt"
get_file_info(file_path)


