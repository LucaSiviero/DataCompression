import matplotlib.pyplot as plt
import os
import json
import utils


def create_and_show_plot(x, y, z, color: str) -> None:
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot(x, y, z, color)
    plt.show()


PERFORMANCES_FILE_NAME = "output.json"
PERFORMANCES_FOLDER = "output"

here = os.path.dirname(os.path.abspath(__file__))
PERFORMANCES_FOLDER_PATH = os.path.join(here, PERFORMANCES_FOLDER)
performances_path = os.path.join(PERFORMANCES_FOLDER_PATH, PERFORMANCES_FILE_NAME)
performances_file = open(performances_path)
PERFORMANCES = json.load(performances_file)
performances_file.close()

ALGORITHMS = utils.get_algorithms(PERFORMANCES)
SIZES = [1000, 10000, 100000]
ENTROPIES = utils.get_entropies(PERFORMANCES)

for alg in ALGORITHMS:
    for entropy in ENTROPIES:
        x = [entropy for _ in SIZES]
        z = utils.get_performances(PERFORMANCES, alg, entropy, SIZES)
        create_and_show_plot(x, SIZES, z, "red")