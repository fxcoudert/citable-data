#############################################################"
# Circular density profile on flattened nanotubes

a=20.4205
c=8.486

for element in Si Oint Hint Ow Hw
do
    cfiles density nt12-24-full.trj_wrap_flat.xyz -c $a:50:$c --axis=X --axis=Z --max=20.5:12.8 --min=-20.5:-12.8 --points=1000 --selection="atoms: name $element and y < 2.5 and y > -4" -o density_flat_${element}.dat &
done

