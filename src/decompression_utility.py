import zlib
import base64
from typing import List


class DecompressionUtility:

    @staticmethod
    def decompress_dataset(compressed_dataset: str) -> List[str]:
        compressed = base64.b64decode(compressed_dataset.encode())
        decompressed = zlib.decompress(compressed)
        dataset = decompressed.decode().split(' ')
        return dataset
