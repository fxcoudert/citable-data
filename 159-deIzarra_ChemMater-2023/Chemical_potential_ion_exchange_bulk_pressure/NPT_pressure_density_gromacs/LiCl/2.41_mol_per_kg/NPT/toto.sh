#!/bin/bash

source /usr/local/gromacs/bin/GMXRC


oldline="ref_p"


filesPressure=("0.006MPA"
			 "0.01MPA"
			 "0.05MPA"
			 "0.1MPA"
			 "0.3MPA"
			 "0.7MPA"
			 "1MPA"
			 "2MPA"
			 "5MPA"
			 "10MPA"
			 "40MPA"
			 "70MPA"
			 "100MPA"
			 "200MPA"
			 "300MPA"
			 "400MPA"
			 "500MPA"
			 "600MPA"
			 "800MPA"
			 "1000MPA")	
			 
			 
	Pressure=("0.06"
				"0.1"
				"0.5"
				"1"
				"3"
				"7"
				"10"
				"20"
				"50"
				"100"
				"400"
				"700"
				"1000"
				"2000"
				"3000"
				"4000"
				"5000"
				"6000"
				"8000"
				"10000")				 
	 	
				 

	for i in {0..19}
	do
	scp eql2.mdp ${filesPressure[i]}
	scp  prd.mdp ${filesPressure[i]}
	done

	for i in {0..19}
	do
	 cd ${filesPressure[i]}
	 newline="ref_p 					 = "${Pressure[i]}
	 sed -i "s/$oldline.*/$newline/" eql2.mdp
	 sed -i "s/$oldline.*/$newline/" prd.mdp
	 cd ..
	done




