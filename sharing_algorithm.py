from order import *
import networkx as nx
import matplotlib.pyplot as plt
import math

#### Define system parameters
##### Maximum distance (in meters) for two order to be considered as neighbor
neighbor_radius = 1000

##### Maximum time interval (in minutes) for two neighbors to share delivery
sharing_time_interval = 30


def coordinatesDistance(coord_a, coord_b):
    lat1, lon1=coord_a
    lat2, lon2=coord_b

    R=6371000                               # radius of Earth in meters
    phi_1=math.radians(lat1)
    phi_2=math.radians(lat2)

    delta_phi=math.radians(lat2-lat1)
    delta_lambda=math.radians(lon2-lon1)

    a=math.sin(delta_phi/2.0)**2+\
       math.cos(phi_1)*math.cos(phi_2)*\
       math.sin(delta_lambda/2.0)**2
    c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))

    return R*c                         # output distance in meters 
