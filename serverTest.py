import sys

while (True):
    line = sys.stdin.readline()

    if line == 'forward\n':
        sys.stdout.write('moveForward python')
        sys.stdout.flush()
    elif line == 'left\n':
        sys.stdout.write('moveLeft python')
        sys.stdout.flush()
    elif line == 'right\n':
        sys.stdout.write('moveRight python')
        sys.stdout.flush()
    elif line == 'back\n':
        sys.stdout.write('moveBack python')
        sys.stdout.flush()
    elif line == 'stop\n':
        sys.stdout.write('STOP python')
        sys.stdout.flush()

