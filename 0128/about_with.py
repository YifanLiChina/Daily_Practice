"""
Credit:
    the following code is from example shown in
    Python Context Managers and the "with" Statement (__enter__ & __exit__)
    https://www.youtube.com/watch?v=iba-I4CrmyA
    by Python Training by Dan Bader
"""

with open('hello.txt','w') as f:
    f.write('hello world!')

# if we do not close the file, it may cause the program ends
# before the content is fully written into the file,
# which would therefore get lost in the memory
f = open('hello.txt','w')
try:
    f.write('hello world!')
finally:
    f.close()

# apart from these builtin functions like open() and close(),
# we can diy our own 'with' by setting context managers
class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with ManagedFile('manager.txt') as f:
    f.write('this is a file to test how context manager works')

mf = ManagedFile('manager2.txt')
# the above line only calls __init__
# thus if we try 'mf.file'
# the result would be:
# Traceback (most recent call last):
#   File "/Users/liyifan/Documents/GitHub/Daily_Practice/0128/about_with.py", line 39, in <module>
#     mf.file
# AttributeError: 'ManagedFile' object has no attribute 'file'
# because the function __enter__ has not been called
with mf as the_file:
    the_file.write('hello manager!')

# the later part of the video is about combining yield and with,
# interesting but not very relevant to my current work
