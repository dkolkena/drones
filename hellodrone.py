#!/usr/bin/env python

import time
from turtledrone import TRDrone 

drony = TRDrone()

def draw_square(drone):
	""" Draws a square with a drone
	"""
	d = drone
	d.takeoff()
	for i in range(10):
		d.move_forward()
	for i in range(18):
		d.turn_left()
	for i in range(10):
		d.move_forward()
	for i in range(18):
		d.turn_left()
	for i in range(10):
		d.move_forward()
	for i in range(18):
		d.turn_left()
	for i in range(10):
		d.move_forward()
	for i in range(18):
		d.turn_left()
	d.land()
	time.sleep(5)
	d.halt()

draw_square(drony)