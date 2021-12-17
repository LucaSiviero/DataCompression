from lzma import compress, decompress


class LZMA:
    def __init__(self) -> None:
        pass

    def compress(self, text:str) -> str:
        #Conversion to bytes for compress
        byte_text = bytes(text, "utf-8")                    
        #Invoke method and compress the data            
        compressed_data = compress(byte_text)                           
        return compressed_data

    def decompress(self, text:str) -> str:
        decompressed_data = decompress(text)
        decompressed_string = decompressed_data.decode("utf-8", "ignore")
        return decompressed_string