from sys import argv
import os

script, app_name = argv

def create_directories(app_name):
    if not os.path.exists(app_name + "/src"):
        os.makedirs(app_name + "/src")

    if not os.path.exists(app_name + "/test"):
        os.makedirs(app_name + "/test")

print "Creating app structure"
create_directories(app_name)
os.system("tree %r" % app_name)

def to_packages(app_name):
    open(app_name + "/src/" + "__init__.py", 'w')
    open(app_name + "/test/" + "__init__.py", 'w')

print "Making into packages"
to_packages(app_name)
os.system("tree %r" % app_name)


