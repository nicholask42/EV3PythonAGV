#!/usr/bin/env python3
import sys
sys.path.insert(0,'ev3dev-lang-python')
from ev3dev import ev3

m = ev3.LargeMotor('outA')
m.run_timed(time_sp=3000, speed_sp=500)