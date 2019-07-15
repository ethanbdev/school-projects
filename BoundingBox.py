def boundingbox(pointlist):
    xmin = 100000
    ymin = 100000
    xmax = 0
    ymax = 0
    for point in pointlist:
        tempx = point[0]
        if tempx > xmax:
            xmax = tempx
        if tempx < xmin:
            xmin = tempx
        tempy = point[1]
        if tempy > ymax:
            ymax = tempy
        if tempy < ymin:
            ymin = tempy
    return xmin, ymin, xmax, ymax

pointlist = [[8,5], [1,23], [10,4], [4,12], [3,2]]
print(boundingbox(pointlist))   