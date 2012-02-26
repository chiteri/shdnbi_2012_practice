import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.ticker import FormatStrFormatter

data_list0 = [] # A list data type to hold data from first input file 
data_list1 = [] # A list data type to hold data from second input file 

j_psi_percentile = 3.1 / 100 # The percentage of mass of the J/psi particles plotted 
upsilon_percentile = 90 / 100 # The percentage of mass of the J/psi particles plotted 

# Open the first file and read its content
with open('../data/data_file_0.dat', 'r' ) as file0:
    for line in file0: # Read the data obtained line by line 
        data_list0.append(float(line))  # And convert them to their floating point equivalents

data_list0.sort() # Order the items in the list 

# Follow the same procedure for the second file
#with open('../data/data_file_1.dat', 'r' ) as file1:
#    for line in file1: # Read the data obtained line by line 
#        data_list1.append(float(line))  # And convert them to their floating point equivalents
		
#data_list1.sort() # Order the items in the list 

# Draw a hisotgram with their data values of the first file
fig, ax = plt.subplots(1,1,1)
# ax = fig.add_subplot(1,1,1)

counts, bins, patches = plt.hist(data_list0, 50, normed=1, facecolor='yellow', edgecolor='gray', alpha=0.75, range=(0.0, 100.0)) 

# Set the ticks to be at the edges of the bins.
ax.set_xticks(bins)

# Set the xaxis's tick labels to be formatted with 1 decimal place...
ax.xaxis.set_major_formatter(FormatStrFormatter('%0.1f'))

# Change the colors of bars at the edges...
j_psi_particles, upsilon_particles = np.percentile( data_list0, [ j_psi_percentile, upsilon_percentile ] )
for patch, rightside, leftside in zip(patches, bins[1:], bins[:-1]):
    if rightside < j_psi_particles:
        patch.set_facecolor('green')
    elif leftside > upsilon_particles:
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

# plt.xlabel('Range of data values')
# plt.ylabel('Frequency of the values')
#plt.title('Calculations of mass (GeV / c^2) using Classical mechanics (Newton\'s method)')

plt.grid(True)

# Give ourselves some more room at the bottom of the plot
#plt.subplots_adjust(bottom=0.15) 

#ax = fig.add_subplot(2,2,1)

#n, bins, patches = plt.hist(data_list1, 50, normed=1, facecolor='g', alpha=0.75, range=(0.0, 100.0)) 

plt.xlabel('Range of detected Masses (GeV / c^2) in C.M.S experiment X')
#plt.ylabel('Frequency of the values')
#plt.title('Calculations of mass using Special Relativity (Einstein\'s method)')

plt.grid(True)

plt.show()

if __name__ == "__main__": 
    import sys 
    plot_data (sys.argv)
