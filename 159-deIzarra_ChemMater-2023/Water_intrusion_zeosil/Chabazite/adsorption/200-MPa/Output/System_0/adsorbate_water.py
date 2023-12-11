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

file_name.append("output_ZIF-8_Ambroise_2.2.2_300.000000_500000.data")

# Declare the number of file to read in.
number_file = len(file_name)

# Define the line to store line of the read files.
line = ''

# Declare where to read in the file, after the begin of the simulation.
ignore = True

#Declare ith cycle
MC_cycle = []

#Declare absolute and relative adsorption
absolute_adsorption = []
excess_adsorption = []

#Declare average pressure
average_pressure = []

# Splited_line is used to split line in the file
splited_line = []

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
				if line.startswith("[Equilibration] Current cycle:"):
					splited_line = line.split(" ")
					MC_cycle.append(splited_line[3])
				if line.startswith("Current cycle:"):
					#print(splited_line)
					splited_line = line.split(" ")
					MC_cycle.append(float(splited_line[2]) + 400000)
	
				# Extract absolute adsorption of water in Silicalite at a step
				if line.startswith("	absolute adsorption:"):
					splited_line = line.split(" ")
					
					for j in range(0, len(splited_line)):
						if splited_line[j] == "[mol/uc],":
							#print (splited_line[j])
								
							for k in range(0,j):
								if check_float(splited_line[k]) == True:
									absolute_adsorption.append(splited_line[k])
					
				# Extract absolute adsorption of water in Silicalite at a step
				if line.startswith("	excess adsorption:"):
					splited_line = line.split(" ")
					
					for j in range(0, len(splited_line)):
						if splited_line[j] == "[mol/uc],":
							#print (splited_line[j])
								
							for k in range(0,j):
								if check_float(splited_line[k]) == True:
									excess_adsorption.append(splited_line[k])
					
				# Extract Pressure at a step 
				#if line.startswith("Average pressure:"):
				#	splited_line = line.split(" ")

				#	for j in range(0, len(splited_line)):
				#		if splited_line[j] == "[kPa]":
				#			average_pressure.append(splited_line[j-1])
				
				####################################################
f.close()

# Prepare the csv file to output
filename = "adsorption_pressure_MC_cycle.csv"

# field names 
top_fields = ['MC_cycle', 'absolute_adsorption_(H20)', 'excess_adsorption_(H20)'] 

total_data = [MC_cycle, absolute_adsorption, excess_adsorption]

# writing to csv file 
with open(filename, 'w') as csvfile:
	
	# creating a csv writer object
	csvwriter = csv.writer(csvfile)
	
	# Write Header of the columns.
	csvwriter.writerow(top_fields)
	
	# Write the data, row by row.
	for row in range(0, len(MC_cycle)):
		csvwriter.writerow((MC_cycle[row], absolute_adsorption[row], excess_adsorption[row]))

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



