#!/usr/bin/env python

import re
import csv
import string
#####################################################################################

# Function to test of a string is a float.
def check_float(potential_float):

    try:

        float(potential_float)

        return True

    except ValueError:

        return False

#####################################################################################

# Declare the pressure in MPa corresponding to the file.
file_name = []

file_name.append("CHA_SI_defect_0.25_per_cell_not_equilibrated_1.1.1_300.000000_0.data")

# Declare the number of file to read in.
number_file = len(file_name)

# Define the line to store line of the read files.
line = ''

# Declare where to read in the file, after the begin of the simulation.
ignore = True

#Declare ith cycle
MC_cycle = []

# Splited_line is used to split line in the file
splited_line = []

Potential_Energy = []

# read in the files with a loop
for i in range(0, len(file_name)):
	with open(file_name[i], 'r') as f:
		for line in f:
			line = line.rstrip()
			
			if line.startswith("Starting simulation"):
				ignore = False
			
			if not ignore:
				##### Doing the analysis here and gather data #####
				# Extract current cycle
				if line.startswith("Current cycle:"):
					#print(splited_line)
					splited_line = line.split(" ")
					MC_cycle.append(float(splited_line[2]))				
							
				# Extract potential energy
				if line.startswith("Current total potential energy:"):
					splited_line = line.split(" ")
					splited_line=list(filter(None, splited_line))
					Potential_Energy.append(0.008314*float(splited_line[4]))
								
				####################################################
f.close()
print(len(MC_cycle))
# Write the data, row by row.

# Prepare the csv file to output
filename = "energy.txt"

# field names 
top_fields = ['MC_cycle', 'Potentiel_energy (kJ/mol)'] 

total_data = [MC_cycle, Potential_Energy]

# writing to csv file 
with open(filename, 'w') as csvfile:
	
	# creating a csv writer object
	csvwriter = csv.writer(csvfile)
	
	# Write Header of the columns.
	csvwriter.writerow(top_fields)
	
	# Write the data, row by row.
	for row in range(0, len(MC_cycle)):
		csvwriter.writerow((MC_cycle[row], Potential_Energy[row]))

csvfile.close()




