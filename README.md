# pathFind

Visual pathfind in a maze, using python pygame library, DFS,BFS and A* algorithms
![Image of the GUI](https://github.com/Pungolini/pathFind/blob/master/screenshot.png)


usage: python mazeGui.py [size] [algorithm]

Both [size] and [algorithm] are optional, default values are defined in mazeGui.py

To run the program you need pygame installed. You can install it using pip command


**grid.py** contains a class that defines elementary methods to work with the matrix used as grid

**pathFind.py** contains 3 classes: Stack , Queue and Path. The latter implements **Breadth First Search (BFS)**, **Depth First Search (BFS)** and __A*__ algorithms.

**mazeGui.py** implements the GUI, using pygame
