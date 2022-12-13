#Description:
#   counts n of bombs adjacent to each free cell
#   input: 5x5 grid with bombs(#) and free cells(-)
#   output 5x5 grid with counted
#   !!!!!Currently doesnt work!!!!!

class Grid:
    def __init__(self,data):
        self.data = data

    def get_cell(self,x,y):
        return self.data[y][x]

    def countdir(self,x,y,xOffs,yOffs):
        if xOffs ==-1 and yOffs ==-1 and (x==0 or y==0):  #top left
            return 0
        if xOffs == 1 and yOffs ==-1 and (x==4 or y==0):  #top right
            return 0
        if xOffs ==-1 and yOffs == 1 and (x==0 or y==4):  #bot left
            return 0
        if xOffs == 1 and yOffs == 1 and (x==4 or y==4):  #bot right
            return 0
        if yOffs ==-1 and y==0:  #top
            return 0
        if yOffs == 1 and y==4:  #bot
            return 0
        if xOffs ==-1 and x==0:  #left
            return 0
        if xOffs == 1 and x==4:  #right
            return 0


        if self.get_cell(x+xOffs, y+yOffs) == "#":
            return 1
        elif self.get_cell(x+xOffs, y+yOffs) == "-":
            return 0

    def countadjbombs(self,x,y):
        cnt = 0

        for xOffs in range(-1,2):
            for yOffs in range(-1,2):
                if self.countdir(x,y,xOffs, yOffs):
                    cnt += 1
        
        return str(cnt)


def num_grid(lst):
    grid = Grid(lst)
    cntedgrid = [["-" for i in range(5)] for i in range(5)]

    for y in range(5):
        for x in range(5):

            if grid.get_cell(x,y) == "-":
                if int(grid.countadjbombs(x,y)) > 0:
                    cntedgrid[x][y] = grid.countadjbombs(x,y)

            elif grid.get_cell(x,y) == "#":
                cntedgrid[x][y] = "#"
    
    return cntedgrid

testgrid1 = [
    ["#","-","#","-","-"],
    ["#","-","-","-","-"],
    ["#","-","#","#","#"],
    ["#","#","#","-","#"],
    ["#","-","#","#","#"]
]

for row in num_grid(testgrid1):
    print (row)