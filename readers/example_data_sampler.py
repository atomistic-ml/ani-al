import sys
sys.path.append("lib/")

import pyanitools as pya

# Set the HDF5 file containing the data (you must untar the data file first)
hdf5file = '../data/data-1.h5'

# Construct the data loader class
adl = pya.anidataloader(hdf5file)

# Print the species of the data set one by one
for data in adl:

    # Extract the data
    P = data['path']
    X = data['coordinates']
    E = data['energy']
    S = data['species']

    # Print the data
    print("Path:   ", P)
    print("  Symbols:     ", S)
    print("  Coordinates: ", X)
    print("  Energies:    ", E, "\n")

# Closes the H5 data file
adl.cleanup()
