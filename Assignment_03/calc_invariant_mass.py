import numpy as np
# from math import sqrt 
import argparse 

def determine_mass(data_file): 	 
    # Format the headings for the data before display 
    print repr('Energy').ljust(7), repr('X-coord').ljust(7), repr('Y-coord').ljust(7), repr('Z-coord').ljust(7), repr('Charge').ljust(7), repr('Invariant Mass').ljust(20)      
    print repr('++++++').ljust(7), repr('+++++++').ljust(7), repr('+++++++').ljust(7), repr('+++++++').ljust(7), repr('++++++').ljust(6), repr('++++++++++++++').ljust(20)
	
    # Open the first file and read its content    
    with open(data_file, 'r' ) as file: 		
        for particle_details in file: # Read the data obtained line by line 
            values = particle_details.split() # The first item can tell us if we are looking at daughter particles or four momentum values  
			
            # Four momentum information for an event. Use lists with lengths equal to the number of daughter particles 
            energy = [0.00]*len( values[0] ) # An empty list to hold the values of e
            x_coord = [0.00]*len( values[0] ) # An empty list to hold the values of px
            y_coord = [0.00]*len( values[0] ) # An empty list to hold the values of py
            z_coord = [0.00]*len( values[0] ) # An empty list to hold the values of pz
            charge = [0.0]*len( values[0] ) # An empty list to hold the values of q
			
            invariant_mass = 0.00 # The invariant mass for each parent particle  
            # daughter_particles = 0 
			
            if len( values[0] ) == 1: # We expect single digit (1, 2 ... 9, 2 mostly) daughter particles from decays 
                daughter_particles = int(values[0]) # The first line represents the number of particles to expect in subsequent events for the decay
 
            elif len( values[0] ) > 1: 
                for n in range (0, daughter_particles): 
                    # print 'Hello World!!'
                    # Get the four momentum data from the list 
                    energy[n], x_coord[n], y_coord[n], z_coord[n], charge[n] = float(values[0]), float(values[1]), float(values[2]), float(values[3]),  int(values[4])  			
                    print repr(energy[n]).rjust(8), repr(x_coord[n]).rjust(8), repr(y_coord[n]).rjust(8), repr(z_coord[n]).rjust(8), repr(charge[n]).rjust(8), 
                    break # Temporarily stop execution, force the program to go to the next outer loop iteration 
	
                invariant_mass = calc_invariant_mass( energy, x_coord, y_coord, z_coord, daughter_particles ) 					
                print repr(invariant_mass).rjust(20)	
						
################################################################################
# Calculate the invariant mass according to the theory of special relativity
################################################################################
def calc_invariant_mass(E, px, py, pz, number_of_events):	
    energies, coordinates =  0.00, 0.00 
    
    for n in range (0, number_of_events ): 
        energies  += E[n]
        coordinates += px[n] + py[n] + pz [n]
        break # Force the program to iterate to the next loop, stop execution temporarily

    return np.sqrt(energies**2 - coordinates**2) # Return the root of the value obtained
			
if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Calculate the invariant mass of parent particles after a decay into muons in a p-p collision.') 
    parser.add_argument('-f', '--file', type=str, nargs='+', help='The paths to the file(s) holding the input data.') 
	
    args = parser.parse_args() 
	
    determine_mass (args.file[0])
