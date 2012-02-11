import csv 
import matplotlib.pyplot as plt 

spamReader = csv.reader(open('data/data_file_0.dat'), delimiter=' ', quotechar='|') 

xls_list = [] 

for row in spamReader:
    xls_list.append (row)

plt.plot( xls_list )

plt.xlabel('Cells in Worksheet')
plt.ylabel('Values of excel column')
plt.title('Plot of First CMS data')
plt.grid(True)

plt.show()
