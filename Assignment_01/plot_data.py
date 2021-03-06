import matplotlib.pyplot as plt 
import numpy as np

data_list = [] # Create a list data type to hold the data from input files 

# Open the files and read their contents
with open('../resources/data_file_0.dat', 'r' ) as file:
    for line in file: # Read the data obtained line by line 
        data_list.append(float(line))  # And convert them to their floating point equivalents

# Draw a hisotgram with their data values
fig = plt.figure()
ax = fig.add_subplot(111)

bins = plt.hist(data_list, 50, normed=1, facecolor='g', alpha=0.75, range=(0.0, 100.0)) 

# get the corners of the rectangles for the histogram
#left = np.array(bins[:-1])
#right = np.array(bins[1:])
#bottom = np.zeros(len(left))
#top = bottom + n 

plt.xlabel('Range of data Masses detected during C.M.S experiment Y')
plt.ylabel('Frequency of the values')
plt.title('CALCULATION OF MASSES DETECTED USING CLASSICAL MECHANICS')

plt.grid(True)

plt.show()
