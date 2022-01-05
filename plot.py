import matplotlib.pyplot as plt
import os
import json
import utils


def compare_algorithms(performances: dict, algorithms: list, entropies: list, sizes: list, colors: list) -> None:
    plt.xlabel('file size (byte)')
    plt.ylabel('compression ratio')
    plt.title("algorithms")
    entropy = entropies[int(len(entropies)/2)]

    for alg, color_ in zip(algorithms, colors):
        print(color_, alg) # ----------------------------------------------------------- DEBUG --------------------------------------------------
        y = utils.get_performances(performances, alg, entropy, sizes)
        plt.plot(sizes, y, color=color_, )

    plt.show()

def show_each_algorithms(performances: dict, algorithms: list, entropies: list, sizes: list, colors: list) -> None:
    for alg in algorithms:
        space_graph = plt.figure().add_subplot(projection='3d')
        space_graph.set_xlabel('source entropy')
        space_graph.set_ylabel('file size')
        space_graph.set_zlabel('compression ratio')
        plt.title(alg)

        for entropy, color in zip(entropies, colors):
            x = [entropy for _ in sizes]
            z = utils.get_performances(performances, alg, entropy, sizes)

            space_graph.plot(x, sizes, z, color)

        plt.show()

PERFORMANCES_FILE_NAME = "output.json"
PERFORMANCES_FOLDER = "output"

# load compression ratios from json file.
here = os.path.dirname(os.path.abspath(__file__))
PERFORMANCES_FOLDER_PATH = os.path.join(here, PERFORMANCES_FOLDER)
performances_path = os.path.join(PERFORMANCES_FOLDER_PATH, PERFORMANCES_FILE_NAME)
performances_file = open(performances_path)
PERFORMANCES = json.load(performances_file)
performances_file.close()

ALGORITHMS = utils.get_algorithms(PERFORMANCES)
SIZES = utils.get_sizes(PERFORMANCES)
ENTROPIES = utils.get_entropies(PERFORMANCES)
COLORS = ["red", "green", "blue", "orange", "black", "pink"]

show_each_algorithms(PERFORMANCES, ALGORITHMS, ENTROPIES, SIZES, COLORS)
compare_algorithms(PERFORMANCES, ALGORITHMS, ENTROPIES, SIZES, COLORS)



