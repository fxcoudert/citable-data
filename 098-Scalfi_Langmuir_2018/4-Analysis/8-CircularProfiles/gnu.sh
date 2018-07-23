set view map
set size ratio -1
set palette defined ( 0 'white', 1 'blue', 2 'red', 3 'yellow' );
max(a,b)=(a>b)?a:b;
splot 'density_flat_Ow.dat' u 1:2:3 with image
set xrange [-12:12]
set yrange [-5:5]
set ylabel 'Projection on Z axis'
set xlabel 'Circular coordinate'
set ytics 4.25

set term pngcairo size 2970,1700 font 'Helvetica,60'
set output 'density_flat_Si.png'
splot 'density_flat_Si.dat' u 1:2:3 with image notitle

set term pngcairo size 2970,1700 font 'Helvetica,60'
set output 'density_flat_Oint.png'
splot 'density_flat_Oint.dat' u 1:2:3 with image notitle

set term pngcairo size 2970,1700 font 'Helvetica,60'
set output 'density_flat_Hint.png'
splot 'density_flat_Hint.dat' u 1:2:3 with image notitle

set term pngcairo size 2970,1700 font 'Helvetica,60'
set output 'density_flat_Ow.png'
splot 'density_flat_Ow.dat' u 1:2:3 with image notitle

set term pngcairo size 2970,1700 font 'Helvetica,60'
set output 'density_flat_Hw.png'
splot 'density_flat_Hw.dat' u 1:2:3 with image notitle

set cbrange [0:0.01]
set term pngcairo size 2970,1700 font 'Helvetica,60'
set output 'density_flat.png'
splot '<paste density_flat_Oint.dat density_flat_Ow.dat' u 1:2:(max($3,$6)) with image notitle

set cbrange [0:0.01]
set term pngcairo size 2970,1700 font 'Helvetica,60'
set output 'density_flat_hw.png'
splot '<paste density_flat_Oint.dat density_flat_Hw.dat' u 1:2:(max($3,$6)) with image notitle

set cbrange [0:0.01]
set term pngcairo size 2970,1700 font 'Helvetica,60'
set output 'density_flat_hint.png'
splot '<paste density_flat_Oint.dat density_flat_Hint.dat' u 1:2:(max($3,$6)) with image notitle
