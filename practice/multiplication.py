import plotly.express as px

from die import Die


# Create two D8s.
die_2 = Die()
die_1 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1_000_000):
    results.append(die_1.roll() * die_2.roll())

# Analyze the results.
frequencies = []
max_results = die_1.num_sides * die_2.num_sides

poss_results = range(2, max_results + 1)
for value in poss_results:
    frequencies.append(results.count(value))

# Visualize the results.
title = "Results of Multiplying two D8s 1,000,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

fig.show()
