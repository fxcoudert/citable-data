from chemfiles import Trajectory, UnitCell, Atom, Topology, Frame, Selection

name = "nt12.opt"
a = 24.2

# Read the frame
frame = Trajectory(name+".xyz").read()

# Set the topology
topo = Trajectory("topology.pdb").read()
frame.set_topology(topo.topology())

# Get the positions
positions = frame.positions()

# Set the cell
cell = UnitCell(a, a, 42.43, 90, 90, 120)
frame.set_cell(cell)

# Select all except hydroxyl groups
#selection = Selection("atoms: name Al or name Obr or name Si")
selection = Selection("atoms: name Hext or name Oext or name Al or name Obr or name Si")
framework = selection.evaluate(frame)

with open(name+".cris",'w') as cris:
    with open(name+".slice.xyz",'w') as slic:
        with open(name+".framework.xyz",'w') as out:
            cris.write(" .false.\n")
            cris.write('{} {} 8.486 90.0 90.0 120.0\n'.format(a, a))
            cris.write('{}\n'.format(len(framework)/5))
 
            slic.write('{}\n\n'.format(len(framework)/5))
            out.write('{}\n\n'.format(len(framework)))
            for (ind,i) in enumerate(framework):
                atom = frame.atom(i)
                if atom.name() == "Al":
                    atom.set_charge(1.5750)
                    num = 1
                if atom.name() == "Obr":
                    atom.set_charge(-1.0500)
                    num = 2
                if atom.name() == "Oext":
                    atom.set_charge(-0.9500)
                    num = 3
                if atom.name() == "Hext":
                    atom.set_charge(0.4250)
                    num = 4
                if atom.name() == "Si":
                    atom.set_charge(2.1000)
                    num = 5
                out.write('{}\t'.format(atom.name()))
                out.write('{:8.5f}\t'.format(positions[i][0]))
                out.write('{:8.5f}\t'.format(positions[i][1]))
                out.write('{:8.5f}\n'.format(positions[i][2]))
 
                if (ind%5 == 0):
                    cris.write('{:d}\t'.format(num))
                    cris.write('{:8.5f}\t'.format(positions[i][0]))
                    cris.write('{:8.5f}\t'.format(positions[i][1]))
                    cris.write('{:8.5f}\t'.format(positions[i][2]))
                    cris.write('{:5.4f}\t'.format(atom.charge()))
                    cris.write('{}\n'.format(atom.name()))
 
                    slic.write('{}\t'.format(atom.name()))
                    slic.write('{:8.5f}\t'.format(positions[i][0]))
                    slic.write('{:8.5f}\t'.format(positions[i][1]))
                    slic.write('{:8.5f}\n'.format(positions[i][2]))


# Select all
selection = Selection("all")
nt = selection.evaluate(frame)
for i in nt:
    positions[i][0] += a/4
    positions[i][1] += a*0.4330127019
    positions[i][2] += 21.215

with Trajectory(name+".gibbs.xyz",'w') as gibbs:
    gibbs.write(frame)
 
# Select SiOH groups
selection = Selection("angles: name(#1) Si and name(#2) Oint and name(#3) Hint")
sioh_groups = selection.evaluate(frame)

print("{} SiOH groups found".format(len(sioh_groups)))

with open("sioh.coord",'w') as sioh_file:
    sioh_file.write('{}\n'.format(len(sioh_groups)))
    for (si, o, h) in sioh_groups:
        sioh_file.write('{:8.5f}\t{:8.5f}\t{:8.5f}\n'.format(positions[si][0], positions[si][1], positions[si][2]))
        sioh_file.write('{:8.5f}\t{:8.5f}\t{:8.5f}\n'.format(positions[o][0], positions[o][1], positions[o][2]))
        sioh_file.write('{:8.5f}\t{:8.5f}\t{:8.5f}\n'.format(positions[h][0], positions[h][1], positions[h][2]))
        #sioh_file.write('{:8.5f}\t{:8.5f}\t{:8.5f}\n'.format(positions[si][0], positions[si][1], positions[si][2]))
        sioh_file.write('{:8.5f}\t{:8.5f}\t{:8.5f}\n'.format(positions[o][0], positions[o][1], positions[o][2]))
        sioh_file.write('{:8.5f}\t{:8.5f}\t{:8.5f}\n'.format(positions[h][0], positions[h][1], positions[h][2]))
    sioh_file.write("END\n")        

with open(name+".sioh.xyz",'w') as sioh_file:
    sioh_file.write('{}\n\n'.format(3*len(sioh_groups)))
    for (si, o, h) in sioh_groups:
        sioh_file.write('{}\t{:8.5f}\t{:8.5f}\t{:8.5f}\n'.format(frame.atom(si).type(), positions[si][0], positions[si][1], positions[si][2]))
        sioh_file.write('{}\t{:8.5f}\t{:8.5f}\t{:8.5f}\n'.format(frame.atom(o).type(), positions[o][0], positions[o][1], positions[o][2]))
        sioh_file.write('{}\t{:8.5f}\t{:8.5f}\t{:8.5f}\n'.format(frame.atom(h).type(), positions[h][0], positions[h][1], positions[h][2]))


# Select Al2OH groups
selection = Selection("angles: name(#1) Al and name(#2) Oext and name(#3) Hext")
aloh_groups = selection.evaluate(frame)
selection = Selection("atoms: name Hext")
hext = selection.evaluate(frame)

print("{} AlOH groups found".format(len(aloh_groups)))

with open("aloh.coord",'w') as aloh_file:
    aloh_file.write('{:d}\n'.format(len(aloh_groups)/2))
    for h in hext:
        groups = filter(lambda u: u[2] == h, aloh_groups)
        assert(len(groups) == 2)
        assert(groups[0][1] == groups[1][1])
        al1 = groups[0][0]
        al2 = groups[1][0]
        o = groups[0][1]

        aloh_file.write('{:8.5f}\t{:8.5f}\t{:8.5f}\n'.format(positions[al1][0], positions[al1][1], positions[al1][2]))
        aloh_file.write('{:8.5f}\t{:8.5f}\t{:8.5f}\n'.format(positions[o][0], positions[o][1], positions[o][2]))
        aloh_file.write('{:8.5f}\t{:8.5f}\t{:8.5f}\n'.format(positions[al2][0], positions[al2][1], positions[al2][2]))
        aloh_file.write('{:8.5f}\t{:8.5f}\t{:8.5f}\n'.format(positions[h][0], positions[h][1], positions[h][2]))
        aloh_file.write('{:8.5f}\t{:8.5f}\t{:8.5f}\n'.format(positions[o][0], positions[o][1], positions[o][2]))
        aloh_file.write('{:8.5f}\t{:8.5f}\t{:8.5f}\n'.format(positions[h][0], positions[h][1], positions[h][2]))
    aloh_file.write("END\n")

with open(name+".aloh.xyz",'w') as aloh_file:
    aloh_file.write('{:d}\n\n'.format(4*len(aloh_groups)/2))
    for h in hext:
        groups = filter(lambda u: u[2] == h, aloh_groups)
        assert(len(groups) == 2)
        assert(groups[0][1] == groups[1][1])
        al1 = groups[0][0]
        al2 = groups[1][0]
        o = groups[0][1]

        aloh_file.write('{}\t{:8.5f}\t{:8.5f}\t{:8.5f}\n'.format(frame.atom(al1).type(), positions[al1][0], positions[al1][1], positions[al1][2]))
        aloh_file.write('{}\t{:8.5f}\t{:8.5f}\t{:8.5f}\n'.format(frame.atom(o).type(), positions[o][0], positions[o][1], positions[o][2]))
        aloh_file.write('{}\t{:8.5f}\t{:8.5f}\t{:8.5f}\n'.format(frame.atom(al2).type(), positions[al2][0], positions[al2][1], positions[al2][2]))
        aloh_file.write('{}\t{:8.5f}\t{:8.5f}\t{:8.5f}\n'.format(frame.atom(h).type(), positions[h][0], positions[h][1], positions[h][2]))
