import matplotlib.pyplot as plt 
import numpy as np

data_list0 = [] # A list data type to hold data from first input file 
data_list1 = [] # A list data type to hold data from second input file 

# Open the first file and read its content
with open('../data/data_file_0.dat', 'r' ) as file0:
    for line in file0: # Read the data obtained line by line 
        data_list0.append(float(line))  # And convert them to their floating point equivalents

data_list0.sort() # Order the items in the list 

# Follow the same procedure for the second file
with open('../data/data_file_1.dat', 'r' ) as file1:
    for line in file1: # Read the data obtained line by line 
        data_list1.append(float(line))  # And convert them to their floating point equivalents
		
data_list1.sort() # Order the items in the list 

# Draw a hisotgram with their data values of the first file
fig = plt.figure(1)
ax = fig.add_subplot(211)

bins = plt.hist(data_list0, 50, normed=1, facecolor='g', alpha=0.75, range=(0.0, 100.0)) 
# plt.xlabel('Range of data values')
plt.ylabel('Frequency of the values')
plt.title('PLOT OF FIRST CMS DATA SET')

plt.grid(True)

# get the corners of the rectangles for the histogram
#left = np.array(bins[:-1])
#right = np.array(bins[1:])
#bottom = np.zeros(len(left))
#top = bottom + n 

# Draw a hisotgram with their data values of the second file
ax = fig.add_subplot(212)

bins = plt.hist(data_list1, 50, normed=1, facecolor='g', alpha=0.75, range=(0.0, 100.0)) 

plt.xlabel('Range of data values')
plt.ylabel('Frequency of the values')
plt.title('PLOT OF SECOND CMS DATA SET')

plt.grid(True)

plt.show()
