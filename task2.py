import matplotlib.pyplot as p
import numpy as np
import copy as cp
import task_classes as tc
import sys
np.set_printoptions(threshold=sys.maxsize)

# setup grid
grid = np.zeros((60,40))

# setup obstacles 
max_obstacle_no = 5
obstacle_no = np.random.randint(max_obstacle_no) + 2
print(obstacle_no)

for i in range(obstacle_no):

    # block out a maximum area of the grid for the obstacle
    max_dims = [np.random.randint(grid.shape[0]/2), np.random.randint(grid.shape[1]/2)]
    binary_array = np.ones((max_dims[0], max_dims[1]))
    #print(binary_array.shape)
    #print(grid.shape)
    #print(max_dims[1])
    starting_pos = [np.random.randint(grid.shape[0]- max_dims[0]), np.random.randint(grid.shape[1] - max_dims[1])]

    while np.any(binary_array * grid[starting_pos[0]: starting_pos[0] + max_dims[0], starting_pos[1]: starting_pos[1] + max_dims[1]]):
        max_dims = [np.random.randint(grid.shape[0]/2), np.random.randint(grid.shape[1]/2)]
        binary_array = np.ones((max_dims[0], max_dims[1]))
        starting_pos = np.array([np.random.randint(grid.shape[0] - max_dims[0]), np.random.randint(grid.shape[1] - max_dims[1])])
    
    grid[starting_pos[0]: starting_pos[0] + max_dims[0], starting_pos[1]: starting_pos[1] + max_dims[1]] = binary_array 

final = np.ones((grid.shape[0] + 2, grid.shape[1] + 2))  
final[1:1+grid.shape[0], 1:1+grid.shape[1]] = grid

# solving with robot

robot_no = 4 #np.random.randint(max_obstacle_no)

master_path = np.zeros((grid.shape[0] + 2, grid.shape[1] + 2)) 
robot_paths = np.zeros((grid.shape[0] + 2, grid.shape[1] + 2, robot_no))  

move_matrix = np.array([[0, 1 ,0], [1, 0 ,1], [0, 1, 0]])
orientation_matrix = np.array([1, 0])

rotation_matrix = np.array([[0, 1], [-1, 0]])

robots = []

queues = []

for i in range(robot_no):
    robots.append(tc.robot(np.array([1, 2*i+1])))
    robot_paths[1, 2*i+1, i] = 1
    queues.append(tc.queue())
    queues[i].enqueue(np.array([1, 2*i+1]))

while not all([ q.is_empty() for q in queues]):

    for j in range(robot_no): 
        if queues[j].is_empty():
            continue
        else:
            robots[j].position = queues[j].dequeue()

            for x in range(4):
                coordinate = robots[j].position + orientation_matrix
                if (final[tuple(coordinate)] + master_path[tuple(coordinate)]) == 0: 
                    master_path[tuple(coordinate)] = 1
                    robot_paths[coordinate[0], coordinate[1], j] = 1
                    queues[j].enqueue(coordinate) 

                orientation_matrix = np.dot(orientation_matrix,rotation_matrix)
       
            print("queue ",j, " size: ", queues[j].size())
            print([ q.is_empty() for q in queues])

print("Solved")
print("Final Robot Positions :", [r.position for r in robots])


# visualisation 

fig = p.figure()


ax = fig.gca()
ax.imshow(np.transpose(final), origin='lower', cmap = 'Greys')

print(robot_paths[:,:,0])

robot_paths[robot_paths == 0] = np.nan
cmap_colours = ['Oranges','Purples', 'Blues', 'Greens', 'Oranges', 'Reds']
cmaps = []

master_path[master_path == 0] = np.nan
for i in range(robot_no):
    cmap = cp.copy(p.get_cmap(cmap_colours[i]))
    print(cmap_colours[i])
    cmap.set_bad(alpha=0)
    ax.imshow(np.transpose(robot_paths[:,:,i]), origin='lower', cmap = cmap, vmin=0, vmax=1, alpha = 0.5)

ax.set_xticks(np.arange(final.shape[0])- 0.5)
ax.set_yticks(np.arange(final.shape[1])- 0.5)

#ax.set_xticklabels(np.arange(0, grid.shape[0], 1))
#ax.set_yticklabels(np.arange(0, grid.shape[1], 1))

ax.set_xticklabels([])
ax.set_yticklabels([])


ax.grid(which='major')

p.show()