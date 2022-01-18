from lzma import compress, decompress


class LZMA:
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return "LZMA"

    def compress(self, uncompressed_path: str, compressed_path: str) -> str:
        with open(uncompressed_path, "rb") as file:
            byte_content = file.read()

        #Invoke method and compress the data            
        compressed_data = compress(byte_content)

        with open(compressed_path, "wb") as file:
            file.write(compressed_data)                           



    def decompress(self, text:str) -> str:
        decompressed_data = decompress(text)
        decompressed_string = decompressed_data.decode("utf-8", "ignore")
        return decompressed_string