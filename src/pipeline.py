from textbook_scanner import TextbookScanner
from text_processor import TextProcessor
from dataset_creator import DatasetCreator
from compression_utility import CompressionUtility
from src.logger import setup_logger  # Assuming the logger setup function is available in the src.logger module


class Pipeline:

    def __init__(self):
        self.logger = setup_logger('pipeline_logger', 'pipeline.log')  # Set up a logger for the pipeline class

    def run_pipeline(self, pdf_path: str) -> str:
        try:
            scanner = TextbookScanner()
            processor = TextProcessor()
            creator = DatasetCreator()
            utility = CompressionUtility()

            text = scanner.scan_textbook(pdf_path)
            processed_text = processor.process_text_advanced(text)  # Using the correct method from TextProcessor
            dataset = creator.create_dataset(processed_text)
            compressed_dataset = utility.compress_dataset(dataset)

            return compressed_dataset

        except FileNotFoundError:
            self.logger.error(f"File not found: {pdf_path}")  # Using the logger to log errors
            return None
        except Exception as e:
            self.logger.error(f"An error occurred: {str(e)}")  # Using the logger to log exceptions
            return None
