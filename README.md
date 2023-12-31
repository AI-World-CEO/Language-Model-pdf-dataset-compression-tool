AIdatasetCompress: Language Model Dataset Compression Tool 

Welcome to AIdatasetCompress, an efficient tool to convert PDF files into compressed datasets for training language models. Built with Python and GPT-4, this tool offers an intuitive way to feed your AI models with refined and relevant data. 

  

Features 

This new version completely takes the pdf and organizes it all the way to tokenized format in 3 pkl files such as Train.pkl test.pkl and val.pkl for testing and training ready for all three phases of your model
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

At the bottom of the main.py code block replaces the code with your PDF and location you want it to print out make sure there are two \\ wherever you see one, sometimes the pdf may have special characters in it, you place an r at the beginning of the pdf file, like below 

  

def main(): 

    print("Scanning textbook...") 

    scanner = TextbookScanner() 

    raw_text = scanner.scan_textbook(   place pdf here sometimes you may need to place an r at the start of the file

        r"C:\\Users\\John Doe\\Downloads\01. Beginning Project Management author Russell W. harnall, John M. ureston.pdf") 

  

  

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

  

  

 

 
