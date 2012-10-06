from sys import argv
import os
from shutil import rmtree

script, app_name = argv

def destroy_directories(app_name):
    if os.path.exists(app_name):
        print "Deleting app structure '%s'" % app_name
        rmtree(app_name)
    else:
        print "No app named '%s'" % app_name

destroy_directories(app_name) 
