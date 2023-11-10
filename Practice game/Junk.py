import numpy as np
import matplotlib.pyplot as plt

#define data
x = np.array([2, 4, 8, 16, 32])
y = np.array([0.009, 0.020, 0.061, 0.111, 0.189])

#find line of best fit
a, b = np.polyfit(x, y, 1)

#add points to plot
plt.scatter(x, y)

#add line of best fit to plot
plt.plot(x, a*x+b)  

print(0.0060047*0.085+0.00354167)
print((0.085-0.00354167)/0.0060047)