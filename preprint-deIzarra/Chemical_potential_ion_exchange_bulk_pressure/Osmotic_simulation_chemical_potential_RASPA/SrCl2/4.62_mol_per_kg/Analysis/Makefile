CFLAGS	=	-O3 -O2

SHELL := /bin/bash

exe: main.o 
		g++ main.o -o exe

main.o: main.cpp
		g++ -c main.cpp 

clean: 
	rm -rf *.o exe
