import numpy as np
import matplotlib.pyplot as plt

a = 3.05
x = [7.23-a,10.8-a,14.51-a,18.25-a,21.85-a]
y = [31.16,34.75,38.44,42.2,45.76]

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].scatter(x,y)
axs[0].set_xlabel("Total Volume Dispensed (mL)")
axs[0].set_ylabel("Mass (g)")
axs[0].set_title("Mass (g) vs. Total Volume Displaced (mL) of DI Water")

coefficients = np.polyfit(x, y, 1)
polynomial = np.poly1d(coefficients)
xs = np.linspace(min(x), max(x), 100)
ys = polynomial(xs)
axs[0].plot(xs, ys, '--r')

# Get the equation of the trend line
equation = "y = {:.3f}x + {:.3f}".format(coefficients[0], coefficients[1])

# Display the equation on the graph
axs[0].annotate(equation, (10,34), fontsize=12)

a1 = 11.35
x1 = [14.8-a1,17.99-a1,21.97-a1,25.74-a1,29.05-a1]
y1 = [30.08,32.67,35.91,39.00,41.72]

axs[1].scatter(x1,y1)
axs[1].set_xlabel("Total Volume Dispensed (mL)")
axs[1].set_ylabel("Mass (g)")
axs[1].set_title("Mass (g) vs. Total Volume Displaced (mL) of Unknown Liquid B")

coefficients1 = np.polyfit(x1, y1, 1)
polynomial = np.poly1d(coefficients)
xs1 = np.linspace(min(x1), max(x1), 100)
ys1 = polynomial(xs1)
axs[1].plot(xs1, ys1, '--r')

# Get the equation of the trend line
equation = "y = {:.3f}x + {:.3f}".format(coefficients1[0], coefficients1[1])

# Display the equation on the graph
axs[1].annotate(equation, (10,34), fontsize=12)

plt.show()
