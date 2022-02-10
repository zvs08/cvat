#!/usr/local/bin/python3
import os
import sys
import re

#
# dir
#   - video_1
#       - ...
#   - video_2
#       - ...
#
dir = sys.argv[1]

labels = [{"name": "disc", "color": "#f68e83", "attributes": []}]

for filename in sorted(os.listdir(dir)):
    video_name = filename
    video_name_match = re.search('task_(.*)-\\d+_\\d+.*', filename, re.IGNORECASE)
    if video_name_match:
        video_name = video_name_match.group(1)
        print(video_name)
