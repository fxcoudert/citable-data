#!/usr/bin/gnuplot

	set border lw 1.0
 
 set datafile separator ","
 set ytics format "{/:{/=10 %h}}"
 set xtics format "{/:{/=10 %h}}"
 set key bottom reverse 

set yrange [0:8]
set xrange [0:200]
	
	f(x)=4
	
	set encoding iso_8859_1
	set xlabel "{/: {/=12 MC steps}}"
	set ylabel "{/: {/=12 Nombre de pairs d'ions}}"
	set title "Echantillonnage de 1M LiCL"
	plot "species_evolution.txt" using 1:2 every 1 w l lc rgb 'red' lw 3.0 notitle axis x1y1,\
		 "species_evolution.txt" using 1:3 every 1 w l lc rgb 'green' lw 3.0 title "LiCl salt pairs"				  axis x1y1,\
		 f(x) lc rgb 'black' lw 2.0 title "1M = 4 pairs à retrouver"				  axis x1y1,\
		 
	pause -1
