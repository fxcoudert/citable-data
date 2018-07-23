import numpy as np
import sys

#water_range=range(1008,1356,3)
#n_w = len(water_range)

#sioh_range=range(432,444)+range(516,528)+range(600,612)+range(684,696)+range(768,780)+range(852,864)
#n_sioh = len(sioh_range)

#aloh_range=range(480,516)+range(564,600)+range(648,684)+range(732,768)+range(816,852)+range(900,936)
#n_aloh = len(aloh_range)

#files=['_w-w.dat','_si-si.dat','_al-al.dat','_si-w.dat','_w-si.dat','_al-w.dat','_w-al.dat']

if (len(sys.argv)==1):
    print("Error: invalid argument\n")
    quit()

name = str(sys.argv[1])
print(name)

print("Reading file")
with open('hbonds'+name,'r') as data:
    hb=[]
    hbf=[] 
    for line in data:
        if (not line.startswith('#')):
            line2=line.split()
            a=int(line2[1])
            d=int(line2[3])
            h=int(line2[5])
            #dist=float(line2[7])
            #angle=float(line2[8])
            #hbf.append((a,d,h,dist,angle))
            hbf.append((a,d,h))
        if line.startswith('# Frame'):
            hb.append(hbf)
            hbf=[]
    hb.append(hbf)
    number = map(len,hb)
    mean = float(sum(number))/(len(number)-1)
    print("mean number per frame: " + str(mean) + '\n')

print("Autocorrelation function")
print('\n'+name)
out = open('autocorr'+name,'w')

flattened = [val for sublist in hb for val in sublist]
network = set(flattened)
n_hb = len(network)

print('number of hb :')
print(n_hb)

n_frame = len(hb)-1
print('computing A')
# array hbonds*frame
A = np.zeros((n_hb,n_frame))

for ind,bond in enumerate(network):    
    for frame in range(n_frame):
        if (bond in hb[frame+1]):
            A[ind][frame]=1

n = n_frame/2
print('dt range:')
print(n)

C = np.zeros((n))
for dt in range(n):
    for time in range(n_frame-dt):
        #moyenne sur les HB
        C[dt]+=np.sum(np.multiply(A[:,time],A[:,time+dt]))
    if (n_hb):
        C[dt]/=(n_hb*(n_frame-dt))
    if (dt==0):
        norm = C[0]
    if (norm):
        C[dt]/=norm
    out.write(str(dt)+'   '+str(C[dt])+'\n')

