#!/bin/bash
source ./set_environment

cd "$(dirname "$0")"

STRUC_DIR=$RASPA_DIR/share/raspa/structures/cif

raess $STRUC_DIR/$1.cif $RASPA_DIR/share/raspa/forcefield/UFF/force_field_mixing_rules.def 298.0 12.0 2000 Xe 0.85 1.6 >> /home/emmanuel/Documents/coudert_lab/raess_test/./cpp_output_2000_0.85_1.6.csv
