from huffman import HuffmanCoding

class HybridAlgorithm():
    def __init__(self, algorithms: list):
        self.algorithms = algorithms
    
    def __str__(self) -> str:
        text = ""

        if len(self.algorithms) == 1:
            return str(self.algorithms[0])
        
        for algorithm in self.algorithms[:-1]: 
            text = text + f"{algorithm}_"
        text = text + str(self.algorithms[-1])

        return text

    def __hash__(self) -> str:
        return str(self)

    def _update_algorithms(self) -> None:
        algs = []

        for alg in self.algorithms:
            if str(alg) == "Huffman":
                algs.append(HuffmanCoding())
            else:
                algs.append(alg)
        
        self.algorithms = algs

    def compress(self, text: str) -> str:
        self._update_algorithms()

        compressed_text = text

        for algorithm in self.algorithms:
            compressed_text = algorithm.compress(compressed_text)
        
        return compressed_text
    
    def decompress(self, text:str) -> str:
        decompressed_text = text
        
        for algorithm in self.algorithms[::-1]:
            decompressed_text = algorithm.decompress(decompressed_text)

        return decompressed_text