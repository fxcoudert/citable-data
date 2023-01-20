#!/bin/bash
#export NODES=$(srun hostname | sort | uniq)
#echo "Running on nodes:"
#echo "${NODES}"

$MATSCREEN_PYTHON $MATSCREEN/screen.py -ppn 1 -n 1 -s $MATSCREEN/data/structures_sym.csv -v 20 -m xenon -g yes -N 100000 -t widom_nogrid
if [ -f "set_environment" ]; then
	rm set_environment
fi
bash $MATSCREEN/copy_env.sh set_environment

