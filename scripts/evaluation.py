import os


def create_source_folder():
    evaluation_scripts_path = 'src/evaluation'

    # Check if the directory already exist
    # If not, create the directory
    if not os.path.exists(evaluation_scripts_path):
        os.makedirs(evaluation_scripts_path)
        print(f"'{evaluation_scripts_path}' directory created.")
    else:
        print(f"'{evaluation_scripts_path}' directory already exists.")


if __name__ == "__main__":
    create_source_folder()
