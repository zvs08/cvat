#!/usr/local/bin/python3
import os
import sys
import subprocess

# Converts multiple video files to images in corresponding individual folder:
# - dir
#   - IMG_0152-11.75.mp4
#   - IMG_1916-18.75.mp4
#
# - out_dir
#   - img_0152-11.75.mp4
#       - images
#           - frame_000001.jpg
#           - frame_000002.jpg
#           - ...
#   - img_1916-18.75.mp4
#       - images
#           - frame_000001.jpg
#           - frame_000002.jpg
#           - ...
#
def video_to_images(dir, out_dir):
    for filename in sorted(os.listdir(dir)):
        path = os.path.join(dir, filename)
        if os.path.isfile(path):
            out_path = os.path.join(out_dir, filename).lower()
            print("converting " + filename + "...")
            if not os.path.isdir(out_path):
                os.mkdir(out_path)
                os.mkdir(os.path.join(out_path, 'images'))
            image_path_pattern = os.path.join(out_path, 'images', 'frame_%06d.PNG')
            cmd_ffmpeg = ['ffmpeg', '-i', path, '-start_number', '0', image_path_pattern]

            if subprocess.run(cmd_ffmpeg).returncode == 0:
                print("FFMpeg finished successfully")
            else:
                print("There was an error running FFMpeg")

if __name__ == '__main__':
    dir = sys.argv[1]
    out_dir = sys.argv[2] if len(sys.argv) > 2 else '.'
    video_to_images(dir, out_dir)
