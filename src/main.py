# main.py
import os
from src.pipeline import Pipeline


def main(pdf_path: str, output_path: str):
    print("Initializing pipeline...")
    pipeline = Pipeline()
    print("Running pipeline...")
    result = pipeline.run_pipeline(pdf_path)
    print("Pipeline run completed, results obtained:")
    print(result)

    # Create the directory if it does not exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save the compressed dataset into a file
    if result is not None:  # Add a check to ensure result is not None before writing to a file
        with open(output_path, "w") as file:
            file.write(result)
    else:
        print("No results to write to file.")


if __name__ == "__main__":
    main("C:\\Users\\Garry Anderson\\Music\\sim2940_technical.pdf",
         "C:\\output\\compressed_dataset.txt")
