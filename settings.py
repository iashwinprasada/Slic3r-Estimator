import os
# __file__ refers to the file settings.py
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')
APP_UPLOAD = os.path.join(APP_ROOT, 'static/Slic3r/bin/uploads')
APP_SLIC3R = os.path.join(APP_ROOT, 'static/Slic3r/bin')
