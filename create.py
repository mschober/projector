from sys import argv
import os

script, app_name = argv

if not os.path.exists(app_name + "/src"):
    os.makedirs(app_name + "/src")

if not os.path.exists(app_name + "/test"):
    os.makedirs(app_name + "/test")


