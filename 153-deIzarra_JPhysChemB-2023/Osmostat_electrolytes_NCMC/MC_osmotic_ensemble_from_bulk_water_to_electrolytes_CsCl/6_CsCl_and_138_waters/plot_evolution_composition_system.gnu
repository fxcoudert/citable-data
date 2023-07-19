#!/usr/bin/gnuplot

	set border lw 1.5
	set terminal wxt size 600,250

 set datafile separator ","
 set ytics format "{/:{/=11 %h}}"
 set xtics format "{/:{/=11 %h}}"
 set key left top 

set yrange [0:20]
set xrange [0:1000]
	
	set encoding iso_8859_1
	set xlabel "{/: {/=12 Number of MC cycles}}"
	set ylabel "{/: {/=12 CsCl Concentration (M)}"
	#set title  "Δµ vs concentration salt (monovalent, varying cation)" 
	plot "Output/System_0/species_evolution.txt" using 1:(($3/(6.02*10**23))/(1000*$2*18.01528*1.6605*10**(-30))) every 1 w l lc rgb '#01665e'  lw 3.0 notitle axis x1y1,\
		 
	pause -1

