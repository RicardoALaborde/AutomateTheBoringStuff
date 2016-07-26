'''
For today's challenge, you should calculate some simple statistical values based on a list of values.

Write functions that will calculate:
    The mean value
    The variance
    The standard deviation

Obviously, many programming languages and environments have standard functions for these
(this problem is one of the few that is really easy to solve in Excel!), but you are not
allowed to use those! The point of this problem is to write the functions yourself.
'''

listOfValues = [
0.5514,0.4081,0.0901,0.4637,0.5288,0.0831,
0.0054,0.0292,0.0548,0.4460,0.0009,0.9525,
0.2079,0.3698,0.4966,0.0786,0.4684,0.1731,
0.1008,0.3169,0.0220,0.1763,0.5901,0.4661,
0.6520,0.1485,0.0049,0.7865,0.8373,0.6934,
0.3973,0.3616,0.4538,0.2674,0.3204,0.5798,
0.2661,0.0799,0.0132,0.0000,0.1827,0.2162,
0.9927,0.1966,0.1793,0.7147,0.3386,0.2734,
0.5966,0.9083,0.3049,0.0711,0.0142,0.1799,
0.3180,0.6281,0.0073,0.2650,0.0008,0.4552
]

meanValue=0

def getMean():
    global meanValue
    sumOfValues = 0
    for i in listOfValues:
        sumOfValues += i
    meanValue = sumOfValues/len(listOfValues)
    print('The mean is: ' + str(meanValue))
getMean()

variance=0

def getVariance(mean):
    global variance
    sumOfXs=[]
    divisionOfXs=0
    sums=0
    for i in listOfValues:
        sumOfXs.append(i - mean)
    for x in sumOfXs:
        sums+=x**2
    divisionOfXs = sums/(len(listOfValues))
    print('The variance is: ' + str(divisionOfXs))
    variance = divisionOfXs

getVariance(meanValue)

def stDeviation(varValue):
    global variance
    print('The standard deviation is: ' + str(varValue**0.5))

stDeviation(variance)
