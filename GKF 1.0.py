from os import walk, path, system
from time import sleep


# Specific folder and file name to find
# Example of root_folder
# root_folder = "C:\\Users\\ilCONDORA\\Desktop\\3dmigoto\\Mods"
file_name = "merged.ini"


def search_file(root_folder, file_name):
    max_folder_length = 25  # Maximum length for the folder name

    # Traverse through the directory tree starting from the root folder
    for root, dirs, files in walk(root_folder):
        for file in files:
            # Check if the current file matches the desired file name
            if file == file_name:
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

                            # Print the folder name and value
                            print(f"Folder: {formatted_folder} Value: {value}")
                            break

while True:
    # Clear the command prompt
    system('cls')

    # Welcome message and version
    print("\nWelcome to Genshin KeySwap Finder by ilCONDORA")
    print("Version: 1.0\n\n")

    # Delay before execution
    sleep(2)

    # Search for the file and print the desired line
    search_file(root_folder, file_name)

    # Prompt user to restart or exit
    restart = input("\n\nPress 'R' to restart the program, or any other key to exit: ")
    if restart.upper() != 'R':
        print("\nProgram exited. Thank you for using Genshin KeySwap Finder, see you later!")
        sleep(3)
        break

    print("\nRestarting...")
    sleep(1)
