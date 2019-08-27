# AnimalDynamics-Task


## Installation
- Tested on Ubuntu 16.04
- Open a terminal and clone the repo using ```git clone https://github.com/eddymj96/AnimalDynamics-Task```

Due to the nature of the problem and the assumptions it seems logical to work with arrays/matrices thus ```numpy``` was used. Additionally, the graphing and visualisation tool ```matplotlib``` was employed to illustrate the map and paths of the robots. 
Both need to be installed to run the program, this can be done however the user wishes; a quick system-wide installation can be done by simply running ```bash install_script.sh``` in a terminal.

## Task 1:
Given the task of implementing a robot that is to sweep through a 2D map, exploring the entire area whilst avoiding obstacles. Starting at one corner of grid and ending another.

## Assumptions
- The map will be discretised into a 2D-Grid and 'exploration' of the map means visiting each viable, discrete point without going through randomly-generated, randomly-sized, rectangular obstacles.
<p align="center">
<img src="https://github.com/eddymj96/AnimalDynamics-Task/blob/master/Assets/obstacles2.png" width="80%" height="80%" />
</p>

- The robot is a simple point-mass robot that can only move vertically or horizontally along the map's points and can turn on the spot i.e. change directions whilst on the same point.  

- The robot has no previous 'blobal' map knowledge and senses obstacles with a one-node depth 'sensor' directed in front of it.
<p align="center">
<img src="https://github.com/eddymj96/AnimalDynamics-Task/blob/master/Assets/sensorillu.png" width="20%" height="20%" />
</p>

## Procedure

1.
The robot will explore with a simple breadth-first search (BFS)

## Notes and Improvements

The breadth-first search currently does not attempt to avoid a robot going over its previous nodes in order to visit others (the robot's respective previous path, it won't go over other robot's paths) in the queue. Whilst it ensure coverage, the sweep is inneficient; a hueristic form of the BFS could be derived in such a way that it lessens or even minimises visitation of previous nodes. 

Due to the assumptions made and the constraints that the robots must all terminate at the same point without visiting each others visited nodes a complicaiton arrives. Since the exit is situated in the corner, there are only 2 unique nodes that would allow a robot to traverse to the exit. Thus a compromise was made, when the map had been fully been explored the robots would disregard previously explored nodes from other robots to reach the exit.

A similar problem occasionally arises when the map is arranged in such a way that the exploration of some robots can "trap" a robot from visiting the rest of the map due as shown:
<p align="center">
<img src="https://github.com/eddymj96/AnimalDynamics-Task/blob/master/Assets/Trapped1.png" width="80%" height="80%" />
</p>
