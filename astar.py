from heapq import *

def astar(puzzle,goalState,heuristic):
  explored = []
  gScore = {}
  pQueue = []
  actions ={}
  gScore[str(puzzle)] = 0
  actions[str(puzzle)] = []
  heappush(pQueue,(0,puzzle))
  while(pQueue):
    current=heappop(pQueue)[1]
    # print(current)
    if(current == goalState): return actions[str(current)]
    explored.append(current)
    for successor in getSuccessors(current):
    	if((successor not in explored) and successor not in pQueue):
	        gScore[str(successor)] = gScore[str(current)] + 1
	        heappush(pQueue,(gScore[str(successor)] + heuristic(successor),successor))
	        tempList = list(actions[str(current)])
	        tempList.append(successor)
	        actions[str(successor)] = tempList
      	elif(successor in pQueue):
			if(str(successor) in gScore):
				if(gScore[str(successor)]> gScore[str(current)] + 1):
					pQueue.remove((gScore[str(successor)] + heuristic(successor),successor))
					gScore[str(successor)] = gScore[str(current)] + 1
					heappush(pQueue(gScore[str(successor)] + heuristic(successor),successor))
					temp = list(actions[str(current)])
					temp.append(successor)
					actions[str(successor)] = temp

def heuristic_evaluation(puzzle): 
	return 0

def getSuccessors(puzzle):
	successors = []
	tempPuzzle = [row[:] for row in puzzle]
	for i in range(len(puzzle)):
		for j in range(len(puzzle[0])):
			if(puzzle[i][j] == 0):
				x = i
				y = j
	if(x>0):
		tempPuzzle[x-1][y] = puzzle[x][y]
		tempPuzzle[x][y] = puzzle[x-1][y]
		successors.append(tempPuzzle)
		tempPuzzle = [row[:] for row in puzzle]
	if(x<2):
		tempPuzzle[x+1][y] = puzzle[x][y]
		tempPuzzle[x][y] = puzzle[x+1][y]
		successors.append(tempPuzzle)
		tempPuzzle = [row[:] for row in puzzle]
	if(y>0):
		tempPuzzle[x][y-1] = puzzle[x][y]
		tempPuzzle[x][y] = puzzle[x][y-1]
		successors.append(tempPuzzle)
		tempPuzzle = [row[:] for row in puzzle]
	if(y<2):
		tempPuzzle[x][y+1] = puzzle[x][y]
		tempPuzzle[x][y] = puzzle[x][y+1]
		successors.append(tempPuzzle)
		tempPuzzle = [row[:] for row in puzzle]
	return successors

