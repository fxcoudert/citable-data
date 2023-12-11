#!/bin/bash

source /usr/local/gromacs/bin/GMXRC

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
				 

	for i in {0..19}
	do
gmx energy -f ${filesPressure[i]}/prd.edr -o ${filesPressure[i]}/volume.xvg > ${filesPressure[i]}/volume.av << EOF
Volume
EOF
	done

	




