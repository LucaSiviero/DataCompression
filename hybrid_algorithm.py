class HybridAlgorithm():
    def __init__(self, algorithms: list):
        self.algorithms = algorithms
    
    def __str__(self) -> str:
        text = ""

        for algorithm in self.algorithms: text = text + f"{algorithm}_"

        return text


    def compress(self, text: str) -> str:
        compressed_text = text

        for algorithm in self.algorithms:
            compressed_text = algorithm.compress(compressed_text)
        
        return compressed_text