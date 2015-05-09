#!/usr/bin/env python

import time
from turtledrone import TRDrone 

# drone = turtledrone.TRDrone()

def hello(drone):
	drone.takeoff()
	time.sleep(1)
	drone.land()
	drone.halt()

def spin():
	d = TRDrone()
	d.takeoff()
	time.sleep(1)
	m = map(lambda x, d=d: d.turn_left(), range(100))
	list(m)
	time.sleep(2)
	d.land()
	d.halt()

spin()