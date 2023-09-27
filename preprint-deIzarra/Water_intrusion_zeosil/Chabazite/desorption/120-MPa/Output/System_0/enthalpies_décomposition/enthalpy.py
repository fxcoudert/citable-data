#!/usr/bin/env python

import re
import csv
import math

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

file_name.append("../output_CHA_SI_3.2.2_300.000000_1.2e+08.data")

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

#Declare energy terms
total_energy = []
host_adsorbate_energy = []
adsorbate_adsorbate_energy = []
tail_energy = []

# Splited_line is used to split line in the file
splited_line = []
splited_line_2 = []

# read in the files with a loop
for i in range(0, len(file_name)):
	with open(file_name[i], 'r') as f:
		for line in f:
			line = line.rstrip()
			
			if line.startswith("Current cycle: 0"):
				ignore = False
			
			if not ignore:
				##### Doing the analysis here and gather data #####
				# Extract current cycle

				if line.startswith("Current cycle:"):
					#print(splited_line)
					splited_line = line.split(" ")
					MC_cycle.append(float(splited_line[2]))
	
				# Extract absolute adsorption of water in Silicalite at a step
				if line.startswith("Component 0 (Tip4p)"):
					splited_line = line.split(" ")
					splited_line_2 = splited_line[8].split("/")
					if check_float(splited_line_2[0]) == True:
									absolute_adsorption.append(float(splited_line_2[0]))
									
			    # Extract different energies through MC cycles.
			    
			    # Extract total energy
				if line.startswith("Current total potential energy:"):
					splited_line = line.split(" ")
					for j in range(0, len(splited_line)):
						if splited_line[j] == "[K]":
							total_energy.append(float(splited_line[j-1]))	
					
							
				# Extract host-adsorbate energy		
				if line.startswith("\tCurrent Host-Adsorbate energy:"):
					splited_line = line.split(" ")
					for j in range(0, len(splited_line)):
						if splited_line[j] == "[K]":
							host_adsorbate_energy.append(float(splited_line[j-1]))	
							
				# Extract adsorbate-adsorbate energy		
				if line.startswith("\tCurrent Adsorbate-Adsorbate energy:"):
					splited_line = line.split(" ")
					for j in range(0, len(splited_line)):
						if splited_line[j] == "[K]":
							adsorbate_adsorbate_energy.append(float(splited_line[j-1]))	
							
								
f.close()

#Extract tail energy correction
for i in range(0, len(MC_cycle)):
	tail_energy.append(total_energy[i]-host_adsorbate_energy[i]-adsorbate_adsorbate_energy[i])

for i in range(0, len(MC_cycle)):
	total_energy[i] = (total_energy[i]-tail_energy[i])

########################################################
# Variable to calculate enthalpy for each energy term. #
########################################################

av_N=0
av_N_square=0

av_total_energy=0
av_host_adsorbate_energy=0
av_adsorbate_adsorbate_energy=0
av_tail_energy=0

av_N_times_total_energy=0
av_N_times_host_adsorbate_energy=0
av_N_times_adsorbate_adsorbate_energy=0
av_N_times_tail_energy=0

for i in range(0, len(MC_cycle)):
	av_N += absolute_adsorption[i]
	av_N_square += absolute_adsorption[i]*absolute_adsorption[i]
	
	av_total_energy += total_energy[i]
	av_host_adsorbate_energy += host_adsorbate_energy[i]
	av_adsorbate_adsorbate_energy += adsorbate_adsorbate_energy[i]
	av_tail_energy += tail_energy[i]
    
	av_N_times_total_energy +=  absolute_adsorption[i]*total_energy[i]
	av_N_times_host_adsorbate_energy +=  absolute_adsorption[i]*host_adsorbate_energy[i]
	av_N_times_adsorbate_adsorbate_energy +=  absolute_adsorption[i]*adsorbate_adsorbate_energy[i]
	av_N_times_tail_energy +=  absolute_adsorption[i]*tail_energy[i]
    

av_N /= len(MC_cycle)
av_N_square /= len(MC_cycle)

av_total_energy /= len(MC_cycle)
av_host_adsorbate_energy /= len(MC_cycle)
av_adsorbate_adsorbate_energy /= len(MC_cycle)
av_tail_energy /= len(MC_cycle)

av_N_times_total_energy /= len(MC_cycle)
av_N_times_host_adsorbate_energy /= len(MC_cycle)
av_N_times_adsorbate_adsorbate_energy /= len(MC_cycle)
av_N_times_tail_energy /= len(MC_cycle)


##########################################################
# calculate error over 10 blocks on each enthalpy terms. #
##########################################################

av_N_buffer = 0
av_N_square_buffer = 0

av_total_energy_buffer = 0
av_host_adsorbate_energy_buffer = 0
av_adsorbate_adsorbate_energy_buffer = 0
av_tail_energy_buffer = 0

av_N_times_total_energy_buffer = 0
av_N_times_host_adsorbate_energy_buffer = 0
av_N_times_adsorbate_adsorbate_energy_buffer = 0
av_N_times_tail_energy_buffer = 0



av_N_blocks = []
av_N_square_blocks = []

av_total_energy_blocks = []
av_host_adsorbate_energy_blocks = []
av_adsorbate_adsorbate_energy_blocks = []
av_tail_energy_blocks = []

av_N_times_total_energy_blocks= []
av_N_times_host_adsorbate_energy_blocks= []
av_N_times_adsorbate_adsorbate_energy_blocks= []
av_N_times_tail_energy_blocks= []

blocks = len(MC_cycle)/5

for i in range(0, 5):
	av_N_buffer = 0
	av_N_square_buffer = 0
	
	av_total_energy_buffer = 0
	av_host_adsorbate_energy_buffer = 0
	av_adsorbate_adsorbate_energy_buffer = 0
	av_tail_energy_buffer = 0
	
	av_N_times_total_energy_buffer = 0
	av_N_times_host_adsorbate_energy_buffer = 0
	av_N_times_adsorbate_adsorbate_energy_buffer = 0
	av_N_times_tail_energy_buffer = 0
	
	for j in range(0, blocks):
		av_N_buffer += absolute_adsorption[i*blocks+j]
		av_N_square_buffer += absolute_adsorption[i*blocks+j]*absolute_adsorption[i*blocks+j]
	
		av_total_energy_buffer +=  total_energy[i*blocks+j]
		av_host_adsorbate_energy_buffer +=  host_adsorbate_energy[i*blocks+j]
		av_adsorbate_adsorbate_energy_buffer +=  adsorbate_adsorbate_energy[i*blocks+j]
		av_tail_energy_buffer +=  tail_energy[i*blocks+j]
    
		av_N_times_total_energy_buffer += absolute_adsorption[i*blocks+j]*total_energy[i*blocks+j]
		av_N_times_host_adsorbate_energy_buffer += absolute_adsorption[i*blocks+j]*host_adsorbate_energy[i*blocks+j]
		av_N_times_adsorbate_adsorbate_energy_buffer += absolute_adsorption[i*blocks+j]*adsorbate_adsorbate_energy[i*blocks+j]
		av_N_times_tail_energy_buffer += absolute_adsorption[i*blocks+j]*tail_energy[i*blocks+j]

	av_N_blocks.append(av_N_buffer/blocks)
	av_N_square_blocks.append(av_N_square_buffer/blocks)
	
	av_total_energy_blocks.append(av_total_energy_buffer/blocks)
	av_host_adsorbate_energy_blocks.append(av_host_adsorbate_energy_buffer/blocks)
	av_adsorbate_adsorbate_energy_blocks.append(av_adsorbate_adsorbate_energy_buffer/blocks)
	av_tail_energy_blocks.append(av_tail_energy_buffer/blocks)
	
	av_N_times_total_energy_blocks.append(av_N_times_total_energy_buffer/blocks)
	av_N_times_host_adsorbate_energy_blocks.append(av_N_times_host_adsorbate_energy_buffer/blocks)
	av_N_times_adsorbate_adsorbate_energy_blocks.append(av_N_times_adsorbate_adsorbate_energy_buffer/blocks)
	av_N_times_tail_energy_blocks.append(av_N_times_tail_energy_buffer/blocks)
	
enthalpy_total_energy_blocks = []
enthalpy_host_adsorbate_energy_blocks = []
enthalpy_adsorbate_adsorbate_energy_blocks = []
enthalpy_tail_energy_blocks = []

enthalpy_total_energy_av = (av_N_times_total_energy-av_N*av_total_energy)/(av_N_square-av_N*av_N)
enthalpy_host_adsorbate_energy_av = (av_N_times_host_adsorbate_energy-av_N*av_host_adsorbate_energy)/(av_N_square-av_N*av_N)
enthalpy_adsorbate_adsorbate_energy_av = (av_N_times_adsorbate_adsorbate_energy-av_N*av_adsorbate_adsorbate_energy)/(av_N_square-av_N*av_N)
enthalpy_tail_energy_av = (av_N_times_tail_energy-av_N*av_tail_energy)/(av_N_square-av_N*av_N)

for i in range(0, 5):
	enthalpy_total_energy_blocks.append((av_N_times_total_energy_blocks[i]-av_N_blocks[i]*av_total_energy_blocks[i])/(av_N_square_blocks[i]-av_N_blocks[i]*av_N_blocks[i]))
	enthalpy_host_adsorbate_energy_blocks.append((av_N_times_host_adsorbate_energy_blocks[i]-av_N_blocks[i]*av_host_adsorbate_energy_blocks[i])/(av_N_square_blocks[i]-av_N_blocks[i]*av_N_blocks[i]))
	enthalpy_adsorbate_adsorbate_energy_blocks.append((av_N_times_adsorbate_adsorbate_energy_blocks[i]-av_N_blocks[i]*av_adsorbate_adsorbate_energy_blocks[i])/(av_N_square_blocks[i]-av_N_blocks[i]*av_N_blocks[i]))
	enthalpy_tail_energy_blocks.append((av_N_times_tail_energy_blocks[i]-av_N_blocks[i]*av_tail_energy_blocks[i])/(av_N_square_blocks[i]-av_N_blocks[i]*av_N_blocks[i]))

	
error_N = 0
error_enthalpy_total_energy = 0
error_enthalpy_host_adsorbate_energy = 0
error_enthalpy_adsorbate_adsorbate_energy = 0
error_enthalpy_tail_energy = 0


for i in range(0, 5):
	error_N += pow(av_N - av_N_blocks[i],2)
	error_enthalpy_total_energy += pow(enthalpy_total_energy_av - enthalpy_total_energy_blocks[i],2)
	error_enthalpy_host_adsorbate_energy += pow(enthalpy_host_adsorbate_energy_av - enthalpy_host_adsorbate_energy_blocks[i],2)
	error_enthalpy_adsorbate_adsorbate_energy += pow(enthalpy_adsorbate_adsorbate_energy_av - enthalpy_adsorbate_adsorbate_energy_blocks[i],2)		
	error_enthalpy_tail_energy += pow(enthalpy_tail_energy_av - enthalpy_tail_energy_blocks[i],2)		

error_N = math.sqrt((1/5.0)*(error_N))
error_enthalpy_total_energy = math.sqrt((1/5.0)*(error_enthalpy_total_energy))
error_enthalpy_host_adsorbate_energy = math.sqrt((1/5.0)*(error_enthalpy_host_adsorbate_energy))
error_enthalpy_adsorbate_adsorbate_energy = math.sqrt((1/5.0)*(error_enthalpy_adsorbate_adsorbate_energy))
error_enthalpy_tail_energy = math.sqrt((1/5.0)*(error_enthalpy_tail_energy))


filename = "enthalpy_contribution.txt"

with open(filename, 'w') as f:
	
	f.write('N_adsorbate per cell: ')
	f.write('%f' %(av_N/12))
	f.write(' +/- ')
	f.write('%f\n' %(error_N/12))
	f.write('enthalpy total (host_host + host_adsorbate + adsorbate_adsorbate) is (<N*Ut>-<N>*<Ut>)/(<N^2>-<N>^2) - K*T : ')
	
	f.write('%f' %(((av_N_times_total_energy-av_N*av_total_energy)/(av_N_square-av_N*av_N)-300)*8.314462618/1000))
	f.write(' +/- ')
	f.write('%f' %((error_enthalpy_total_energy)*8.314462618/1000))
	f.write('\tkJ/mol\n')
	
	f.write('enthalpy host_adsorbate_energy is (<N*Uha>-<N>*<Uha>)/(<N^2>-<N>^2) : ')
	f.write('%f' %(((av_N_times_host_adsorbate_energy-av_N*av_host_adsorbate_energy)/(av_N_square-av_N*av_N))*8.314462618/1000))
	f.write(' +/- ')
	f.write('%f' %((error_enthalpy_host_adsorbate_energy)*8.314462618/1000))
	f.write('\tkJ/mol\n')
	
	f.write('enthalpy adsorbate_adsorbate_energy is (<N*Uaa>-<N>*<Uaa>)/(<N^2>-<N>^2) : ')
	f.write('%f' %(((av_N_times_adsorbate_adsorbate_energy-av_N*av_adsorbate_adsorbate_energy)/(av_N_square-av_N*av_N))*8.314462618/1000))
	f.write(' +/- ')
	f.write('%f' %((error_enthalpy_adsorbate_adsorbate_energy)*8.314462618/1000))
	f.write('\tkJ/mol\n')
	
	f.write('enthalpy tail_energy is (<N*Utail>-<N>*<Utail>)/(<N^2>-<N>^2) : ')
	f.write('%f' %(((av_N_times_tail_energy-av_N*av_tail_energy)/(av_N_square-av_N*av_N))*8.314462618/1000))
	f.write(' +/- ')
	f.write('%f' %((error_enthalpy_tail_energy)*8.314462618/1000))
	f.write('\tkJ/mol\n')
	f.write('#######################################################################\n')
	
	f.write('#MC_cycle \t absolute_adsorption (#mol. total) \t absolute_adsorption (#mol. total/cell \t total energy (kJ/mol) \t host_adsorbate_energy (kJ/mol) \t host_adsorbate_adsorbate_energy (kJ/mol) \t tail_energy (kJ/mol)\n')
	
	
	for i in range(0, len(MC_cycle)):
		f.write('%f' %(MC_cycle[i]))
		if MC_cycle[i] < 10:
			f.write('\t\t\t')
		if MC_cycle[i] >= 10 and MC_cycle[i] < 100 :
			f.write('\t\t\t')
		if MC_cycle[i]>=100 and MC_cycle[i]<1000:
			f.write('\t\t\t')
		f.write('%.3f' %(absolute_adsorption[i]))
		f.write('\t\t\t')
		f.write('%.8f' %(total_energy[i]*8.314462618/1000))
		f.write('\t\t\t')
		f.write('%.8f' %(host_adsorbate_energy[i]*8.314462618/1000))
		f.write('\t\t\t')
		f.write('%.8f' %(adsorbate_adsorbate_energy[i]*8.314462618/1000))
		f.write('\t\t\t')
		f.write('%.8f' %(tail_energy[i]*8.314462618/1000))
		f.write('\n')
		
f.close()
    
