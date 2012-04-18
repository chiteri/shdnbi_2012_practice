import argparse

def determine_mass(data_file): 
    # Open the first file and read its content 
    with open(data_file, 'r' ) as file: 	
        for particle_details in file: # Read the data obtained line by line 
            values = particle_details.split() # The first item can tell us if we are looking at daughter particles or four momentum values
			
            if len( values ) == 1: # We expect single digit (1, 2 ... 9, 2 mostly) daughter particles from decays 
                daughter_particles = int(values[0]) # The first line represents the number of particles to expect in subsequent events
	   
            elif len( values ) > 1: 
                # particle in range(1, daughter_particles): # Loop through the number of particles detected in the decay 
                energy, px, py, pz, charge = values[0], values[1], values[2], values[3],  values[4] # Unpack the list. Get the four momentum data 
                print energy, px, py, pz, charge 
                # mass = invariant_mass(energy, px, py, pz, charge)
			
################################################################################
# Calculate the invariant mass according to the theory of special relativity
################################################################################
def invariant_mass(E, px, py, pz):
    mass  = (E[0]+E[1])**2
    mass -= (px[0]+px[1])**2
    mass -= (py[0]+py[1])**2
    mass -= (pz[0]+pz[1])**2

    return np.sqrt(mass)
			
if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Calculate the invariant mass of parent particles after a decay into muons in a p-p collision.') 
    parser.add_argument('-f', '--file', type=str, nargs='+', help='The paths to the file(s) holding the input data.') 
	
    args = parser.parse_args() 
	
    determine_mass (args.file[0])