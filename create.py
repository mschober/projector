from sys import argv
import os

script, app_name = argv

def create_directories(app_name):
    if not os.path.exists(app_name + "/src"):
        os.makedirs(app_name + "/src")

    if not os.path.exists(app_name + "/test"):
        os.makedirs(app_name + "/test")

def destroy_directories(app_name):
    if os.path.exists(app_name + "/src"):
        os.removedirs(app_name + "/src")

    if os.path.exists(app_name + "/test"):
        os.removedirs(app_name + "/test")

print "Creating app structure"
create_directories(app_name)
os.system("tree %r" % app_name)

print "Deleting app structure"
destroy_directories(app_name)
