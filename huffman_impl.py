from huffman import HuffmanCoding

class Huffman():
    def __init__(self) -> None:
        self._name = "Huffman"

    def __str__(self) -> str:
        return self._name
    
    def compress(self, uncompressed_path: str, compressed_path: str) -> str:
        self.huffman = HuffmanCoding()
        self.huffman.compress(uncompressed_path , compressed_path)
        return compressed_path

    def decompress(self, compressed_path: str, uncompressed_path) -> str:
        self.huffman.decompress(compressed_path, uncompressed_path)
        return uncompressed_path