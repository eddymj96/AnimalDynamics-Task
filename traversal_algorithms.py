import task_classes as tc
import numpy as np
        
def explorer(course, robots):
    queues = []

    # Generate list of queues for each robot and mark their initial positions
    for i in range(len(robots)):
        queues.append(tc.queue())
        queues[i].enqueue(robots[i].position)
        course.mark_path(robots[i].position, i)
    
    # While at least one queue is not empty
    while not all([ q.is_empty() for q in queues]):
        for j in range(len(queues)): 
            if queues[j].is_empty(): # if queue is empty - skip
                continue
            else:
                robots[j].position = queues[j].dequeue()

                for k in range(4): # for 4 rotations to return to original orientation
                    coordinate = robots[j].scan()
                    if course.node_is_unexplored(coordinate): 
                        course.mark_path(coordinate, j)
                        queues[j].enqueue(coordinate) 

                    robots[j].turn()

    print("Solved")
    return course
