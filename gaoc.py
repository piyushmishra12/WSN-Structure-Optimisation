import wsn
import numpy as np
import matplotlib.pyplot as plt

    
# initialise population
pop = []
sink_distance = []
energy = []
source_distance = []

for i in range(10):
    x, y, sod, sd0, sd1, sd2, sd3, e = make_wsn()
    # plot_wsn(x, y)
    p = np.array((x, y))
    p = p.reshape(2, -1).T
    pop.append(p)
    
    sink_distance.append(sd0)
    
    energy.append(e)
    source_distance.append(sod)

avg_fitness = []
for epoch in range(10):
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

# fit = fit[1:]
# pop = pop[1:]
# energy = energy[1:]
# sink_distance = sink_distance[1:]
# source_distance = source_distance[1:]

    for i in range(len(pop)):
        for j in range(i+1, len(pop)):
            if fit[i] > fit[j]:
                pop[i], pop[j] = pop[j], pop[i]
                fit[i], fit[j] = fit[j], fit[i]
                energy[i], energy[j] = energy[j], energy[i]

# fit_idx = {x:i for i,x in enumerate(fit)}
# tourn_fitness = [random.choice(fit) for _ in range(4)]

# tourn_fit_idx = []
# for i,x in enumerate(fit):
#     if x in tourn_fitness:
#         tourn_fit_idx.append(i)

    tourn = pop[:4]

    nextgen_pop = []
    next_energy = []
    for i in range(4):
        for j in range(4):
            next_chromosome = np.concatenate((tourn[i][:12],tourn[j][12:]))
            nextgen_pop.append(next_chromosome)
            next_energy.append(energy[i][:12] + energy[j][12:])

    nextgen_pop = nextgen_pop[:10]
    next_energy = next_energy[:10]

    x = []
    y = []
    for i in range(len(nextgen_pop)):
        x_list = []
        y_list = []
        for j in range(num_nodes):
            x_list.append(nextgen_pop[i][j][0])
            y_list.append(nextgen_pop[i][j][1])
        x.append(x_list)
        y.append(y_list)

    next_sink_distance = []
    for i in range(len(x)):
        sd0 = []
        dx, dy = x[i][num_nodes - 1], y[i][num_nodes - 1]
        d = np.array(dx, dy)
        for j in range(num_nodes):
            p = np.array(x[i][j], y[i][j])
            sd0.append(np.linalg.norm(d - p))
        next_sink_distance.append(sd0)
    
    avgfit = np.sum(fit)/10
    pop = nextgen_pop
    energy = next_energy
    sink_distance = next_sink_distance
    
    print("Epoch " + str(epoch) + " : fitness " + str(avgfit))
    avg_fitness.append(avgfit)

plt.plot(avg_fitness)