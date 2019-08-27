import numpy as np
import matplotlib.pyplot as p
import copy as cp

class robot:
    rotation_matrix = np.array([[0, 1], [-1, 0]])
    def __init__(self, position):
        self.position = position
        self.orientation = np.array([1, 0])

    def scan(self):
        return self.position + self.orientation

    def turn(self):
        self.orientation = np.dot(self.orientation, self.rotation_matrix)
    

class queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class course:
    def __init__(self, length, width, obstacle_no):
        # Generate empty grid
        grid = np.zeros((length, width))
        self.exit_pos = np.array([length, width])
        # Generate number of obstacles
        for i in range(obstacle_no):
            # Generate dimensions of the obstacle, maximum being half the grid size
            max_dims = [np.random.randint(grid.shape[0]/2), np.random.randint(grid.shape[1]/2)]
            # Create boolean mask array
            binary_array = np.ones((max_dims[0], max_dims[1]))
            # Generate bottom left corner position of the obstacle
            starting_pos = [np.random.randint(grid.shape[0]- max_dims[0]), np.random.randint(grid.shape[1] - max_dims[1])]

            # While the obstacle does not fit on the grid
            while np.any(binary_array * grid[starting_pos[0]: starting_pos[0] + max_dims[0], starting_pos[1]: starting_pos[1] + max_dims[1]]):
                # Randomly change the dimensions and starting point until it does
                max_dims = [np.random.randint(grid.shape[0]/2), np.random.randint(grid.shape[1]/2)]
                binary_array = np.ones((max_dims[0], max_dims[1]))
                starting_pos = np.array([np.random.randint(grid.shape[0] - max_dims[0]), np.random.randint(grid.shape[1] - max_dims[1])])

            # Add the obstacle to the grid
            grid[starting_pos[0]: starting_pos[0] + max_dims[0], starting_pos[1]: starting_pos[1] + max_dims[1]] = binary_array 

        # Create border that allows the sensor to detect the map 'walls'
        self.final = np.ones((grid.shape[0] + 2, grid.shape[1] + 2))  
        # Place obstacle course inside
        self.final[1:1+grid.shape[0], 1:1+grid.shape[1]] = grid
        self.master_path_tracker = np.zeros((self.final.shape[0], self.final.shape[1]))
    def add_robot_paths(self, robot_no):
        self.robot_paths = np.zeros((self.final.shape[0], self.final.shape[1], robot_no))  

    def mark_path(self, coordinate, robot_no):
        self.master_path_tracker[tuple(coordinate)] = 1
        self.robot_paths[coordinate[0], coordinate[1], robot_no-1] = 1
    
    def node_is_unexplored(self, coordinate):
        print(self.master_path_tracker[tuple(coordinate)])
        return (self.final[tuple(coordinate)] + self.master_path_tracker[tuple(coordinate)] == 0)


class visualiser:
    def __init__(self, course):
        fig = p.figure()

        ax = fig.gca()
        ax.imshow(np.transpose(course.final), origin='lower', cmap = 'Greys')

        course.robot_paths[course.robot_paths == 0] = np.nan
        cmap_colours = ['Oranges','Purples', 'Blues', 'Greens', 'Reds']

        course.master_path_tracker[course.master_path_tracker == 0] = np.nan
        for i in range(course.robot_paths.shape[2]):
            cmap = cp.copy(p.get_cmap(cmap_colours[i % 5]))
            cmap.set_bad(alpha=0)
            ax.imshow(np.transpose(course.robot_paths[:,:,i]), origin='lower', cmap = cmap, vmin=0, vmax=1, alpha = 0.5)

        ax.set_xticks(np.arange(course.final.shape[0])- 0.5)
        ax.set_yticks(np.arange(course.final.shape[1])- 0.5)

        ax.set_xticklabels([])
        ax.set_yticklabels([])


        ax.grid(which='major')

        p.show()
    