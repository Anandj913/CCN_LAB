import numpy as np
import matplotlib.pyplot as plt

error_prob = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

total_delay = [7011.245361328125 ,8017.91064453125,13021.8115234375,11016.5458984375,9013.46875,11014.902587890625, 16019.70849609375,42058.68603515625,67832.8740234375,112152.20385742188]
send_delay = [0.963867187,0.862060546875,1.764892578125, 1.9541015625,1.3212890625,1.244140625, 1.36181640625, 4.755126953125, 6.495849609375, 12.02294921875]

plt.plot(error_prob,send_delay)
plt.title('Total Delay Vs Error Probability for fixed sized message length')
plt.xlabel('Error Probability')
plt.ylabel('Total Delay in sending packets (ms)')
plt.show()
