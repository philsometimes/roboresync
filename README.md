# roboresync
Automatically sharpens and drops frames from biplanar x-ray videos for better tracking and easy re-synchronization

- creates new XROMM videos with 1/2 and 1 frame dropped for easy re-syncing. Applies an unsharp mask to counteract avi-avi transcoding quality loss, resulting videos perform better than raw in xmalab.
- unsharp luma=1-3 works well with a lower xmalab threshold, e.g. 1-2. Best tested is luma 2 on 90kV 2.2mA.
- only interpolate half-frames when absolutely necessary, minterpolate does well with isolated markers but creates ghosting when the background is busy, e.g. when markers cross over other stuff. Butterflow (see below) is slightly better but slower
- requires Python 3 (https://www.python.org/downloads/), FFmpeg (https://www.ffmpeg.org/download.html), ffmpy (https://pypi.org/project/ffmpy/). FFmpeg needs to be in PATH.
