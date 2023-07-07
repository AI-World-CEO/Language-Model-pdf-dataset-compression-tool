import os
from typing import List


def create_directories(directories: List[str]):
    """Creates directories if they don't exist.

    Args:
        directories (List[str]): List of directory paths to create.

    Raises:
        OSError: If there's an error creating a directory.
    """
    for directory in directories:
        try:
            os.makedirs(directory, exist_ok=True)
            print(f"'{directory}' directory created.")
        except OSError as e:
            print(f"Error creating '{directory}': {e}")
