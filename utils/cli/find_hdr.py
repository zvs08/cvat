#!/usr/local/bin/python3
import os
import sys
import subprocess

#
# dir
#   - video_1.mov
#   - video_2.mp4
#   - ...
#
dir = sys.argv[1]
hdr_count = 0
total = 0

for filename in sorted(os.listdir(dir)):
    if os.path.isfile(filename) and filename.endswith('.mov'):
        cmd = ['-show_streams', '-v', 'error', os.path.join(dir, filename)]

        proc1 = subprocess.Popen(['ffprobe', '-show_streams', '-v', 'error', os.path.join(dir, filename)], stdout=subprocess.PIPE)
        proc2 = subprocess.Popen(['grep', 'bt2020'], stdin=proc1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc1.stdout.close()  # Allow proc1 to receive a SIGPIPE if proc2 exits.
        out, err = proc2.communicate()
        total = total + 1
        if len(out) > 2:
            print(filename)
            hdr_count = hdr_count +1
print("HDR: {} Total: {}", hdr_count, total)
