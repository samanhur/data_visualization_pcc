import matplotlib.pyplot as plt

from random_walk import RandomWalk


# Make a random walk
rw = RandomWalk(5000)
rw.fill_walk()

# Plot the points in the walk.
plt.style.use("classic")
fig, ax = plt.subplots()
point_numbers = range(rw.num_points)
ax.plot(rw.x_coordinate, rw.y_coordinate, linewidth=1)
ax.set_aspect("equal")

# Emphasize the first and last points.
ax.scatter(0, 0, c="green", edgecolors="none", s=100)
ax.scatter(rw.x_coordinate[-1], rw.y_coordinate[-1], c="red", edgecolors="none", s=100)

# Remove the axes.
# ax.get_xaxis().set_visible(False)
# ax.get_yaxis().set_visible(False)

plt.show()
