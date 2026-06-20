import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
plt.subplot(221, title = "No.1", xticks = [1,2,3,4,5,6])
plt.plot((2, 4), (3, 6), c = 'g')

plt.subplot(223, xlabel = "Number", ylabel="Value")
plt.plot((1, 2), (4, 3), c = 'b')

plt.subplot(224, facecolor = '#00FFFF')
plt.plot((1, 2), (3, 4), c = 'y')

plt.subplots_adjust(wspace=0.4, hspace=0.6)
plt.show()