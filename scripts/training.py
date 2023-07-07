import os


def create_source_folders():
    model_scripts_path = 'src/model'
    training_scripts_path = 'src/training'

    # Check if the directories already exist
    # If not, create the directories
    for folder_path in [model_scripts_path, training_scripts_path]:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"'{folder_path}' directory created.")
        else:
            print(f"'{folder_path}' directory already exists.")


if __name__ == "__main__":
    create_source_folders()
