from matplotlib import cm
import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('seaborn')

fig, ax = plt.subplots()
ax.scatter(2, 4, c='darkblue', s=100)

#set chart title and label axes
ax.set_title('Square numbers', fontsize=21)
ax.set_xlabel('Value', fontsize=10)
ax.set_ylabel('Square of value', fontsize=10)

#set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=10)



#lest try to plot mutliple points
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=(0, .8, 0, .5), s=100)

#set chart title and label axes
ax.set_title('Square numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of value', fontsize=14)

#set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

#plot for 1000 points
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values,cmap=plt.cm.YlGn, s=10)

#set chart title and label axes
ax.set_title('Square numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of value', fontsize=14)

#set size of tick labels
# ax.tick_params(axis='both', which='major', labelsize=14)

#set the range for each axis
ax.axis([0, 1_100, 0, 1_100_000])

plt.show()

