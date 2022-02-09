#!/usr/local/bin/python3
import os
import sys
import subprocess

def video_to_images(dir, out_dir):
    for filename in sorted(os.listdir(dir)):
        path = os.path.join(dir, filename)
        print("processing " + filename + "...")
        if os.path.isfile(path):
            out_path = os.path.join(out_dir, filename)
            print("converting " + filename + "...")
            if not os.path.isdir(out_path):
                os.mkdir(out_path)
                os.mkdir(os.path.join(out_path, 'images'))
            image_path_pattern = os.path.join(out_path, 'images', 'frame_%06d.jpg')
            cmd_ffmpeg = ['ffmpeg', '-i', path, image_path_pattern]

            if subprocess.run(cmd_ffmpeg).returncode == 0:
                print("FFMpeg finished successfully")
            else:
                print("There was an error running FFMpeg")

if __name__ == '__main__':
    dir = sys.argv[1]
    out_dir = sys.argv[2] if len(sys.argv) > 2 else '.'
    video_to_images(dir, out_dir)
