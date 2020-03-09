import numpy as np
import matplotlib.pyplot as plt
import random

num_nodes = 20
length = 1000
breadth = 1000

def make_wsn():

    
    x_list = random.sample(range(0,1000), num_nodes)
    y_list = random.sample(range(0,1000), num_nodes)
    resid_energy = random.sample(range(0, 100), num_nodes)

    sx, sy = x_list[0], y_list[0]
    dx, dy = x_list[num_nodes-1], y_list[num_nodes-1]
    s = np.array((sx, sy))
    d = np.array((dx, dy))
    
    dx1, dy1 = x_list[num_nodes-2], y_list[num_nodes-2]
    d1 = np.array((dx1, dy1))
    
    dx2, dy2 = x_list[num_nodes-3], y_list[num_nodes-3]
    d2 = np.array((dx2, dy2))
    
    dx3, dy3 = x_list[num_nodes-4], y_list[num_nodes-4]
    d3 = np.array((dx3, dy3))

    source_dist = []
    sink_dist = []
    sink_dist1 = []
    sink_dist2 = []
    sink_dist3 = []
    for i in range(0, num_nodes):
        p = np.array((x_list[i], y_list[i]))
        source_dist.append(np.linalg.norm(s - p))
        sink_dist.append(np.linalg.norm(d - p))
        sink_dist1.append(np.linalg.norm(d1 - p))
        sink_dist2.append(np.linalg.norm(d2 - p))
        sink_dist3.append(np.linalg.norm(d3 - p))
    
    return x_list, y_list, source_dist, sink_dist, sink_dist1, sink_dist2, sink_dist3, resid_energy

def plot_wsn(x_list, y_list):
    colour = []
    colour.append('r')
    for i in range(1,num_nodes-4):
        colour.append('b')
    colour.append('g')
    colour.append('g')
    colour.append('g')
    colour.append('g')
    
    plt.subplot(2, 1, 1)
    plt.scatter(x_list, y_list, marker = '2', c = colour)
    plt.xlabel("Network Length")
    plt.ylabel("Network Width")
    
    plt.subplot(2, 1, 2)
    plt.plot(x_list, y_list, '-ok')
    plt.xlabel("Network Length")
    plt.ylabel("Network Width")
    
def get_avg_dist(source_dist, sink_dist):
    avg_sink_dist = np.sum(sink_dist)/num_nodes
    avg_source_dist = np.sum(source_dist)/num_nodes
    return avg_sink_dist, avg_source_dist
