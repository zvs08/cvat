#!/usr/local/bin/python3
import os
import sys
import json
from cli import run

#
# dir
#   - video_1
#       - annotations
#           - instances_default.json
#       - images
#           - frame1.jpg
#           - frame2.jpg
#           - ....
#           - frameN.jpg
#   - video_2
#       - ...
#
dir = sys.argv[1]
project_id = f"{sys.argv[2]}"
credentials = sys.argv[3] if len(sys.argv) > 3 else 'admin:admin'

labels = [{"name": "disc", "color": "#f68e83", "attributes": []}]

for filename in sorted(os.listdir(dir)):
    print(filename + "...")
    if os.path.isdir(filename):
        print("Processing...")
        video_root = os.path.join(dir, filename)
        images_dir = os.path.join(video_root, "images")
        annotations_path = os.path.join(video_root, "annotations", "instances_default.json")
        if os.path.isdir(images_dir) and os.path.isfile(annotations_path):
            print("Uploading...")
            images = [os.path.join(images_dir, file) for file in sorted(os.listdir(images_dir))]
            run(['--auth', credentials, '--server-host', 'localhost', '--server-port', '8080', 'create', '--labels', json.dumps(labels),
                 '--annotation_path', annotations_path, '--annotation_format', 'COCO 1.0', '--project_id', project_id, '--image_quality', '70',
                 filename, 'local', images])
