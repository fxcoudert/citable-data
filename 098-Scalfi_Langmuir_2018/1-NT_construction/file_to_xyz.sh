# Script to make a xyz file

n=$1

sed -i -e "s/XXXX/$n/g" form_slab.py
sed -i -e "s/XXXX/$n/g" flat_to_nt.py

touch atoms
for (( unit=0; unit<$n; unit++))
do
    cat atoms.dat >> atoms
done

((natoms=$n*28))

rm nanotube_${n}_HB1.xyz
touch nanotube_${n}_HB1.xyz
echo "$natoms
" >> nanotube_${n}_HB1.xyz

paste atoms nanotube_${n}_HB1 >> nanotube_${n}_HB1.xyz

rm atoms nanotube_${n}_HB1 slab_${n}_HB1
