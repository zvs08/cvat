#!/bin/bash
pushd $CVAT_CLI
/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 create_cvat_tasks_local.py "$@"
popd

