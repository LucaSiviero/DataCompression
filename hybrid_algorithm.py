import os

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

    def compress(self, uncompressed_path: str, compressed_path: str) -> str:
        partial_files = []
        partial_file = compressed_path

        for alg_id, alg in enumerate(self.algorithms):
            if alg_id == len(self.algorithms) - 1:
                partial_file = compressed_path
            else:
                partial_file = partial_file + str(alg_id)
                partial_files.append(partial_file)

            alg.compress(uncompressed_path, partial_file)
            uncompressed_path = partial_file
        
        for file in partial_files:
            os.remove(file)


        return compressed_path
    
    def decompress(self, compressed_path: str, uncompressed_path: str) -> str:
        for alg in self.algorithms.reverse():
            compressed_path = alg.decompress(compressed_path, uncompressed_path)
            
        return uncompressed_path