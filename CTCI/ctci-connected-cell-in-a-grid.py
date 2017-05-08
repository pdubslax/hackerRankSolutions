count = 0

def safeToExplore(row,col,grid,visited):
	rows = len(grid)
	cols = len(grid[0])
	return row < rows and row >= 0 and col < cols and col >= 0 and grid[row][col] and not visited[row][col]


def depthSearch(row,col,grid,visited):
	global count
	visited[row][col] = True

	rowMod = [-1,-1,-1,0,0,1,1,1]
	colMod = [-1,0,1,-1,1,-1,0,1]

	for x in range(8):
		if safeToExplore(row + rowMod[x],col + colMod[x],grid,visited):
			count += 1
			depthSearch(row + rowMod[x],col + colMod[x],grid,visited)



def get_biggest_region(grid):
	global count
	maxRegion = 0
	visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
	for row in range(len(grid)):
		for col in range(len(grid[row])):
			if grid[row][col] and not visited[row][col]:
				#start a new calculation 
				count = 1
				depthSearch(row,col,grid,visited)
				if count > maxRegion:
					maxRegion = count

	return maxRegion
    

n = int(raw_input().strip())
m = int(raw_input().strip())
grid = []
for grid_i in xrange(n):
    grid_temp = map(int, raw_input().strip().split(' '))
    grid.append(grid_temp)

# grid = [[1,1,0,0],[0,1,1,0],[0,0,1,0],[1,0,0,0]]
print get_biggest_region(grid)
