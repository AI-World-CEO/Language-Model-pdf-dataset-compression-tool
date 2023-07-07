import os
import tkinter as tk
from tkinter import filedialog
from src.pipeline import Pipeline


def compress_file(file_path):
    print("Initializing pipeline...")
    pipeline = Pipeline()
    print("Running pipeline...")
    result = pipeline.run_pipeline(file_path)
    print("Pipeline run completed, results obtained:")
    print(result)

    # Define your output path
    output_path = "C:\\output\\compressed_dataset.txt"

    # Create the directory if it does not exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save the compressed dataset into a file
    with open(output_path, "w") as file:
        file.write(result)


def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        print(f"Selected file: {file_path}")
        compress_file(file_path)


class Application(tk.Frame):  # Two blank lines before the class definition
    def __init__(self, master=None):
        super().__init__(master)
        self.quit_button = None
        self.select_button = None
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.select_button = tk.Button(self)
        self.select_button["text"] = "Select a PDF file"
        self.select_button["command"] = select_file
        self.select_button.grid(row=0, column=0)

        self.quit_button = tk.Button(self, text="QUIT", command=self.master.destroy)
        self.quit_button.grid(row=0, column=1)


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
