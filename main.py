import os
import time
import copy
from collections import deque
def clear_screen():
    os.system("cls")
maze =[
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,0,1,0,0,0,1],
    [1,0,1,0,1,0,1,1,1,0,1,0,1,0,1],
    [1,0,1,0,0,0,0,0,1,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,1,0,0,0,1],
    [1,1,1,1,1,0,1,1,1,0,1,1,1,0,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,1,0,1],
    [1,0,1,0,1,1,1,0,1,1,1,0,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]
start =(1,1)
end =(9,13)
dfsmaze=copy.deepcopy(maze)
bfsmaze=copy.deepcopy(maze)
def print_maze(maze,start,end):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (i,j)==start:
                print("S",end="")
            elif(i,j) == end:
                print("E",end="")
            elif maze[i][j]==0:
                print(" ",end="")
            elif maze[i][j] ==1:
                print("#",end="")
            elif maze[i][j] ==2:
               print(".",end="")
            elif maze[i][j] ==3:
               print("*",end="")
        print()
#print_maze(maze)
def neighbors(position,maze):
    x,y=position
    directions=[(0,1),(0,-1),(1,0),(-1,0)]
    neighbors =[]
    for dx,dy in directions:
        nx=x+dx
        ny=y+dy
        if maze[nx][ny]==0:
            neighbors.append((nx,ny))
    return neighbors
def  dfs(dfsmaze,start,end):
   stack =[(start,[start])]
   visited =set()
   step=0
   while stack:
       position,path =stack.pop()
       if position in visited:
           continue
       visited.add(position)
       step+=1
       if position ==end:
           return True,path,step
       if position !=end and position !=start:
           x,y=position
           dfsmaze[x][y]=2
       clear_screen()
       print_maze(dfsmaze,start,end)
       time.sleep(0.5)
       zhouwei =neighbors(position,dfsmaze)
       for next_position in zhouwei:
             if next_position not in visited:
                 stack.append((next_position,(path+[next_position])))
   return False,[]
result,path,step=dfs(dfsmaze,start,end)
for k,q in path:
    dfsmaze[k][q]=3
print("DFS搜索结果",step)
print(result)
print(path)
print_maze(dfsmaze,start,end)
input("请按回车健继续查看BFS算法结果...")
clear_screen()
def bfs(bfsmaze,start,end):
    queue =deque([(start,[start])])
    visit=set()
    steps=0
    while queue:
        position,path=queue.popleft()
        if position in visit:
            continue
        visit.add(position)
        steps+=1
        if position == end:
            return True,path,steps
        if position !=end and position !=start:
            x,y=position
            bfsmaze[x][y]=2
        clear_screen()
        print_maze(bfsmaze,start,end)
        time.sleep(0.5)
        zhouwei=neighbors(position,bfsmaze)
        for next_position in zhouwei:
            if next_position not in visit:
                queue.append((next_position,path+[next_position]))
    return False,[]
results,paths,steps=bfs(bfsmaze,start,end)
for k,q in paths:
    bfsmaze[k][q]=3
print("BFS搜索步骤",steps)
print(results)
print(paths)
print_maze(bfsmaze,start,end)
#print_maze(path,start,end)
