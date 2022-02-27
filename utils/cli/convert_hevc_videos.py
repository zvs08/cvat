#!/usr/local/bin/python3
import os
import sys
import subprocess
import os


#
# dir
#   - video_1.mov
#   - video_2.mp4
#   - ...
#
dir = sys.argv[1]
outdir = sys.argv[2]

for filename in sorted(os.listdir(dir)):
    if os.path.isfile(filename):
        outpath = os.path.splitext(os.path.join(outdir, filename))[0] + ".mp4"
        cmd_ffmpeg = ['ffmpeg', '-i', os.path.join(dir, filename), '-map', '0', '-c:v', 'libx264', '-crf', '17', '-c:a', 'copy', outpath, '-y']
        if subprocess.run(cmd_ffmpeg).returncode == 0:
            print("FFMpeg finished successfully")
        else:
            print("There was an error running FFMpeg")
