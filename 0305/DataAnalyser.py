import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from os import listdir
from sklearn import linear_model

def singleFileReader(filePath):
    # initialization
    trials = [int(i) for i in range(1,7,1)]
    timestamps = [0 for i in range(6)]
    vestStatuses = [0 for i in range(6)]
    devXs = [0 for i in range(6)]
    devZs = [0 for i in range(6)]
    dists = [0 for i in range(6)]
    signedAngles = [0 for i in range(6)]
    durations = [0 for i in range(6)]
    numberOfCollisions = [0 for i in range(6)]

    myFile = open(filePath, 'r')
    lines = myFile.readlines()
    lineNum = 0

    for line in lines:
        content = line.split(",")
        timestamps[lineNum] = float(content[0])
        vestStatuses[lineNum] = float(content[1])
        devXs[lineNum] = float(content[2])
        devZs[lineNum] = float(content[3])
        dists[lineNum] = float(content[4])
        signedAngles[lineNum] = float(content[5])
        durations[lineNum] = float(content[6])
        numberOfCollisions[lineNum] = float(content[7].strip())
        lineNum+=1

    myFile.close()
    return trials,timestamps,vestStatuses,devXs,devZs,dists,signedAngles,durations,numberOfCollisions


def printAll(timestamps,vestStatuses,devXs,devZs,dists,signedAngles,durations,numberOfCollisions):
    print(timestamps)
    print(vestStatuses)
    print(devXs)
    print(devZs)
    print(dists)
    print(signedAngles)
    print(durations)
    print(numberOfCollisions)


def plotAverage(X, Y):
    Y1 = [np.mean(Y[:3]) for i in range(3)]
    Y2 = [np.mean(Y[3:6]) for i in range(3)]
    plt.plot(X[:3],Y1, color='red', linewidth=1.5)
    plt.plot(X[3:6],Y2, color='red', linewidth=1.5)


def plotRegression(X,X_train,Y):
    Y_train = np.array(Y)
    regr = linear_model.LinearRegression()
    regr.fit(X_train,Y_train)
    # X_test = [i for i in range(1,20,1)]
    devZs_pred = regr.predict(X_train)
    plt.plot(X, devZs_pred, color='green', linewidth=1)


def plotSingleFile(filePath, i):
    trials,timestamps,vestStatuses,devXs,devZs,dists,signedAngles,durations,numberOfCollisions = singleFileReader(filePath)
    trials_train = np.array(trials).reshape(-1, 1)
    printAll(timestamps,vestStatuses,devXs,devZs,dists,signedAngles,durations,numberOfCollisions)

    fig = plt.figure()
    fig.suptitle('Participant: '+str(i+1))

    ax = fig.add_subplot(332)
    vestStatusesPlot = plt.scatter(trials,vestStatuses,marker="x",s=10)
    plt.xlabel("trials")
    plt.ylabel("vest status")
    plt.xlim([1,6])
    ax = vestStatusesPlot

    ax = fig.add_subplot(334)
    devXsPlot = plt.scatter(trials,devXs,marker="x",s=10)
    plotAverage(trials,devXs)
    plotRegression(trials,trials_train,devXs)
    # plot labels
    plt.xlabel("trials")
    plt.ylabel("deviation in X-axis")
    plt.xlim([1,6])
    ax = devXsPlot

    ax = fig.add_subplot(335)
    devZsPlot = plt.scatter(trials,devZs,marker="x",s=10)
    plotAverage(trials,devZs)
    plotRegression(trials,trials_train,devZs)
    # plot labels
    plt.xlabel("trials")
    plt.ylabel("deviation in Z-axis")
    plt.xlim([1,6])
    ax = devZsPlot

    ax = fig.add_subplot(336)
    distsPlot = plt.scatter(trials,dists,marker="x",s=10)
    plotAverage(trials,dists)
    plotRegression(trials,trials_train,dists)
    # plot labels
    plt.xlabel("trials")
    plt.ylabel("general deviation")
    plt.xlim([1,6])
    ax = distsPlot

    ax = fig.add_subplot(337)
    signedAnglesPlot = plt.scatter(trials,signedAngles,marker="x",s=10)
    plotAverage(trials,signedAngles)
    plotRegression(trials,trials_train,signedAngles)
    # plot labels
    plt.xlabel("trials")
    plt.ylabel("deviation in angle")
    plt.xlim([1,6])
    ax = signedAnglesPlot

    ax = fig.add_subplot(338)
    durationsPlot = plt.scatter(trials,durations,marker="x",s=10)
    plotAverage(trials,durations)
    plotRegression(trials,trials_train,durations)
    # plot labels
    plt.xlabel("trials")
    plt.ylabel("duration")
    plt.xlim([1,6])
    ax = durationsPlot

    ax = fig.add_subplot(339)
    numberOfCollisionsPlot = plt.scatter(trials,numberOfCollisions,marker="x",s=10)
    plotAverage(trials,numberOfCollisions)
    plotRegression(trials,trials_train,numberOfCollisions)
    # plot labels
    plt.xlabel("trials")
    plt.ylabel("number of collisions")
    plt.xlim([1,6])
    ax = numberOfCollisionsPlot

    plt.tight_layout()
    plt.show()


# find the files
parkingfiles = listdir("./Results_20190304/Parking")

for i in range(len(parkingfiles)):
    filePath = './Results_20190304/Parking/' + parkingfiles[i]
    plotSingleFile(filePath, i)

# filePath = './Results_20190304/Parking/' + parkingfiles[0]
# plotSingleFile(filePath, 0)
