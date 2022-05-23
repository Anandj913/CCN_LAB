import numpy as np
import matplotlib.pyplot as plt

error_prob = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
link_utilization = [8.830022075055188E-4, 
		    7.952286282306163E-4, 
                    3.978779840848806E-4,
		    3.9761431411530816E-4,
                    3.615982643283312E-4,
	            3.731807438736161E-4,
                    6.633499170812604E-4,
                    6.1808941693565E-4,
	            6.642863073984888E-4,
                    4.2869697554283754E-4]
total_delay = [4529,4530,5534,8042,8541,9043,11046,11046,27595,51654]

plt.plot(error_prob,total_delay)
plt.title('Total Delay Vs Error Probability for fixed sized message length')
plt.xlabel('Error Probability')
plt.ylabel('Total Delay in sending packets (ms)')
plt.show()
