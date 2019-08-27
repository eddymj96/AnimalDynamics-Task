import matplotlib.pyplot as p
import numpy as np
import copy as cp
import task_classes as tc

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

    starting_pos = [np.random.randint(grid.shape[0]- max_dims[0]), np.random.randint(grid.shape[1] - max_dims[1])]

    while np.any(binary_array * grid[starting_pos[0]: starting_pos[0] + max_dims[0], starting_pos[1]: starting_pos[1] + max_dims[1]]):
        max_dims = [np.random.randint(grid.shape[0]/2), np.random.randint(grid.shape[1]/2)]
        binary_array = np.ones((max_dims[0], max_dims[1]))
        starting_pos = np.array([np.random.randint(grid.shape[0] - max_dims[0]), np.random.randint(grid.shape[1] - max_dims[1])])
    
    grid[starting_pos[0]: starting_pos[0] + max_dims[0], starting_pos[1]: starting_pos[1] + max_dims[1]] = binary_array 

final = np.ones((grid.shape[0] + 2, grid.shape[1] + 2))  
final[1:1+grid.shape[0], 1:1+grid.shape[1]] = grid
# solving with robot

robot_path = np.zeros((grid.shape[0] + 2, grid.shape[1] + 2))   

move_matrix = np.array([[0, 1 ,0], [1, 0 ,1], [0, 1, 0]])
orientation_matrix = np.array([1, 0])

rotation_matrix = np.array([[0, 1], [-1, 0]])

init_pos = np.array([1,1])

robot = tc.robot(init_pos)

final_pos = [60, 40]

queue = tc.queue()

robot_path[tuple(init_pos)] = 1

queue.enqueue(init_pos)
while not queue.is_empty():
    robot.position = queue.dequeue()

    for x in range(4):
        coordinate = robot.position + orientation_matrix
        print(final[tuple(coordinate)] + robot_path[tuple(coordinate)])
        if (final[tuple(coordinate)] + robot_path[tuple(coordinate)]) == 0: 
            robot_path[tuple(coordinate)] = 1
            
            queue.enqueue(coordinate) 

        orientation_matrix = np.dot(orientation_matrix,rotation_matrix)
       
    print("queue size", queue.size())

print("Solved")
print("Final Robot Position :", robot.position)

# visualisation 


fig = p.figure()


ax = fig.gca()
ax.imshow(np.transpose(final), origin='lower', cmap = 'Greys')
my_cmap = cp.copy(p.get_cmap('Oranges'))
my_cmap.set_bad(alpha=0)
robot_path[robot_path == 0] = np.nan
ax.imshow(np.transpose(robot_path), origin='lower', cmap = my_cmap, vmin=0, vmax=1, alpha = 0.5)
ax.set_xticks(np.arange(final.shape[0])- 0.5)
ax.set_yticks(np.arange(final.shape[1])- 0.5)
ax.set_xticklabels([])
ax.set_yticklabels([])


ax.grid(which='major')

p.show()