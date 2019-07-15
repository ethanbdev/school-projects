import math

def euclidean(x1, y1, x2, y2):
    #formula taken from: http://mathworld.wolfram.com/Distance.html
    dx = x2 - x1
    dy = y2 - y1
    temp = (math.pow(dx,2)) + (math.pow(dy,2))
    return round(math.sqrt(temp),4)

def manhattan(x1, y1, x2, y2):
    #formula take from: https://xlinux.nist.gov/dads//HTML/manhattanDistance.html
    dx = x1 - x2
    dy = y1 - y2
    return round((math.fabs(dx) + math.fabs(dy)),4)

def haversine(x1, y1, x2, y2):
    #formula taken from: http://www.movable-type.co.uk/scripts/gis-faq-5.1.html (US Census Bureau GIS FAQ)
    dx = x2 - x1
    dy = y2 - y1
    a = pow(math.sin(dy/2),2) + math.cos(y1) * math.cos(y2) * pow(math.sin(dx/2),2)
    c = 2 * math.pow(math.sin((min(1, math.sqrt(a)))),-1)
    return round(c,4)
    #return d = R * c if you knew radius of object