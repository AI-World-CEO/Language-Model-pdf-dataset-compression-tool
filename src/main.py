# main.py
import os
from src.pipeline import Pipeline
from utilities import create_directories


def main(pdf_path: str, output_path: str):
    print("Initializing pipeline...")

    # Create the necessary directories before running the pipeline
    directories = ['data/compressed', 'data/decompressed', 'data/raw',
                   'src/compression', 'src/preprocessing',
                   'src/evaluation', 'models', 'results',
                   'src/model', 'src/training']
    create_directories(directories)

    pipeline = Pipeline()
    print("Running pipeline...")
    result = pipeline.run_pipeline(pdf_path)
    print("Pipeline run completed, results obtained:")
    print(result)

    # Create the directory if it does not exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save the compressed dataset into a file
    with open(output_path, "w") as file:
        file.write(result)


if __name__ == "__main__":
    if 'COLAB_GPU' in os.environ:
        # Replace this with the path to your pdf file in Google Drive
        path_to_pdf = '/content/drive/My Drive/<Your Directory>/<Your PDF File>.pdf'

        # Replace this with the path to your desired output directory in Google Drive
        path_to_output = '/content/drive/My Drive/<Your Directory>/compressed_dataset.txt'
    else:
        # Replace this with the path to your pdf file on your local machine
        path_to_pdf = "<Your Directory>/<Your PDF File>.pdf"

        # Replace this with the path to your desired output directory on your local machine
        path_to_output = "<Your Directory>/compressed_dataset.txt"

    main(path_to_pdf, path_to_output)
