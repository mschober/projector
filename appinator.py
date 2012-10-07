#!/usr/bin/env python
from sys import argv
import os
from create import Create
from destroy import Destroy

script, action, app_name = argv

class NewTest():
    def __init__(self, app_name):
        self.new_test(app_name)

    def new_test(self, app_name):
        open("app/test/" + app_name, 'w')

if action == "create":
    Create(app_name)
elif action == "destroy":
    Destroy(app_name)
elif action == "new-test":
    NewTest(app_name)
else:
    print "no action specified"

