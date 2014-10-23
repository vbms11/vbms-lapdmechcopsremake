
def loadLevelFile (filename):
    
    # read the file
    f = open(filename)
    lines = f.read().splitlines()
    f.close()
    
    sizeY = len(lines)
    sizeX = len(lines[0])
    
    level = [[0 for x in xrange(sizeX)] for y in xrange(sizeY)]
    
    for y in xrange(0, sizeY):
        for x in xrange(0, sizeX):
            type = lines[y][x]
            if type == "#":
                level[y][x] = BuildingTile(SceneTile)
            elif type == "X":
                level[y][x] = BaseTile(SceneTile)
            elif type == "+":
                level[y][x] = RoadTile(SceneTile)
            elif type == "-":
                level[y][x] = PathmentTile(SceneTile)
                
    return level

loadLevelFile("../levels/default.txt")


