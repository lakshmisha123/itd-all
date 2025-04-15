#!/opt/homebrew/bin/python3
import os
import platform
import pwd

import psutil
import getpass


def get_current_working_directory():
    return os.getcwd()


def get_os_information():
    os_name = platform.system()
    os_version = platform.release()
    return os_name, os_version


def get_memory_information():
    memory = psutil.virtual_memory()
    return memory.total, memory.available, memory.used, memory.free


def get_current_user_information():
    return getpass.getuser()


def get_root_user_info():
    root_user = pwd.getpwuid(0)
    return root_user


if __name__ == "__main__":
    # Get current working directory
    current_directory = get_current_working_directory()
    print("Current working directory:", current_directory)

    # Get OS information
    os_name, os_version = get_os_information()
    print("Operating System:", os_name)
    print("Operating System Version:", os_version)

    # Get memory information
    total_memory, available_memory, used_memory, free_memory = get_memory_information()
    print("Total Memory:", total_memory)
    print("Available Memory:", available_memory)
    print("Used Memory:", used_memory)
    print("Free Memory:", free_memory)

    # Get current user information
    current_user = get_current_user_information()
    print("Current User:", current_user)

    # Get root user information
    root_user_info = get_root_user_info()
    print("Root User Info:", root_user_info)
