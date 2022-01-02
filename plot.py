import matplotlib.pyplot as plt
import os
import json
import utils


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
SIZES = [1000, 10000, 100000]
ENTROPIES = utils.get_entropies(PERFORMANCES)
COLORS = ["red", "green", "blue"]

for alg in ALGORITHMS:
    space_graph = plt.figure().add_subplot(projection='3d')
    space_graph.set_xlabel('source entropy')
    space_graph.set_ylabel('file size')
    space_graph.set_zlabel('compression ratio')
    plt.title(alg)

    for entropy, color in zip(ENTROPIES, COLORS):
        x = [entropy for _ in SIZES]
        z = utils.get_performances(PERFORMANCES, alg, entropy, SIZES)

        space_graph.plot(x, SIZES, z, color)

    plt.show()
