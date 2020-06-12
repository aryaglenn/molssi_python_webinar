import os
import numpy
import argparse

def open_file(filename):
    """
    Opens a file, reads file to a variable data, and closes the file.
    Input: filename
    Return: data
    """
    outfile = open(filename, "r")
    data = outfile.readlines()
    outfile.close()
    return data

def write_file(filename, energy_data):
    """
    Opens a new file, writes a list of numbers with the label Total Energy for each item on the list.
    Input: filename, energy_data
    Output: new file with name output
    """
    base_filename = filename.split(".")[0]
    output = F"{base_filename}_Etot.txt"
    filehandle = open(output, "w+")
    filehandle.write(F"Total energy:\n")
    for i in range(len(energy_data) - 2):
        total_energy = energy_data[i]
        filehandle.write(F"{total_energy}\n")
    filehandle.close()

# Tell argparse to handle arguments
parser = argparse.ArgumentParser("This script parses amber mdout files to extract the total energy.")  # ArgumentParser takes the argument description

# Tell argparse what arguments to expect
parser.add_argument("path", help = "This argument takes the name of the file to be analyzed.")


# Get arguments
args = parser.parse_args()
    

data = open_file(args.path)
energy_data = []


for line in data:
    if "Etot" in line:
        line = line.split()
        total_energy = line[2]
        energy_data.append(total_energy)
 
    
# will write file into the same directory that original input file is from    
write_file(args.path, energy_data)