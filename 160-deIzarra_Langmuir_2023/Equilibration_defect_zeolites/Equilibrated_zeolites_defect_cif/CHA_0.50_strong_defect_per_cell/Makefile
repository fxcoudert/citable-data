CFLAGS	=	-O3 -O2

SHELL := /bin/bash

exe: main.o 
		g++ main.o -o exe -I /home/clement/Documents/programmes/chemfiles/build/prefix/include -lchemfiles -L /home/clement/Documents/programmes/chemfiles/build/prefix/lib

main.o: main.cpp
		g++ -c main.cpp -I /home/clement/Documents/programmes/chemfiles/build/prefix/include -lchemfiles -L /home/clement/Documents/programmes/chemfiles/build/prefix/lib

clean: 
	rm -rf *.o exe
