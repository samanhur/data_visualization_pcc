import matplotlib.pyplot as plt

# Define data.
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

# Make plot.
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

# Set chart title and label axes.
ax.set_title("Cubes", fontsize=20)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis="both", labelsize=14)

# Set the range for each axes.
ax.axis([0, 5100, 0, 128_000_000_000])
ax.ticklabel_format(style="plain")

# Show plot.
plt.show()
