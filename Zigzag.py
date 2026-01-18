import time, sys

indent = 0 # Spaces before the stars
indentIncreasing = True # Direction of movement

try:
    while True: # The main program loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.2)

        if indentIncreasing:
            indent += 1
            if indent == 20:
                indentIncreasing = False
        else:
            indent -= 1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()