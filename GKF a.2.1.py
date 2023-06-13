from os import walk, path, system, stat
from time import sleep
from math import ceil

# Specific folder and file name to find
root_folder = "C:\\Users\\ilCONDORA\\Desktop\\mods genshin\\3dmigoto\\Mods"
file_name = "merged.ini"

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

                            # Print the folder name, value and spacer
                            output = f"Folder: {formatted_folder} Value: {value}"
                            print(output)
                            spacer = "- " * ceil((len(output) / 2) + 1)
                            print(f"{spacer}\n")
                            break

    if not found_files:
        print("No files named 'merged.ini' found in the subfolders of the 'Mods' folder.\n")
        

# Check if the root_folder path is valid
if not path.exists(root_folder) or not path.isdir(root_folder):
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
        print("\nWelcome to Genshin KeySwap Finder by ilCONDORA")
        print("Version: a.2.1\n\n")

        sleep(2)

        # Search for the file and print the desired line
        search_file(root_folder, file_name)

        # Compare the current timestamp with the last timestamp
        while current_timestamp == last_timestamp:
            current_timestamp = stat(root_folder).st_mtime
            sleep(0.2)

        print("Change detected in the folder. Restarting...")

        # Update the last change timestamp
        last_timestamp = current_timestamp

        sleep(2)