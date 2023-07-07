import os


def create_data_folders():
    raw_data_path = 'data/raw'

    # Check if the directory already exists
    if not os.path.exists(raw_data_path):
        # If not, create the directory
        os.makedirs(raw_data_path)
        print(f"'{raw_data_path}' directory created.")
    else:
        print(f"'{raw_data_path}' directory already exists.")


if __name__ == "__main__":
    create_data_folders()
