from typing import List


class DatasetCreator:
    def create_dataset(self, text: str) -> List[str]:
        # Split text into sentences using the '.' character as the delimiter
        dataset = text.split('.')
        # Remove possible empty strings from list
        dataset = [sentence.strip() for sentence in dataset if sentence]
        return dataset
