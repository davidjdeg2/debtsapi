#!/usr/bin/env python
import os
import sys
from main import create_app

sys.path.append("/etc/debtsapi/app")

application = create_app('app')
