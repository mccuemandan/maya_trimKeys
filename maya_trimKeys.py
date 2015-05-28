import maya.cmds as cmds

def trimKeys(startFrame, endFrame, multiple):
     selected = cmds.ls(sl=True)

     timeRange = endFrame - startFrame

     keyframes = []

     for i in range(timeRange):
        frame = i + startFrame
        keyframes.append(frame)

     for i in range(timeRange):
        if i%multiple == 0:
            frame = i + startFrame
            keyframes.remove(frame)

     for i in keyframes:
        for s in selected:
            print  "delete key " + str(i) + " of " + str(s)
            currentFrame = int(i)
            cmds.cutKey(s, time = (currentFrame, currentFrame))
