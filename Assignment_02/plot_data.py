import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.ticker import FormatStrFormatter
import argparse # Assist in the parsing of command line arguments 

def draw_plots( data_file, main_particle_mass, range_minimum, range_maximum, nbins=50): 
    data_list = [] # A list data type to hold data from an input file 

    # Open the first file and read its content
    with open(data_file, 'r' ) as file:
        for line in file: # Read the data obtained line by line 
            data_list.append(float(line))  # And convert them to their floating point equivalents

    # Draw a hisotgram with their data values of the first file
    fig, ax = plt.subplots(1,1,1)

    counts, bins, patches = plt.hist(data_list, bins=nbins, facecolor='yellow', edgecolor='gray', alpha=0.75, range=(range_minimum,range_maximum), histtype='stepfilled') 

    plt.xlabel('Range of detected Masses (GeV / c$^2$) in C.M.S experiment X')
    plt.ylabel('Frequency of the values')
    plt.title('Calculations of J / Psi\'s Mass (GeV / c$^2$) using Special Relativity (Einstein\'s equations)')

    ax.set_ylim(bottom=0.0)

    plt.grid(True)

    # Give ourselves some more room at the bottom of the plot
    plt.subplots_adjust(bottom=0.15) 

    plt.grid(True)

    plt.show()

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Look for different particles, J/Psi, Upsilon and the z-Boson in LHC data.')
    parser.add_argument('-f', '--file', type=str, nargs='+', help='The paths to the file(s) holding the input data.')
    parser.add_argument('-p', '--particle-mass', dest='particle_mass', type=float, nargs='+', help='A floating point number to hold the mass (GeV / c^2) of the particle to search for.')
    parser.add_argument('-r', '--range', nargs='+', help='Range of masses within which to plot the histograms.')
    parser.add_argument('-n', '--nbins', dest='nbins', type=int, help='Number of bins to use for the histogram,', default=50)

    args = parser.parse_args() 
    
    draw_plots (args.file[0], float(args.particle_mass[0]), float(args.range[0]), float(args.range[1]), args.nbins)
