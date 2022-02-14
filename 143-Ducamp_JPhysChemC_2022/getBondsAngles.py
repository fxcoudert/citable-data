#!/opt/anaconda3/bin/python3

import pymatgen as pmg
from pymatgen.util.coord import pbc_diff, get_angle

def get_angle_between_closest_sites(structure,i,j,k):
    v1 = pbc_diff(structure[i].frac_coords, structure[j].frac_coords)
    v2 = pbc_diff(structure[k].frac_coords, structure[j].frac_coords)

    cart_v1 = structure.lattice.get_cartesian_coords(v1)
    cart_v2 = structure.lattice.get_cartesian_coords(v2)

    return get_angle(cart_v1, cart_v2, units="degrees")


# List of cif files name

with open("name_list", "r") as f:
    nameList = f.readline().split()

open("results", "w").close()



# Loop over each cif files

for name in nameList:
    structure = pmg.Structure.from_file("./"+name+".cif")
    
    # get sites
    Si_sites = []
    for index, site in enumerate(structure):
        if site.species_string == "Si":
            Si_sites.append(index)
    
    O_sites = []
    for index, site in enumerate(structure):
        if site.species_string == "O":
            O_sites.append(index)
    
    # get bond lengths
    SiO_bondlengths = []
    for index in Si_sites:
        neighbors = structure.get_neighbors(structure[index], 2.0)
        for neigh in neighbors:
            SiO_bondlengths.append(neigh.nn_distance)
    
    
    # angles calculation
    
    def get_angle_between_closest_sites(structure,i,j,k):
        v1 = pbc_diff(structure[i].frac_coords, structure[j].frac_coords)
        v2 = pbc_diff(structure[k].frac_coords, structure[j].frac_coords)
        
        cart_v1 = structure.lattice.get_cartesian_coords(v1)
        cart_v2 = structure.lattice.get_cartesian_coords(v2)
    
        return get_angle(cart_v1, cart_v2, units="degrees")
    
    OSiO_bondangles = []
    for index in O_sites:
        neighbors = structure.get_neighbors(structure[index], 2.0)
        OSiO_bondangles.append(get_angle_between_closest_sites(structure,neighbors[0].index,index,neighbors[-1].index))


    try:
    
    
    #Calculation of means, max, min and variance for angles
        SiOSi_mean = (sum(OSiO_bondangles)/len(OSiO_bondangles))
        totalg = 1
        totalh = 0
        for n in OSiO_bondangles:
            totalg = totalg * n
            totalh = totalh + (1/n)
        SiOSi_gmean = totalg**(1.0/len(OSiO_bondangles))
        SiOSi_hmean = len(OSiO_bondangles)/totalh
        SiOSi_max = max(OSiO_bondangles)
        SiOSi_min = min(OSiO_bondangles)
        SiOSi_var = (sum([x**2 for x in OSiO_bondangles])/len(OSiO_bondangles))-(SiOSi_mean**2)
    
        with open("results", "a") as f:
            f.write(str(name)+"\t"+str(SiOSi_mean)+"\t"+str(SiOSi_gmean)+"\t"+str(SiOSi_hmean)+"\t"+str(SiOSi_max)+"\t"+str(SiOSi_min)+"\t"+str(SiOSi_var)+"\t")
    
    #Calculation of means, max, min, and variance for bond lengths
        SiO_mean = sum(SiO_bondlengths)/len(SiO_bondlengths)
        totalg = 1
        totalh = 0
        for n in SiO_bondlengths:
            totalg = totalg * n
            totalh = totalh+ (1/n)
        SiO_gmean = totalg**(1.0/len(SiO_bondlengths))
        SiO_hmean = len(SiO_bondlengths)/totalh
        SiO_max = max(SiO_bondlengths)
        SiO_min = min(SiO_bondlengths)
        SiO_var = (sum([x**2 for x in SiO_bondlengths])/len(SiO_bondlengths))-(SiO_mean**2)
    
        with open("results", "a") as f:
            f.write(str(SiO_mean)+"\t"+str(SiO_gmean)+"\t"+str(SiO_hmean)+"\t"+str(SiO_max)+"\t"+str(SiO_min)+"\t"+str(SiO_var)+"\n")

    except Exception:
        with open("error.dat", "a") as err:
            err.write(name+"\n")
