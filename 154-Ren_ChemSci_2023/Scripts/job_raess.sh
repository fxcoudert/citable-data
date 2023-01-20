#!/bin/bash
start=$SECONDS
#export NODES=$(srun hostname | sort | uniq)
#echo "Running on nodes:"
#echo "${NODES}"

python3 $MATSCREEN/screen.py -ppn 1 -n 1 -s $MATSCREEN/data/structures_sym.csv -v 20 -m xenon -t raess -f UFF -g yes -N 2000 -rj 0.85 -r 1.6 -o .
if [ -f "set_environment" ]; then
        rm set_environment
fi
bash $MATSCREEN/copy_env.sh set_environment
echo $(( SECONDS - start ))
