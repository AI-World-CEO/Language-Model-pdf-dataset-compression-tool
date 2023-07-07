import os


def create_project_folders():
    # Define the directories to be created
    directories = ['models', 'results']

    for directory in directories:
        # Check if the directory already exist
        # If not, create the directory
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"'{directory}' directory created.")
        else:
            print(f"'{directory}' directory already exists.")


if __name__ == "__main__":
    create_project_folders()
