#!/usr/local/bin/python3
import os
import sys
import json
from cli import run

#
# dir
#   - video_1
#       - frame1.jpg
#       - frame2.jpg
#       - ....
#       - frameN.jpg
#   - video_2
#       - ...
#
dir = sys.argv[1]
annotations_path = sys.argv[2]
project_id = f"{sys.argv[3]}"
credentials = sys.argv[4] if len(sys.argv) > 4 else 'admin:admin'

labels = [{"name": "disc", "color": "#f68e83", "attributes": []}]

for filename in sorted(os.listdir(dir)):
    filepath = os.path.join(dir, filename)
    if os.path.isdir(filename):
        resources = [filepath + "/" + file for file in os.listdir(filepath)]
        run(['--auth', credentials, '--server-host', 'localhost', '--server-port', '8080', 'create', '--labels', json.dumps(labels),
             '--annotation_path', annotations_path, '--annotation_format', 'COCO 1.0', '--project_id', project_id, '--image_quality', '70',
             filename, 'local', resources])
    else:
        run(['--auth', credentials, '--server-host', 'localhost', '--server-port', '8080', 'create', '--labels', json.dumps(labels),
             '--annotation_path', annotations_path, '--annotation_format', 'COCO 1.0', '--project_id', project_id, '--image_quality', '70',
             filename, 'local', filepath])
