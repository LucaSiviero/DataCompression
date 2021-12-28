class HybridAlgorithm():
    def __init__(self, algorithms: list):
        self.algorithms = algorithms
    
    def __str__(self) -> str:
        text = ""

        if len(self.algorithms) == 1:
            return str(self.algorithms[0])

        for algorithm in self.algorithms: 
            text = text + f"{algorithm}_"

        return text

    def __hash__(self) -> str:
        return str(self)

    def compress(self, text: str) -> str:
        compressed_text = text

        for algorithm in self.algorithms:
            compressed_text = algorithm.compress(compressed_text)
        
        return compressed_text