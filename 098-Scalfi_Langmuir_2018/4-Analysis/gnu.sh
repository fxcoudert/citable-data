gnuplot -p -e "
    set view map;
    set size square;
    set xrange [-15:15];
    set yrange [0:15];
    set cbrange [0:0.05];
    set palette defined ( 0 'white', 1 'blue', 2 'red', 3 'orange' );
    splot '$1' u 1:2:3 with image;
"
