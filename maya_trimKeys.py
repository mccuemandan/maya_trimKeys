import maya.cmds as cmds

def trimKeys(timeRange, multiple):
     selected = cmds.ls(sl=True)
     keyframes = []

     for i in range(timeRange):
        keyframes.append(i)

     for i in range(timeRange):
        if i%multiple == 0:
            keyframes.remove(i)

     for i in keyframes:
        for s in selected:
            print  "delete key " + str(i) + " of " + str(s)
            currentFrame = int(i)
            cmds.cutKey(s, time = (currentFrame, currentFrame))
