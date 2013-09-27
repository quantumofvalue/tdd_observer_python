import optparse
import sys

import unittest

import os
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),"lib")))
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),"tests/helpers")))

USAGE = """%prog TEST_PATH
Run unit tests for App Engine apps.

TEST_PATH   Path to package containing test modules"""

def main(test_path):
    suite = unittest.loader.TestLoader().discover(test_path)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    parser = optparse.OptionParser(USAGE)
    options, args = parser.parse_args()
    if len(args) != 1:
        print 'Error: Exactly 1 argument required.'
        parser.print_help()
        sys.exit(1)
    TEST_PATH = args[0]
    main(TEST_PATH)
