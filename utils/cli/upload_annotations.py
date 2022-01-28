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
format = sys.argv[5] if len(sys.argv) > 5 else 'CVAT 1.1'

labels = [{"name": "disc", "color": "#f68e83", "attributes": []}]

for filename in sorted(os.listdir(dir)):
    filepath = os.path.join(dir, filename)
    if os.path.isdir(filename):
        resources = [os.path.join(filepath, file) for file in os.listdir(filepath)]
        run(['--auth', credentials, '--server-host', 'localhost', '--server-port',   '8080', 'create', '--labels', json.dumps(labels),
             '--annotation_path', annotations_path, '--annotation_format', format, '--project_id', project_id, '--image_quality', '100',
             filename, 'local', resources])

