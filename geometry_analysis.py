import numpy
import os
import argparse

def calculate_distance(coords1, coords2):
    """
    Calculate distance between two atoms based on two pairs of xyz coordinates.
    Input: coords1, coords2
    Return: distance_12
    """
    x_distance = coords1[0] - coords2[0]
    y_distance = coords1[1] - coords2[1]
    z_distance = coords1[2] - coords2[2]
    distance_12 = numpy.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
    return distance_12

def bond_check(atom_distance, min_length = 0, max_length = 1.5):  # defaults
    """
    Check if a distance is a bond based on a minimum and maximum length.
    Inputs: distance, min_length, and max_length
    Return: True or False
    """
    if atom_distance > min_length and atom_distance <= max_length:
        return True 
    else:
        return False

if __name__ == "__main__":  # how to tell python this is main part of code
    
    parser = argparse.ArgumentParser("This script analyzes a user provided xyz file and outputs all the bond lengths.")
    parser.add_argument("xyz_file", help = "The filepath for the xyz file you want to analyze")
    args = parser.parse_args()

    file_location = args.xyz_file
    xyz_file = numpy.genfromtxt(fname = file_location, dtype = "unicode", skip_header = 2)
    symbols = xyz_file[:, 0]
    coordinates = xyz_file[:, 1:]
    coordinates = coordinates.astype(numpy.float)
    num_atoms = len(symbols)
    for num1 in range(0, num_atoms):
        for num2 in range(0, num_atoms):
            if num1 < num2:
                distance = calculate_distance(coordinates[num1], coordinates[num2])
                if bond_check(distance):  # if statements default as boolean
                    print(F"{symbols[num1]} to {symbols[num2]} : {distance:.3f}")