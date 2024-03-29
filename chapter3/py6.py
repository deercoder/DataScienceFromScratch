#!/usr/bin/env python
# scatter plot, like drawing (x,y) from two datasets with Xs, Ys,
# it is used for drawing relationship

from matplotlib import pyplot as plt

friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

# S
plt.scatter(friends, minutes)

# now we want to draw the label
for label, friend_count, minute_count in zip(labels, friends, minutes):
	plt.annotate(label,
		xy = (friend_count, minute_count),	# put label with points
		xytext=(5, -5),		# but slightly offset
		textcoords='offset points')

plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")

# show
plt.show()
