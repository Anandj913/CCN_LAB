'''
Name: Anand Jhunjhunwala
Roll no: 17EC35032
'''

import random
import math
import statistics
import matplotlib.pyplot as plt
import numpy as np

#Set the value of lamda and total number of events
_lambda = 20
num_events = 1000
event_num = []
inter_event_times = []
event_times = []
event_time = 0


for i in range(num_events):
	event_num.append(i)
	#Get a random probability value from the uniform distribution's PDF
	n = random.random()

	#Generate the inter-event time from the exponential distribution's CDF using the Inverse-CDF technique
	inter_event_time = -math.log(1-n) / _lambda
	inter_event_times.append(inter_event_time)

	#Add the inter-event time to the running sum to get the next absolute event time
	event_time = event_time + inter_event_time
	event_times.append(event_time)

#plot the inter-event times
fig = plt.figure()
fig.suptitle('Times between consecutive events in a simulated Poisson process for lambda ' + str(_lambda))
plot, = plt.plot(event_num, inter_event_times, 'bo-', label='Inter-event time')
plt.legend(handles=[plot])
plt.xlabel('Index of event')
plt.ylabel('Time')
plt.show()


#plot the absolute event times
fig = plt.figure()
fig.suptitle('Absolute times of consecutive events in a simulated Poisson process for lambda ' + str(_lambda))
plot, = plt.plot(event_num, event_times, 'bo-', label='Absolute time of event')
plt.legend(handles=[plot])
plt.xlabel('Index of event')
plt.ylabel('Time')
plt.show()

interval_nums = []
num_events_in_interval = []
interval_num = 1
num_events = 0

#Calculate the number of events in unit time frame
for i in range(len(event_times)):
	event_time = event_times[i]
	if event_time < interval_num:
		num_events += 1
	else:
		interval_nums.append(interval_num)
		num_events_in_interval.append(num_events)

		interval_num += 1

		num_events = 1


hist = np.zeros(int(np.max(num_events_in_interval))+1) # histogram
for i in num_events_in_interval:
	hist[int(i)] = hist[int(i)] + 1

hist /= np.sum(hist)

#Plot PDF
fig = plt.figure()
fig.suptitle('Probability of occurance for lambda: ' + str(_lambda))
plt.plot(hist)
plt.xlabel('K')
plt.ylabel('Probability of occurance')
plt.show()

#Print calculated lamda value
print("Calculated Lambda: {}".format(statistics.mean(num_events_in_interval)))