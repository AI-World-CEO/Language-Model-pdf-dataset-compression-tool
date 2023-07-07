from typing import Optional
from dataset_creator import DatasetCreator
from src.logger import my_logger as logger
from src.compression_utility import CompressionUtility
from src.text_processor import TextProcessor
from src.textbook_scanner import TextbookScanner


class Pipeline:

    @staticmethod
    def run_pipeline(pdf_path: str) -> Optional[str]:
        try:
            scanner = TextbookScanner()
            processor = TextProcessor()
            creator = DatasetCreator()
            utility = CompressionUtility()

            text = scanner.scan_textbook(pdf_path)
            processed_text = processor.process_text_advanced(text)
            dataset = creator.create_dataset(processed_text)
            compressed_dataset = utility.compress_dataset(dataset)

            return compressed_dataset

        except FileNotFoundError:
            logger.error(f"File not found: {pdf_path}")
            return None
        except PermissionError:
            logger.error(f"No permission to read file: {pdf_path}")
            return None
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
            return None
