import lzma

class LZMA:
    def __init__(self) -> None:
        self.decompressor = lzma.LZMADecompressor()
        self.compressor = lzma.LZMACompressor()

    
    def compress(self, text:str) -> bytes:
        byte_text = bytes(text, "utf-16")                             #Conversion to bytes
        compressed_data = self.compressor.compress(byte_text)         #Invoke method and compress the data
        #compressed_data = str(compressed_data,"utf-16")              #Compressed data is byte, transform to str
        compressed_data += self.compressor.flush()
        return compressed_data

    def decompress(self, text:bytes) -> str:
        decompressed_data = self.decompressor.decompress(text)
        decompressed_string = str(decompressed_data, "utf-16")
        return decompressed_string



lzmaobj = LZMA()
string = "Francesco"
compressed = lzmaobj.compress(string)
decompressed = lzmaobj.decompress(compressed)