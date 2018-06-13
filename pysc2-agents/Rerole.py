#!/usr/bin/python
from subprocess import Popen
import sys
 
#filename = sys.argv[1]
while True:
    print("\nStarting ")
    p = Popen("python3 -m main --map=Simple64 --training=True --render=False --agent_race=T", shell=True)
    p.wait()
