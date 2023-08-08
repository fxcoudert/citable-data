rm ZIF4-RESTART.wfn

lead='   &SUBSYS'
tail='    &COORD'
output=$(sed -e "/$lead/,/$tail/{ /$lead/{p; r new_cell
        }; /$tail/p; d }"  ZIF4_300.inp)
echo "$output" > ZIF4_300.inp