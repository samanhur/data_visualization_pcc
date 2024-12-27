import plotly.express as px

from die import Die


# Create two D8s.
die_1 = Die(8)
die_2 = Die(8)

# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for num_roll in range(1_000_000)]

# Analyze the results.
max_results = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_results + 1)

frequencies = [results.count(value) for value in poss_results]

# Visualize the results.
title = "Results of Rolling two D8s 1,000,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

fig.show()
