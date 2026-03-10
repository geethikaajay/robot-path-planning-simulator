import numpy as np
import matplotlib.pyplot as plt
from heapq import heappush, heappop

# Grid definition
grid = np.array([
[0,0,0,1,0],
[0,1,0,1,0],
[0,1,0,0,0],
[0,0,0,1,0],
[1,1,0,0,0]
])

start = (0,0)
goal = (4,4)

rows, cols = grid.shape

# A* algorithm
def heuristic(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(start,goal):
    open_list=[]
    heappush(open_list,(0,start))

    came_from={}
    g_cost={start:0}

    while open_list:

        _,current=heappop(open_list)

        if current==goal:
            break

        x,y=current

        neighbors=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

        for nx,ny in neighbors:

            if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==0:

                new_cost=g_cost[current]+1

                if (nx,ny) not in g_cost or new_cost<g_cost[(nx,ny)]:

                    g_cost[(nx,ny)]=new_cost

                    priority=new_cost+heuristic((nx,ny),goal)

                    heappush(open_list,(priority,(nx,ny)))

                    came_from[(nx,ny)]=current

    path=[]
    node=goal

    while node!=start:
        path.append(node)
        node=came_from[node]

    path.append(start)
    path.reverse()

    return path

path=astar(start,goal)

# Visualization
grid_display=np.copy(grid)

for x,y in path:
    grid_display[x,y]=2

plt.imshow(grid_display)

plt.title("Robot Path Planning (A*)")

plt.show()