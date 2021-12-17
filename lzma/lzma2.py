import lzma
from Source.first_order_source import FirstOrderSource
from alphabets import alphabets_

class LZMA:
    def __init__(self) -> None:
        None

    def compress(self, text: str) -> str:
        text_as_byte = bytes(text, "utf-8")
        compressed_as_byte = lzma.compress(text_as_byte)
        print(len(compressed_as_byte)/len(text_as_byte))

        return compressed_as_byte.decode("utf-8")
    
    def decompress(self, coded_text: str) -> str:
        text_as_byte = bytes(coded_text, "utf-16")
        decompressed = lzma.decompress(text_as_byte)
        return decompressed.decode("utf-16")



fos = FirstOrderSource(alphabets_["K-ARY-50"])
text = fos.generate_text(100000)

lzm = LZMA()


comp = lzm.compress(text)