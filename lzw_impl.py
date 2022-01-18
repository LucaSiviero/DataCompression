import lzw

class LZW():
    def __init__(self):
        self._name = "LZW"

    def __str__(self) -> str:
        return self._name

    def compress(self, uncompressed_path: str, compressed_path: str) -> str:
        infile     = lzw.readbytes(uncompressed_path)
        compressed = lzw.compress(infile)
        lzw.writebytes(compressed_path, compressed)
        return compressed_path

    def decompress(self, compressed_path: str, uncompressed_path) -> str:
        infile       = lzw.readbytes(compressed_path)
        uncompressed = lzw.decompress(infile)
        lzw.writebytes(uncompressed_path, uncompressed)
        return uncompressed_path
