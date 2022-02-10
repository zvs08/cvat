#!/usr/local/bin/python3
import os
import sys
import re
import zipfile

inner_path = os.path.join('annotations', 'instances_default.json')

# Extracts annotations from a dir with multiple zip files and put to corresponding video folders:
# - dir
#   - task_img_1992-37.23.mp4-2022_02_02_14_05_50-coco 1.0.zip
#   - task_img_8076-19.32.mp4-2022_01_30_12_06_58-coco 1.0.zip
#
# - out_dir
#   - img_1992-37.23.mp4
#       - annotations
#           - instances_default.json
#   - img_8076-19.32.mp4
#       - annotations
#           - instances_default.json
#
def extract_annotations(dir, out_dir):
    for filename in sorted(os.listdir(dir)):
        path = os.path.join(dir, filename)
        if os.path.isfile(path):
            video_name_match = re.search('task_(.*)-\\d+_\\d+_.+coco 1\\.0.*\\.zip', filename, re.IGNORECASE)
            if video_name_match:
                video_name = video_name_match.group(1)
                print("extracting " + video_name + "...")
                archive = zipfile.ZipFile(path)
                archive.extract(inner_path, os.path.join(out_dir, video_name))

if __name__ == '__main__':
    dir = sys.argv[1]
    out_dir = sys.argv[2] if len(sys.argv) > 2 else '.'
    extract_annotations(dir, out_dir)
