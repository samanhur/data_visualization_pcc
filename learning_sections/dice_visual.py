import plotly.express as px

from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()


results = []

# Make some rolls, and store results in a list.
for roll_num in range(1000):
    results.append(die_1.roll() + die_2.roll())

# Analyze the results.
frequencies = []
poss_results = range(2, (die_1.num_sides + die_2.num_sides)+ 1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the result.
title = "Results of Rolling Two D6 Dice 1,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}

fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

fig.show()
