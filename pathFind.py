from grid import GridClass
from collections import deque

#DIRECTIONS = [(-1,-1,),(-1,0,),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
DIRECTIONS = [(0,1),(1,0),(0,-1),(-1,0)]

class Stack:
    
    def __init__(self):
        self.stack = []
        
    def push(self,obj):
        
        self.stack.append(obj)
    
    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            print("Stack is empty!")
            
    def isEmpty(self):
        return len(self.stack) == 0

    def returnStack(self):
        return self.stack
    
    def show(self):
        
        for _ in (print(x) for x in self.stack):
            pass


class Queue:

    def __init__(self):

        self.queue = deque()

    def enqueue(self, obj):

        self.queue.append(obj)
    
    def dequeue(self):
        
        return self.queue.popleft()
        



class Path:
    

    def __init__(self,row,col,grid):
        self.visited = [[False for i in range(row)] for j in range(col)]
        self.nRows = row
        self.nCols = col
        self.maze = grid


    def visitPoint(self,point):
        
        self.visited[point[0]][point[1]] = True
        
        
    def unvisitPoint(self,point):
        
        self.visited[point[0]][point[1]] = False
        
    def isVisited(self,point):
        
        return self.visited[point[0]][point[1]] == True

    def inBounds(self,row,col):
        return ((row  >= 0) and ( row  < self.nRows)) and ((col  >= 0) and ( col  < self.nCols))

    def getNeighbour(self,source,d):
        target = (source[0] + DIRECTIONS[d][0] , source[1] + DIRECTIONS[d][1])

        
        
        
        if self.inBounds(target[0],target[1]):
            if self.maze.is_locked(target[0],target[1]) == False:
                
                return target
        
        return None

    def neighbourhood(self,source):

        res = []

        for i in range(len(DIRECTIONS)):
            n = self.getNeighbour(source,i)

            if n:
                res.append(n)

        return res

    def DFS(self,source,dest):
        
        S = Stack()
        S.push((source,[source]))
        solution = []
        
        while not S.isEmpty():
            
            #S.show()
            (source,solution) = S.pop()
            
            if source == dest:
                print("Found!")

                return solution
                
            
            if not self.isVisited(source):
                self.visitPoint(source)
            
                for i in range(len(DIRECTIONS)):
        
                    target = self.getNeighbour(source,i)
        
                    if target == None:
                        continue
                    else:
                        S.push((target,solution + [target]))
                        #path[target] = source


    def BFS(self,source, dest):
    # keep track of explored nodes
        explored = set()
        # keep track of all the paths to be checked
        queue = [(source,[source])]
        while queue:
            # pop the first path from the queue
            vertex,path = queue.pop(0)

            explored.add(vertex)
            for target in self.neighbourhood(vertex):
        
                if target == None:
                    continue

                if target == dest:
                    return path + [dest]
                
                else:
                    if target not in explored:
                        explored.add(target)
                        queue.append((target,path+[target]))

        #print("{} nodes explored.".format(len(explored)))



    def distBetween(self,start,goal):
        dx = abs(start[0] - goal[0])
        dy = abs(start[1] - goal[1])
        return dx+dy

    def heuristicEstimate(self,start,goal):

        return 1 * self.distBetween(start,goal)

    def neighborNodes(self,current):

        return self.neighbourhood(current)
    
    def reconstructPath(self,cameFrom,goal):
        path = deque()
        node = goal
        path.appendleft(node)
        while node in cameFrom:
            node = cameFrom[node]
            path.appendleft(node)
        return list(path)
    
    def getLowest(self,openSet,fScore):
        lowest = float("inf")
        lowestNode = None
        for node in openSet:
            if fScore[node] < lowest:
                lowest = fScore[node]
                lowestNode = node
        return lowestNode

    def aStar(self,start,goal):
        cameFrom = {}
        openSet = set([start])
        closedSet = set()
        gScore = {}
        fScore = {}
        gScore[start] = 0
        fScore[start] = gScore[start] + self.heuristicEstimate(start,goal)
        while len(openSet) != 0:
            current = self.getLowest(openSet,fScore)
            if current == goal:
                return self.reconstructPath(cameFrom,goal)
            openSet.remove(current)
            closedSet.add(current)
            for neighbor in self.neighborNodes(current):
                tentative_gScore = gScore[current] + self.distBetween(current,neighbor)
                if neighbor in closedSet and tentative_gScore >= gScore[neighbor]:
                    continue
                if neighbor not in closedSet or tentative_gScore < gScore[neighbor]:
                    cameFrom[neighbor] = current
                    gScore[neighbor] = tentative_gScore
                    fScore[neighbor] = gScore[neighbor] + self.heuristicEstimate(neighbor,goal)
                    if neighbor not in openSet:
                        openSet.add(neighbor)
        return 0
                



if __name__ == "__main__":
    

    row,col = 4,4
    maze = GridClass(row,col)

    maze.show_grid()

    source = (0,0)
    end = (row-1,col-1)

    solution = Path(row,col,maze).BFS(source,end)

    print("Solution path pathFind.py:")
    print(solution)