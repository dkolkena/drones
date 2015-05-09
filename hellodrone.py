#!/usr/bin/env python

import time
from turtledrone import TRDrone 
drone = TRDrone() 
drone.takeoff()
drone.write("{} says hi to {}".format('Daniel', drone.name))
time.sleep(5)
drone.land()
drone.halt()