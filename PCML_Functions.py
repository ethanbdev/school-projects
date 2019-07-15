from pcml import *

@localoperation
#compute the factorial of the values in a single layer
def myLocalFactorial(self, locations, subdomains):
    return math.factorial(locations[0]['v'])
    
mylayer = myLocalFactorial(layer2)
mylayer.print_data()

@focaloperation
def myFocalPercentile(self, locations, subdomains):
    #numlower = number of values in neighborhood lower than our value, total = total values
    #assume 1 layer
    #returns percentile of neighbors lower than value
    numlower = 0.0
    total = -1.0
    arr=subdomains[0].bufferedlocgetarr(locations[0],1)
    for loc in arr.flat: #flat: in numpy, convert 2-d array to 1-d list
        if locations[0]['v'] < loc:
            numlower += 1.0
        total += 1.0
    return round(((total-numlower)/total)*100,2)
    #can also be formatted to be decimal, ratio, etc. 

# Test your focal operation
layer2=ReadASCIIGrid("./data/datam.asc")
mylayer = myFocalPercentile(layer2)
mylayer.print_data()