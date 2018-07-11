#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
import shlex
import base64
import struct
import getpass
import platform
import subprocess

def get_terminal_size():
    current_os = platform.system()
    tuple_xy = None
    if current_os == 'Windows':
        tuple_xy = _get_terminal_size_windows()
        if tuple_xy is None:
            tuple_xy = _get_terminal_size_tput()
    if current_os in ['Linux', 'Darwin'] or current_os.startswith('CYGWIN'):
        tuple_xy = _get_terminal_size_linux()
    if tuple_xy is None:
        tuple_xy = (80, 25)
    return tuple_xy

def _get_terminal_size_windows():
    try:
        from ctypes import windll, create_string_buffer
        h = windll.kernel32.GetStdHandle(-12)
        csbi = create_string_buffer(22)
        res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
        if res:
            (bufx, bufy, curx, cury, wattr,
             left, top, right, bottom,
             maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
            sizex = right - left + 1
            sizey = bottom - top + 1
            return sizex, sizey
    except:
        pass

def _get_terminal_size_tput():
    try:
        cols = int(subprocess.check_call(shlex.split('tput cols')))
        rows = int(subprocess.check_call(shlex.split('tput lines')))
        return (cols, rows)
    except:
        pass

def _get_terminal_size_linux():
    def ioctl_GWINSZ(fd):
        try:
            import fcntl
            import termios
            cr = struct.unpack('hh',
            fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
            return cr
        except:
            pass
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        try:
            cr = (os.environ['LINES'], os.environ['COLUMNS'])
        except:
            return None
    return int(cr[1]), int(cr[0])

secret = "Q01EUg=="
recharge = 180

def fancyError(start,error,append):
    letters = " QqWwE$%^&QeRrTtYyUuIi(*&^%%$@#@$OoPpAaSsDdU^%@#$%%$#FfGgHhJjKkLlZzXxCcVv|BbNnMm!@#$%^&*()_{}[]:;\"',.<>?/"
    kill = False
    for ii in error:
        for i in letters:
            sys.stdout.write(start + i + append + "\r")
            if i == ii:
                start += ii
                if ii == error[-1:]:
                    kill = True
                break
            time.sleep(.001)
            sys.stdout.flush()
        if kill == True:
            break

    sys.stdout.write("\n")

def pBar(toolbar_width, char="-", sleep=0.1):
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1))
    for i in range(toolbar_width):
        time.sleep(sleep)
        sys.stdout.write(char)
        sys.stdout.flush()

    sys.stdout.write("\n")

print (""" _ _    _  ___  ______ _   _ _____ _   _ _____ _
| | |  | |/ _ \ | ___ \ \ | |_   _| \ | |  __ \ |
| | |  | / /_\ \| |_/ /  \| | | | |  \| | |  \/ |
| | |/\| |  _  ||    /| . ` | | | | . ` | | __| |
|_\  /\  / | | || |\ \| |\  |_| |_| |\  | |_\ \_|
(_)\/  \/\_| |_/\_| \_\_| \_/\___/\_| \_/\____(_)
""")
key = getpass.getpass("Enter your access token: ")

if key != base64.b64decode(secret).decode('utf-8'):
    print ("""  ___                         ______           _          _
 / _ \                        |  _  \         (_)        | |
/ /_\ \ ___ ___ ___  ___ ___  | | | |___ _ __  _  ___  __| |
|  _  |/ __/ __/ _ \/ __/ __| | | | / _ \ '_ \| |/ _ \/ _` |
| | | | (_| (_|  __/\__ \__ \ | |/ /  __/ | | | |  __/ (_| |
\_| |_/\___\___\___||___/___/ |___/ \___|_| |_|_|\___|\__,_|
""")
    print ("ERROR: token invalid.")
    print ("This incident will be reported.")
else:
    print ("Verifying...")
    sizex, sizey = get_terminal_size()
    pBar(sizex-3, char="█", sleep=.5/(sizex-3))

    print ("""  ___                          _____                 _           _
 / _ \                        |  __ \               | |         | |
/ /_\ \ ___ ___ ___  ___ ___  | |  \/_ __ __ _ _ __ | |_ ___  __| |
|  _  |/ __/ __/ _ \/ __/ __| | | __| '__/ _` | '_ \| __/ _ \/ _` |
| | | | (_| (_|  __/\__ \__ \ | |_\ \ | | (_| | | | | ||  __/ (_| |
\_| |_/\___\___\___||___/___/  \____/_|  \__,_|_| |_|\__\___|\__,_|
    """)
    print ("Wellcome to iBoom!\nWith this program you can easily alienate Imperial Starships with just a few clicks of you keybord.")
    print ("WANNING: Galac-Tech Studios can not be held responsible for the loss of your planet due to crazy fast Imperial Starships.")
    print ("How many ships are incoming?")
    loop = int(input(">>> "))
    if loop > 0:
        if loop != 1:
            print ("What is their distance from Hoth in km?")
        else:
            print ("What is its distance from Hoth in km?")
        distanceToBase = float(input(">>> "))
        if distanceToBase >= 1000:
            distanceToRange = distanceToBase-1000
        else:
            distanceToRange = 0

        for x in range(loop):
            print ("What is ship #" + str(x+1) + "'s speed in km/h?")
            velocity = float(input(">>> "))
            timeTillImpact = distanceToBase/velocity*60*60
            if timeTillImpact < recharge:
                fancyError("|","ERROR: RUN!","|")
                break
            else:
                timeTillInRange = (distanceToRange/velocity*60*60)
                if timeTillInRange >= recharge:
                    timeTillShot = timeTillInRange
                else:
                    timeTillShot = recharge
                m, s = divmod(timeTillShot, 60)
                h, m = divmod(m, 60)
                msg = []
                if h != 0:
                    msg.append("%d hours" % (h))
                if m != 0:
                    msg.append("%d minutes" % (m))
                if s != 0:
                    msg.append("%d seconds" % (s))

                print ("Fire in : " + ", ".join(msg) + "!")
    else:
        print ("ERROR: No ships incoming.")
print ("© 2016 Galac-tech, Studios")
print ("Process Terminating...")
time.sleep(3)
print ("[Process completed]")
