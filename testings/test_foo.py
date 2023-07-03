# put this cell on top for every test file
import os
import sys
working_dir = os.getcwd()
source_dir = working_dir + '/src'
sys.path.append(source_dir)

from package_a.foo import func_2

def test_func_2():
    assert func_2(2) == 4