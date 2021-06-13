#a simple line graph, nothing fancy.
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

#adding another style, always to be added before generation
plt.style.use('dark_background')

fig, ax = plt.subplots()
ax.plot(input_values, squares, c='red', linewidth=3)

#set chart title and label axes
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Input Values", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

#set size of tick labels
ax.tick_params(axis='both', labelsize=14)

#plt.show()

plt.savefig('squares_plot.png', bbox_inches='tight')