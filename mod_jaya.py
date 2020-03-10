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

avg_fit_mod = []
for epoch in range(30):
    fit = []
    for i in range(10):
        f = 1/(0.6*fp1[i] + 0.4*fp2[i])
        fit.append(f)

    for i in range(len(fit)):
        for j in range(i+1, len(fit)):
            if fit[i] > fit[j]:
                fit[i], fit[j] = fit[j], fit[i]
                fp1[i], fp1[j] = fp1[j], fp1[i]
                fp2[i], fp2[j] = fp2[j], fp2[i]

    best_fit, best_fp1, best_fp2 = fit[0], fp1[0], fp2[0]
    worst_fit, worst_fp1, worst_fp2 = fit[9], fp1[9], fp2[9]

    new_fp1 = fp1 + (best_fp1 - fp1) - (worst_fp1 - fp1)
    new_fp2 = fp2 + (best_fp2 - fp2) - (worst_fp2 - fp2)

    fp1 = new_fp1
    fp2 = new_fp2
    
    avg_fit = np.sum(fit)/10
    avg_fit_mod.append(avg_fit)
    
    print("Epoch: " + str(epoch) + " fitness: " + str(avg_fit))

plt.plot(avg_fitness)
plt.plot(avg_fit_mod)
plt.legend(['Genetic Algorithm', 'Proposed Algorithm'])
plt.xlabel('Generation')
plt.ylabel('Average population fitness')