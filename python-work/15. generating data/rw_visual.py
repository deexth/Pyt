import matplotlib.pyplot as plt
from matplotlib import cm
from random_walk import RandomWalk


# file = 'Runs.txt'
#keep making a random_walk
count = 0
while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()

    #plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    point_numbers = range(rw.num_points)
    
    #scatter
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.bone, edgecolors='none', s=3)
    
    #plot
    #ax.plot(rw.x_values, rw.y_values, linewidth=1)
    
    #emphasize the first and last points
    ax.scatter(0, 0, c='red', edgecolors='none', s=100, zorder=2)
    ax.scatter(rw.x_values[-1], rw.y_values[-1],
               edgecolors='none', s=100, zorder=2)
    
    #remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    #labiling
    ax.set_title("Random Walk", fontsize=24)
    ax.set_xlabel("X values", fontsize=14)
    ax.set_ylabel("Y values", fontsize=14)

    plt.show()
    
    #count the number of walks
    # count = count + 1
    # with open(file, 'a') as runs:
    #     runs.write("Run " + str(count) + "\n" + str(rw.x_values) + "\n")
    
    #break the loop
    keep_running = input("Make another walk (y/n)? ")
    if keep_running == 'n' or keep_running == 'N':
        break;
    
    
    


