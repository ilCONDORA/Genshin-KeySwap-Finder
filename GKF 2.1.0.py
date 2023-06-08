from os import walk, path, system
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self):
        self.is_running = False  # Flag to indicate if the program is running

    def on_any_event(self, event):
        if event.is_directory:
            if event.event_type == 'created' or event.event_type == 'deleted':
                # Check if the program is already running
                if not self.is_running:
                    print("\nFolder has been updated. Restarting...")
                    sleep(2)
                    self.is_running = True  # Set the flag to indicate the program is running
                    restart_program()

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

def restart_program():
    # Clear the command prompt
    system('cls')

    # Welcome message and version
    print("\nWelcome to Genshin KeySwap Finder Program")
    print("Version: 2.1\n\n")

    # Delay before execution
    sleep(3)

    # Specific folder and file name to find
    # Example of root_folder
    # root_folder = "C:\\Users\\ilCONDORA\\Desktop\\3dmigoto\\Mods"
    file_name = "merged.ini"

    # Search for the file and print the desired line
    search_file(root_folder, file_name)

    # Set the flag to indicate the program has finished running
    event_handler.is_running = False

if __name__ == "__main__":
    # Initialize the file change handler and observer
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path="C:\\Users\\AndreaCondorelli\\Desktop\\Genshin\\mods", recursive=True)
    observer.start()

    try:
        # Run the program
        restart_program()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
