import numpy as np
from math import sqrt 
import argparse 

def determine_mass(data_file): 	 
    # Format the headings for the data before display 
    print repr('Energy').ljust(7), repr('X-coord').ljust(7), repr('Y-coord').ljust(7), repr('Z-coord').ljust(7), repr('Charge').ljust(7) #, repr('Invariant Mass').ljust(20)      
    print repr('++++++').ljust(7), repr('+++++++').ljust(7), repr('+++++++').ljust(7), repr('+++++++').ljust(7), repr('++++++').ljust(6) #, repr('++++++++++++++').ljust(20)

    events_processed = 0 # A number to hold the number of particle detailed read  
	# Four momentum information for an event. Use lists with lengths equal to the number of daughter particles 
    energy = [0.00]*2 # An empty list to hold the values of e
    x_coord = [0.00]*2 # An empty list to hold the values of px
    y_coord = [0.00]*2 # An empty list to hold the values of py
    z_coord = [0.00]*2 # An empty list to hold the values of pz
    charge = [0.0]*2 # An empty list to hold the values of q
	
    # Open the first file and read its content    
    with open(data_file, 'r' ) as file: 		
        for particle_details in file: # Read the data obtained row by row 
            values = particle_details.split() # The first item can tell us if we are looking at daughter particles or four momentum values  
			
            invariant_mass = 0.00 # The invariant mass for each parent particle  
			
            if len( values[0] ) == 1: # The events expected from a decay 
                daughter_particles = int(values[0]) # The first line represents the number of particles to expect in subsequent events for the decay
 
            elif len( values[0] ) > 1: 
                # particles_processed = 0 
                if events_processed < daughter_particles: 
                    # Get the four momentum data from the list 
                    energy[events_processed], x_coord[events_processed], y_coord[events_processed], z_coord[events_processed], \
					charge[events_processed] = float(values[0]), float(values[1]), float(values[2]), float(values[3]),  int(values[4])  			
                    print repr(energy[events_processed]).rjust(8), repr(x_coord[events_processed]).rjust(8), \
					repr(y_coord[events_processed]).rjust(8), repr(z_coord[events_processed]).rjust(8), repr(charge[events_processed]).rjust(8) 
                    events_processed += 1 
					
                    # break # Temporarily stop execution, force the program to go to the next outer loop iteration 
                    if events_processed == daughter_particles:   
                        # print z_coord, 				
                        invariant_mass = calc_invariant_mass( energy, x_coord, y_coord, z_coord, daughter_particles ) 					
                        print 'Invariant Mass: %3.30f'%invariant_mass # 	
                        print repr('----------------------------------------------').ljust(30)
                        events_processed = 0 # Reset the counter
						
################################################################################
# Calculate the invariant mass according to the theory of special relativity
################################################################################
def calc_invariant_mass(E, px, py, pz, number_of_events):	
    energies = px_sum = py_sum = pz_sum =  0.00 
    
    for n in range (0, number_of_events ): 
        energies  += E[n]
        px_sum += px[n] 
        py_sum += py[n] 
        pz_sum += pz [n]
        # break # Force the program to iterate to the next loop, stop execution temporarily
    
    try:
        return sqrt( energies**2 - (px_sum**2 + py_sum**2 + pz_sum**2) ) # Return the root of the value obtained
    except ValueError: 
	    return 'Houston, we have a problem!' 
			
if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Calculate the invariant mass of parent particles after a decay into muons in a p-p collision.') 
    parser.add_argument('-f', '--file', type=str, nargs='+', help='The paths to the file(s) holding the input data.') 
	
    args = parser.parse_args() 
	
    determine_mass (args.file[0])
