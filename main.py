import matplotlib.pyplot as p
import numpy as np
import task_classes as tc
import traversal_algorithms as ta

## ---- Setup Grid and Obstacles ---- 

length = 60 # choose desired length
width = 40 # choose desired width
max_obstacle_no = 7
obstacle_no = np.random.randint(max_obstacle_no) 

# Create course
course = tc.course(length, width, obstacle_no)

## ---- Solving with Robot ----

no_of_robots = 4
robots = []
   
for i in range(no_of_robots):
    robots.append(tc.robot(np.array([1, 2*i+1])))


course.add_robot_paths(no_of_robots)

completed_course = ta.explorer(course, robots)

# visualisation 

visualisation = tc.visualiser(course)