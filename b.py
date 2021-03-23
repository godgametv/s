import itertools
import threading
import time
import sys

done = False

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\rDone!!    ')

t + threading.Thread(target=animated)
t.start()

time.sleep(5)
done = False