from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import compress
import os
import json
from utils import compression_ratio

fig = plt.figure()
ax = plt.axes(projection='3d')

here = os.path.dirname(os.path.abspath(__file__))

PERFORMANCES_FILE_NAME = "output.json"
performances_folder = "output"
performances_path = os.path.join(performances_folder, PERFORMANCES_FILE_NAME)
performances_file = open(performances_path)

PERFORMANCES = json.load(performances_file)
performances_file.close()

compression_ratios = []
entropies = [0.5, 1.5, 2, 3]
sizes = [100, 1000, 10000, 100000]

for algorithm in PERFORMANCES:
    compression_ratios = []
    for entropy in PERFORMANCES[algorithm]:
        for size in PERFORMANCES[algorithm][entropy]:
            compression_ratios.append(PERFORMANCES[algorithm][entropy][size])
            ax.plot3D(sizes, entropies, compression_ratios, 'black')


ax.set_title('3D line plot')
plt.show()