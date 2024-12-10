from json import loads
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as mpla

def plot_series(data):
    fig = plt.imshow(data[0])
    plt.colorbar()
    def animate(i):
        fig.set_data(data[i%len(data)])
    anim = mpla.FuncAnimation(plt.gcf(), animate, cache_frame_data=False, interval = 1000)
    plt.show()

def plot_frame(data):
    fig = plt.imshow(data)
    plt.colorbar()
    plt.show()

def load_json_frame(filename):
    with open(filename) as jsonfile:
        jsondata = loads(jsonfile.read())
    return jsondata

# Assuming filename convention nameconv_0, nameconv_1, etc loads all file data into a single list        
def load_json_series(name_0, no_Of_Frames):
    data = []
    filename = name_0.split('_')
    for i in range(no_Of_Frames):
        file = '.'.join(['_'.join(filename),"json"])
        with open(file) as jsonfile:
            data.append(loads(jsonfile.read()))
        filename[1] = str(1+ int(filename[1]))
    return data

X = [[[1,0],[0,1]],
     [[0.9,0.1],[0.1,0.9]],
     [[0.8,0.2],[0.2,0.8]],
     [[0.7,0.3],[0.3,0.7]],
     [[0.6,0.4],[0.4,0.6]],
     [[0.5,0.5],[0.5,0.5]],
     [[0.4,0.6],[0.6,0.4]],
     [[0.3,0.7],[0.7,0.3]],
     [[0.2,0.8],[0.8,0.2]],
     [[0.1,0.9],[0.9,0.1]],
     [[0,1],[1,0]],
     [[0.1,0.9],[0.9,0.1]],
     [[0.2,0.8],[0.8,0.2]],
     [[0.3,0.7],[0.7,0.3]],
     [[0.4,0.6],[0.6,0.4]],
     [[0.5,0.5],[0.5,0.5]],
     [[0.6,0.4],[0.4,0.6]],
     [[0.7,0.3],[0.3,0.7]],
     [[0.8,0.2],[0.2,0.8]],
     [[0.9,0.1],[0.1,0.9]]
     ]

plot_series(X)
