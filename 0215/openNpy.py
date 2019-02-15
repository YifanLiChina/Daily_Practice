import numpy as np

eye0 = np.load('npy/eye0_timestamps.npy',encoding = "latin1")
saveEye0 = open('txt/eye0.txt','w')
for i in eye0:
    print(i, file=saveEye0)
saveEye0.close()

eye1 = np.load('npy/eye1_timestamps.npy',encoding = "latin1")
saveEye1 = open('txt/eye1.txt','w')
for i in eye1:
    print(i, file=saveEye1)
saveEye1.close()

gaze = np.load('npy/gaze_timestamps.npy',encoding = "latin1")
saveGaze = open('txt/gaze.txt','w')
for i in gaze:
    print(i, file=saveGaze)
saveGaze.close()

world = np.load('npy/world_timestamps.npy',encoding = "latin1")
saveWorld = open('txt/world.txt','w')
for i in world:
    print(i, file=saveWorld)
saveWorld.close()

