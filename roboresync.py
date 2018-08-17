# creates new XROMM videos with 1/2 and 1 frame dropped for easy re-syncing. Applies an unsharp mask to counteract avi-avi transcoding quality loss, resulting videos perform better than raw in xmalab.
# unsharp luma=1-3 works well with a lower xmalab threshold, e.g. 1-2. Best tested is luma 2 on 90kV 2.2mA.
# only interpolate half-frames when absolutely necessary, minterpolate does well with isolated markers but creates ghosting when the background is busy, e.g. when markers cross over other stuff. Butterflow (see below) is slightly better but slower
# requires Python 3 (https://www.python.org/downloads/), FFmpeg (https://www.ffmpeg.org/download.html), ffmpy (https://pypi.org/project/ffmpy/). FFmpeg needs to be in PATH.

import os
import ffmpy

rootDir = input("Video folder (type or drag): ")
rawVideos = []

for root, dirs, files in os.walk(rootDir):
    for name in files:
        filename = os.path.join(root, name)
        if filename.endswith(".avi") and filename.find(".robo.") == -1:
            rawVideos.append(filename)
            print("Found XROMM video " + filename)
            continue
        else:
            continue

numRawVideos = len(rawVideos)
numRoboVideos = 0
print("Found a total of " + str(numRawVideos) + " XROMM videos")

for video in rawVideos:
    roboDrop0Filename = video[:-4] + ".robo.drop0.avi"
    roboDrop1Filename = video[:-4] + ".robo.drop1.avi"
    ffmpy.FFmpeg(inputs={video: None},outputs={roboDrop0Filename: ['-y','-q:v','0','-vf', 'unsharp=luma_amount=2.0']}).run()
    ffmpy.FFmpeg(inputs={video: None},outputs={roboDrop1Filename: ['-y','-q:v','0','-vf', 'select=gte(n\,1),unsharp=luma_amount=2.0']}).run()
    numRoboVideos = numRoboVideos + 1
    print("Enhanced " + str(numRoboVideos) + " of " + str(numRawVideos) + " raw videos")

    # for half-frame interpolation
        # ['-y','-q:v','0','-vf', 'minterpolate=fps=20:mi_mode=mci:mc_mode=obmc:me_mode=bilat:vsbmc=1,select=gte(n\,1),framestep=2,unsharp=luma_amount=2.0']}).run()



# autodeletes script at end of execution
    # os.remove(sys.argv[0])
