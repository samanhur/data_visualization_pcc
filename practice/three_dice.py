from die import Die
import plotly.express as px


# Create three D6s.
die_1 = Die()
die_2 = Die()
die_3 = Die()


# Make some rolls, and store results in a list.
results = []
for roll_num in range(1_000_000):
    results.append(die_1.roll() + die_2.roll()+die_3.roll())

# Analyze the results.
frequencies = []
max_results = die_1.num_sides + die_2.num_sides + die_3.num_sides

poss_results = range(3, max_results + 1)
for value in poss_results:
    frequencies.append(results.count(value))
    
# Visualize the results.
title = "esults of Rolling three D6s 1,000,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

# fig.show()
fig.write_html("three_dice.html")