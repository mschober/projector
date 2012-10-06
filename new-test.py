from sys import argv
import os

script, test_name = argv

def new_test(test_name):
    open(test_name, 'w')
