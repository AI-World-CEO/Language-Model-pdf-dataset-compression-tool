# compression_utility.py
import zlib
import base64
from typing import List


class CompressionUtility:

    @staticmethod
    def compress_dataset(dataset: List[str]) -> str:
        text = ' '.join(dataset)
        compressed = zlib.compress(text.encode())
        compressed_str = base64.b64encode(compressed).decode()
        return compressed_str
