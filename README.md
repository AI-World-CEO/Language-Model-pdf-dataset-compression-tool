AIdatasetCompress: Language Model Dataset Compression Tool
Welcome to AIdatasetCompress, an efficient tool to convert PDF files into compressed datasets for training language models. Built with Python and GPT-4, this tool offers an intuitive way to feed your AI models with refined and relevant data.

Features
PDF Processing: The tool can process PDFs and extract text data for dataset generation.
Text Processing: Advanced text processing using NLTK, which includes tokenization, lemmatization, and removal of stop words and punctuation.
Data Compression: Efficient compression of large datasets to make the model training process faster and more efficient.
Installation
Before using AIdatasetCompress, make sure that you have Python installed on your machine.

To install the project dependencies, navigate to the project directory and run the following command:

Copy code
pip install -r requirements.txt
Usage
Please replace <Your Directory> and <Your PDF File>.pdf with your respective file paths.

If you're using Google Colab, replace the paths in the following format:

python
Copy code
At the bottom of the main.py code block replace the code with your PDF and location you want it to print out make sure there are two \\ whereever you see one
Example:if __name__ == "__main__":
    main("C:\\Users\\John Doe\\desktop\\sim2940_technical.pdf",  Replace entire code including ""
         "C:\\output\\compressed_dataset.txt")

License
This project is licensed under the terms of the MIT license.
python
Copy code
path_to_pdf = "<Your Directory>/<Your PDF File>.pdf"
path_to_output = "<Your Directory>/compressed_dataset.txt"
To execute the program, navigate to the project directory and run:

python
Copy code
python main.py
Contributions
We are open to contributions! If you find a bug or have ideas for new features, feel free to create an issue or a pull request.



