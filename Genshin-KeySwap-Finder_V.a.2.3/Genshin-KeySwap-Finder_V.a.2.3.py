from os import walk, path, system, stat
from time import sleep
from math import ceil


version= "a.2.3"


# Reading the value of root_folder from the external text file
def read_root_folder_from_file():
    with open("path GKF.txt", 'r') as f:
        return f.readline().strip()

# Get the value of root_folder from the external text file
root_folder = read_root_folder_from_file()

# Specific file names to find
file_name = "merged.ini"
disabled_file_prefix = "DISABLED"


# Welcome message and version
def welcome_message():
    print("\nWelcome to Genshin KeySwap Finder by ilCONDORA")
    print(f"Version: {version}\n\n")


def search_file(root_folder, file_name):
    max_folder_length = 40  # Maximum length for the folder name
    found_files = False  # Variable to track if any files are found

    # Traverse through the directory tree starting from the root folder
    for root, dirs, files in walk(root_folder):
        for file in files:
            # Check if the current file matches the desired file name
            if file == file_name:
                found_files = True # Set found_files to True since a file is found

                # Get the absolute path of the current folder
                folder_path = path.abspath(root)

                # Extract the name of the folder from the path
                folder_name = path.basename(folder_path)

                # Construct the absolute file path
                file_path = path.join(root, file)

                # Open the file and search for the desired line
                with open(file_path, 'r') as f:
                    for line in f:
                        # Check if the line starts with "key ="
                        if line.startswith("key ="):
                            # Extract the value from the line
                            value = line.split("key =", 1)[1].strip()

                            # Format the folder name with a maximum width
                            formatted_folder = folder_name.ljust(max_folder_length)

                            # Search for disabled files in the first subdirectory
                            search_disabled_files(path.join(root, dirs[0]))

                            # Print the folder name, value, and spacer
                            output = f"Folder: {formatted_folder} Value: {value}"
                            print(output)
                            spacer = "- " * ceil((len(output) / 2) + 1)
                            print(f"{spacer}\n")

    if not found_files:
        welcome_message()
        print("No files named 'merged.ini' found in the subfolders of the 'Mods' folder.")
        input("\nPress ENTER to close the program or just close the window")


def search_disabled_files(folder):
    # Traverse through the files in the given folder
    for root, dirs, files in walk(folder):
        for file in files:
            # Check if the current file starts with the disabled_file_prefix
            if file.startswith(disabled_file_prefix):
                # Extract the character name from the file name
                character_name = file[len(disabled_file_prefix):].split(".")[0]

                # Print the character name
                print(f"Character: {character_name}")

                # Only print the first disabled file found
                return
            

# Check if the root_folder path is valid
if not path.exists(root_folder) or not path.isdir(root_folder):
    welcome_message()
    print("Invalid root folder path. Please modify the root_folder variable.")
    input("\nPress ENTER to close the program or just close the window")
else:
    # Get the initial timestamp of the folder
    last_timestamp = stat(root_folder).st_mtime

    while True:
        # Check the current timestamp of the folder
        current_timestamp = stat(root_folder).st_mtime

        # Clear the command prompt
        system('cls')

        # Welcome message and version
        welcome_message()

        sleep(2)

        # Search for the merged.ini file and print the desired line
        search_file(root_folder, file_name)

        # Compare the current timestamp with the last timestamp
        while current_timestamp == last_timestamp:
            current_timestamp = stat(root_folder).st_mtime
            sleep(0.2)

        print("Change detected in the folder. Restarting...")

        # Update the last change timestamp
        last_timestamp = current_timestamp

        sleep(2)
        