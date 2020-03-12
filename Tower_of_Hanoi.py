"""
Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. 
The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
    1) Only one disk can be moved at a time.
    2) Each move consists of taking the upper disk from one of the stacks 
       and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
    3) No disk may be placed on top of a smaller disk.
"""


def tower(d, a, b, c):
    if d == 1:
        print('move form ' + a + ' to ' + b)
    else:
        tower(d-1, a, c, b)
        tower(1, a, b, c)
        tower(d-1, c, b, a)


d = 3
print(tower(d, 'A', 'B', 'C'))
