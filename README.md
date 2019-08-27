# AnimalDynamics-Task
## Task:
Given the task of implementing a robot that is to sweep through a 2D map, starting at one corner of grid and ending another whilst exploring the entire area and avoiding obstacles. This is to be extended to any number of desired robots that should cooperatively to explore the map without visiting nodes that have already been visited by any robots, nor shoudl they collide with obstacles or themselves. 

## Overview 

Robots will explore with a collaborative breadth-first search (BFS) where nodes are discovered and susbequently queued (granted they are viable) until exhaustively searched by the robots and the queue is empty. This guarantees full coverage and non-collisions at the expense of efficiency. 

## Assumptions

- The map will be discretised into a 2D-Grid and 'exploration' of the map means visiting each viable, discrete point without going through randomly-generated, randomly-sized, rectangular obstacles.
<p align="center">
<img src="https://github.com/eddymj96/AnimalDynamics-Task/blob/master/Assets/obstacles2.png" width="80%" height="80%" />
</p>

- The robot is a simple point-mass robot that can only move vertically or horizontally along the map's points and can turn on the spot i.e. change directions whilst on the same point. 

- The robot has no previous 'global' map knowledge and senses obstacles with a one-node depth 'sensor' directed in front of it.
<p align="center">
<img src="https://github.com/eddymj96/AnimalDynamics-Task/blob/master/Assets/sensorillu.png" width="20%" height="20%" />
</p>

- Robots can "instantly" communicate to a central database to transmit what nodes they have discovered and to retrieve information regarding what nodes have already been discovered

## Installation and Usage
- Using Python3
- Tested on Ubuntu 16.04
- Open a terminal and clone the repo using ```git clone https://github.com/eddymj96/AnimalDynamics-Task```
- Change directories using ```cd AnimalDynamics-Task```
- run ```Python3 main.py ``` followed by the number of robots you want to use

### Example 
 ```Python3 main.py 3 ```
 <p align="center">
<img src="https://github.com/eddymj96/AnimalDynamics-Task/blob/master/Assets/example1.png" width="80%" height="80%" />
</p>
 
Due to the nature of the problem and the assumptions it seems logical to work with arrays/matrices thus ```numpy``` was used. Additionally, the graphing and visualisation tool ```matplotlib``` was employed to illustrate the map and paths of the robots. 
Both need to be installed to run the program, this can be done however the user wishes; a quick system-wide installation can be done by simply running ```bash install_script.sh``` in a terminal.

## Notes and Improvements

The breadth-first search currently does not attempt to avoid a robot going over its previous nodes in order to visit others (the robot's respective previous path, it won't go over other robot's paths) in the queue. Whilst it ensure coverage, the sweep is inneficient; a hueristic form of the BFS could be derived in such a way that it lessens or even minimises visitation of previous nodes. 

The path planning between nodes that are already discovered was not implemented since this would require another step of path planning (such as an A* implementation) for travelling to different, already discovered nodes. And thus it is assumed that a robot can simply positions themself there in the code. This is also true for reaching the endpoint; with a singular robot, it will reach the exit point, however multiple robots wont directly terminate at the end point (since their paths would overlap), thus something like A* could also be implememented there.

Due to the assumptions made and the constraints that the robots must all terminate at the same point without visiting each others visited nodes a complication arrives. Since the exit is situated in the corner, there are only 2 unique nodes that would allow a robot to traverse to the exit. Thus a compromise was made, when the map had been fully been explored the robots would disregard previously explored nodes from other robots to reach the exit.

<p align="center">
<img src="https://github.com/eddymj96/AnimalDynamics-Task/blob/master/Assets/corner.png" width="20%" height="20%" />
</p>

A similar problem occasionally arises when the map is arranged in such a way that the exploration of some robots can "trap" a robot from visiting the rest of the map due as shown:
<p align="center">
<img src="https://github.com/eddymj96/AnimalDynamics-Task/blob/master/Assets/Trapped1.png" width="80%" height="80%" />
</p>
