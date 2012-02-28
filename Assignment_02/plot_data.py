import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.ticker import FormatStrFormatter
import argparse # Assist in the parsing of command line arguments 

def draw_plots( data_file, main_particle_mass, range_minimum, range_maximum ): 
    data_list = [] # A list data type to hold data from an input file 

    # Open the first file and read its content
    with open(data_file, 'r' ) as file:
        for line in file: # Read the data obtained line by line 
            data_list.append(float(line))  # And convert them to their floating point equivalents

    data_list.sort() # Order the items in the list 

    # Draw a hisotgram with their data values of the first file
    fig, ax = plt.subplots(1,1,1)

    counts, bins, patches = plt.hist(data_list, 50, normed=1, facecolor='yellow', edgecolor='gray', alpha=0.75, range=(range_minimum, range_minimum)) 

    # Set the ticks to be at the edges of the bins.
    ax.set_xticks(bins)

    # Set the xaxis's tick labels to be formatted with 1 decimal place...
    ax.xaxis.set_major_formatter(FormatStrFormatter('%0.1f')) 
	
    main_particle_percentile = (main_particle_mass / range_maximum) # The percentage of mass of the J/psi particles plotted 
    other_particle_percentile = (range_maximum - main_particle_mass) / range_maximum # The percentage of mass of the J/psi particles plotted 

    # Change the colors of bars at the edges...
    main_particles, other_particles = np.percentile( data_list, [ main_particle_percentile, other_particle_percentile ] )

    for patch, rightside, leftside in zip(patches, bins[1:], bins[:-1]):
        if rightside < main_particles:
            patch.set_facecolor('green')
        elif leftside > other_particles:
            patch.set_facecolor('red')
		
    # Label the raw counts and the percentages below the x-axis...
    bin_centers = 0.5 * np.diff(bins) + bins[:-1]

    for count, x in zip(counts, bin_centers):
        # Label the raw counts
        ax.annotate(str(count), xy=(x, 0), xycoords=('data', 'axes fraction'),
            xytext=(0, -18), textcoords='offset points', va='top', ha='center') 
    
    # Label the percentages
    percent = '%0.0f%%' % (100 * float(count) / counts.sum())
    ax.annotate(percent, xy=(x, 0), xycoords=('data', 'axes fraction'),
        xytext=(0, -32), textcoords='offset points', va='top', ha='center')

    plt.xlabel('Range of detected Masses (GeV / c^2) in C.M.S experiment X')
    plt.ylabel('Frequency of the values')
    plt.title('Calculations of mass (GeV / c^2)')
    # using Classical mechanics (Newton\'s method)

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

    args = parser.parse_args() 
    
    draw_plots (args.file[0], float(args.particle_mass[0]), float(args.range[0]), float(args.range[1]))
