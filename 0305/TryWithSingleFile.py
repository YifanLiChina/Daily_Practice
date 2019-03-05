import numpy as np
import matplotlib

matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import scipy
from os import listdir

timestamps = [0 for i in range(6)]
vestStatuses = [0 for i in range(6)]
devXs = [0 for i in range(6)]
devZs = [0 for i in range(6)]
dists = [0 for i in range(6)]
signedAngles = [0 for i in range(6)]
durations = [0 for i in range(6)]
numberOfCollisions = [0 for i in range(6)]

filePath = './Results_20190304/Parking/20190304122130.txt'
myFile = open(filePath, 'r')
lines = myFile.readlines()
lineNum = 0

for line in lines:
    content = line.split(",")

    timestamps[lineNum] = content[0]
    vestStatuses[lineNum] = content[1]
    devXs[lineNum] = content[2]
    devZs[lineNum] = content[3]
    dists[lineNum] = content[4]
    signedAngles[lineNum] = content[5]
    durations[lineNum] = content[6]
    numberOfCollisions[lineNum] = content[7].strip()
    lineNum+=1

myFile.close()

print(timestamps)
print(vestStatuses)
print(devXs)
print(devZs)
print(dists)
print(signedAngles)
print(durations)
print(numberOfCollisions)
