import wsn
import numpy as np

    
# initialise population
pop = [[]]
sink_distance = [[]]
energy = [[]]
source_distance = [[]]

for i in range(10):
    x, y, sod, sd0, sd1, sd2, sd3, e = make_wsn()
    # plot_wsn(x, y)
    p = np.array((x, y))
    p = p.reshape(2, -1).T
    pop.append(p)
    
    sink_distance.append(sd0)
    
    energy.append(e)
    source_distance.append(sod)

# fitness function

# energy component
fp1 = []
fp2 = []
for i in range(10):
    norm_energy = [x/max(energy[i]) for x in energy[i]]
    eth = 2
    et = np.sum(energy[i])
    fp1.append(np.sum(norm_energy) + num_nodes*(eth/et))
    

# distance component    
    avg_dist = np.sum(sink_distance[i])/num_nodes
    norm_dist = [x/max(sink_distance[i]) for x in sink_distance[i]]
    fp2.append(np.sum(norm_dist) + num_nodes/(avg_dist))

fit = []
for i in range(10):
    f = 1/(0.6*fp1[i] + 0.4*fp2[i])
    fit.append(f)

fit = fit[1:]
pop = pop[1:]
energy = energy[1:]
sink_distance = sink_distance[1:]
source_distance = source_distance[1:]

for i in range(len(pop)):
    min_ = i
    for j in range(i+1, len(pop)):
        if fit[min_] > fit[j-1]:
            min_ = j
    pop[i], pop[min_] = pop[min_], pop[i]
    # fit[i], fit[min_] = fit[min_], fit[i]

fit_idx = {x:i for i,x in enumerate(fit)}
tourn_fitness = [random.choice(fit) for _ in range(3)]

tourn_fit_idx = []
for i,x in enumerate(fit):
    if x in tourn_fitness:
        tourn_fit_idx.append(i)

tourn = [pop[i] for i in tourn_fit_idx]

