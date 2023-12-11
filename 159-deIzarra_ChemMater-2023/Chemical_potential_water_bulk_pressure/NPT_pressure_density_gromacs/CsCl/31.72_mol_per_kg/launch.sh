#!/bin/bash

cd prepare_system
./prepare_system.sh
cd ..

cd minimization
./minimization.sh
cd ..

cd NVT
./NVT.sh
