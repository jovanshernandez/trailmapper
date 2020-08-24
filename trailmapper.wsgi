#! /usr/bin/python

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/ubuntu/trailmapper/')
from my_flask_app import app as application
application.secret_key = 'trailmapperpw123'
