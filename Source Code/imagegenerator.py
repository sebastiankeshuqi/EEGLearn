# To extract the data file in the "Sample Data" folder

import os

import math

import scipy.io


def covert_locations_to_2D():

    # Get the folder path in which this python file exists
    current_path = os.path.dirname(__file__)

    # Get the path of "Sample Data" folder
    data_file_path = os.path.relpath(
        '..\\Sample Data\\Neuroscan_locs_orig.mat', current_path)

    # Open the location data of electrodes
    locations = scipy.io.loadmat(data_file_path)

    loc_3d = locations['A']

    loc_2d = [loc_2d.append(azimuthal_equidistant_projection(*i)) for i in loc_3d]  # Covert them from 3D to 2D


def azimuthal_equidistant_projection(x,y,z):
    '''
    Computes the Azimuthal Equidistant Projection of input point in 3D Cartesian Coordinates.
    :param pos_3d: position in 3D Cartesian coordinates. It is a list in this form [x, y, z].
    We use (0,0,0) as the center point. (0,0,0) will project to (0,0) in this 2D map.
    '''

    # Transform cartesian to spherical coordinates
    r = math.sqrt(x**2 + y**2 + z**2)
    phi = math.atan2(z, math.sqrt(x**2 + y**2))
    theta = math.atan2(x,y)
