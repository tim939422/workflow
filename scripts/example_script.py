import os
print('Search path specified by PYTHONPATH environment variable')
for path in os.environ.get('PYTHONPATH','').split(os.pathsep):
    print(path)

from package_a import foo
foo.func_1()