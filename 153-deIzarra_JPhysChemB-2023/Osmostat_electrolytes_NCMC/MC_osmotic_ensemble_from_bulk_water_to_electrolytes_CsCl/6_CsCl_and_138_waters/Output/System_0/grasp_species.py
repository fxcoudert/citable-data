#!/usr/bin/env python

import re
import csv

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

file_name.append("output_Box_1.1.1_300.000000_100000.data")

# Declare the number of file to read in.
number_file = len(file_name)

# Define the line to store line of the read files.
line = ''

# Declare where to read in the file, after the begin of the simulation.
ignore = True

#Declare ith cycle
MC_cycle = []

#Declare absolute and relative adsorption
water = []
salt = []

# Splited_line is used to split line in the file
splited_line = []
splited_line2 = []

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
					splited_line = line.split(" ")
					MC_cycle.append(splited_line[2])
				if line.startswith("Component 0 (Tip4p)"):
					splited_line = line.split(" ")
					splited_line_2 = splited_line[8].split("/")
					water.append(splited_line_2[0])
				if line.startswith("Component 1 (Cs)"):
					splited_line = line.split(" ")
					splited_line_2 = splited_line[8].split("/")
					salt.append(splited_line_2[0])

					
			
				####################################################
f.close()


# Prepare the csv file to output
filename = "species_evolution.txt"

# field names 
top_fields = ['MC_cycle \t H20 \t salt'] 

total_data = [MC_cycle, water, salt]

# writing to csv file 
with open(filename, 'w') as csvfile:
	
	# creating a csv writer object
	csvwriter = csv.writer(csvfile)
	
	# Write Header of the columns.
	csvwriter.writerow(top_fields)
	
	# Write the data, row by row.
	for row in range(0, len(MC_cycle)):
		csvwriter.writerow((MC_cycle[row], water[row], salt[row]))

csvfile.close()










'''

# Prepare the csv file to output
filename = "adsorption_pressure_MC_cycle.csv"

# field names 
top_fields = ['MC_cycle', 'absolute_adsorption_(H20)', 'excess_adsorption_(H20)', 'Pressure'] 

total_data = [MC_cycle, absolute_adsorption, excess_adsorption, average_pressure]

# writing to csv file 
with open(filename, 'w') as csvfile:
	
	# creating a csv writer object
	csvwriter = csv.writer(csvfile)
	
	# Write Header of the columns.
	csvwriter.writerow(top_fields)
	
	# Write the data, row by row.
	for row in range(0, len(MC_cycle)):
		csvwriter.writerow((MC_cycle[row], absolute_adsorption[row], excess_adsorption[row], average_pressure[row]))

csvfile.close()
'''



