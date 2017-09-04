#!/usr/bin/env python3
import sys
sys.path.insert(0,'ev3dev-lang-python')
from ev3dev import ev3

ev3.Sound.speak('Welcome to the E V 3 dev project!').wait()