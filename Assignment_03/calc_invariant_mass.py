import argparse

def determine_mass(data_file): 
    daughter_particles = 0 # How many particles were in event 
	
    # Open the first file and read its content 
    # Format the headings for the data before display 
    print repr('Energy').ljust(7), repr('X-coord').ljust(7), repr('Y-coord').ljust(7), repr('Z-coord').ljust(7), repr('Charge').ljust(7) 
    
    print repr('++++++').ljust(7), repr('+++++++').ljust(7), repr('+++++++').ljust(7), repr('+++++++').ljust(7), repr('+++++++').ljust(7)
    
    with open(data_file, 'r' ) as file: 	
        for particle_details in file: # Read the data obtained line by line 
            values = particle_details.split() # The first item can tell us if we are looking at daughter particles or four momentum values
			
            if len( values ) == 1: # We expect single digit (1, 2 ... 9, 2 mostly) daughter particles from decays 
                daughter_particles = int(values[0]) # The first line represents the number of particles to expect in subsequent events
	   
            elif len( values ) > 1: 
                for n in range (0, daughter_particles): 
                    # Unpack the list. Get the four momentum data 
                    energy, px, py, pz, charge = float(values[0]), float(values[1]), float(values[2]), float(values[3]),  int(values[4]) 
                    # mass = invariant_mass( energy, px, py, pz ) 					
                    print repr(energy).rjust(8), repr(px).rjust(8), repr(py).rjust(8), repr(pz).rjust(8), repr(charge).rjust(8) 
                    break # Temporarily stop execution, force the program to go to the next loop iteration  
			
################################################################################
# Calculate the invariant mass according to the theory of special relativity
################################################################################
def invariant_mass(E, px, py, pz):
    # mass  = (E[0]+E[1])**2
    # mass -= (px[0]+px[1])**2
    # mass -= (py[0]+py[1])**2
    # mass -= (pz[0]+pz[1])**2  
    mass  = (E[0]+E[1])**2

    return np.sqrt(mass)
			
if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Calculate the invariant mass of parent particles after a decay into muons in a p-p collision.') 
    parser.add_argument('-f', '--file', type=str, nargs='+', help='The paths to the file(s) holding the input data.') 
	
    args = parser.parse_args() 
	
    determine_mass (args.file[0])
