import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import binom
import random



def slotted_aloha(arrival_times: np.ndarray):
    count_arrivals = np.zeros(math.ceil(arrival_times[-1]) + 1)
    for val in arrival_times:
        count_arrivals[math.ceil(val)] += 1
    return np.sum(1 * (count_arrivals == 1))


def pure_aloha(inter_arrival_time: np.ndarray):
    success = 0
    for j, time in enumerate(inter_arrival_time):
        if j - 1 >= 0 and inter_arrival_time[j - 1] >= 1 and j + 1 < N and inter_arrival_time[j + 1] >= 1:
            success += 1
    return success



N = int(1e4)
numG = 20
rng = np.random.default_rng()
throughput_pure = np.zeros(numG)
throughput_slotted = np.zeros(numG)
G = np.logspace(-1.5, .8, numG)

print("Calculating throughput for different attempts rate")

for i, lam in enumerate(G):
    print("For attempt rate: {0}, Calculating arrival time".format(lam))
    inter_arrival_time = rng.exponential(1 / lam, N)
    arrival_times = np.array(inter_arrival_time)
    for j in range(1, len(arrival_times)):
        arrival_times[j] += arrival_times[j - 1]
    print("Calculating Throughput")
    throughput_pure[i] = pure_aloha(inter_arrival_time) / math.ceil(arrival_times[-1])
    throughput_slotted[i] = slotted_aloha(arrival_times) / math.ceil(arrival_times[-1])

print("Plotting the final throughput Vs attempts rate")
fig, ax = plt.subplots()
ax.plot(G, throughput_pure, marker='.', label='Pure Aloha')
ax.plot(G, throughput_slotted, marker='.', label='Slotted Aloha')
ax.set_xlabel('G (attempts rate)')
ax.set_ylabel('S (throughput per frame time)')
ax.legend()
fig.show()
fig.savefig("plot_throughput_vs_attempts_rate.jpeg", dpi=600)
