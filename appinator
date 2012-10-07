#!/usr/bin/env python
#http://docs.python.org/library/optparse.html

from sys import argv
import os
from create import Create
from destroy import Destroy
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-n', '--name', dest='app_name', default='app')
parser.add_option('-c', '--create', action="store_true", dest='create_action')
parser.add_option('-d', '--destroy', action="store_true", dest='destroy_action')
(options, args) = parser.parse_args(argv)

app_name = options.app_name

if options.create_action:
    Create(app_name)
elif options.destroy_action:
    Destroy(app_name)
else:
    print "no action specified"

