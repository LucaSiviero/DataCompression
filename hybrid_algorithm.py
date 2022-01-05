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

    def compress(self, text: str) -> str:
        compressed_text = text

        for algorithm in self.algorithms:
            compressed_text = algorithm.compress(compressed_text)
        
        return compressed_text
    
    def decompress(self, text:str) -> str:
        decompressed_text = text
        
        for algorithm in self.algorithms[::-1]:
            decompressed_text = algorithm.decompress(decompressed_text)

        return decompressed_text