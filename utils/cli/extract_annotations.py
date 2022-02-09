#!/usr/local/bin/python3
import os
import sys
import re
import zipfile

inner_path = os.path.join('annotations', 'instances_default.json')

def extract_annotations(dir, out_dir):
    for filename in sorted(os.listdir(dir)):
        path = os.path.join(dir, filename)
        if os.path.isfile(path) and path.endswith('coco 1.0.zip'):
            video_name_match = re.search('task_(.*)-\\d+_\\d+_.+', filename, re.IGNORECASE)
            if video_name_match:
                video_name = video_name_match.group(1)
                print("extracting " + video_name + "...")
                archive = zipfile.ZipFile(path)
                archive.extract(inner_path, os.path.join(out_dir, video_name))

if __name__ == '__main__':
    dir = sys.argv[1]
    out_dir = sys.argv[2] if len(sys.argv) > 2 else '.'
    extract_annotations(dir, out_dir)
