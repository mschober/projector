from sys import argv
import os

script, app_name = argv

class Create():
    def __init__(self, app_name):
        self.create(app_name)
        self.package(app_name)

    def create(self, app_name):
        print "Creating app structure"
        self.create_directories(app_name)
        os.system("tree %r" % app_name)

    def package(self, app_name):
        print "Making into packages"
        self.to_packages(app_name)
        os.system("tree %r" % app_name)

    def create_directories(self, app_name):
        if not os.path.exists(app_name + "/src"):
            os.makedirs(app_name + "/src")

        if not os.path.exists(app_name + "/test"):
            os.makedirs(app_name + "/test")

    def to_packages(self, app_name):
        open(app_name + "/src/" + "__init__.py", 'w')
        open(app_name + "/test/" + "__init__.py", 'w')

from shutil import rmtree
class Destroy():
    def __init__(self, app_name):
        self.destroy_directories(app_name)

    def destroy_directories(self, app_name):
        if os.path.exists(app_name):
            print "Deleting app structure '%s'" % app_name
            rmtree(app_name)
        else:
            print "No app named '%s'" % app_name
