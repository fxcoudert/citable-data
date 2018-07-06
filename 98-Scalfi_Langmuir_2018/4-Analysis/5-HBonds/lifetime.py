import numpy as np

water_in_range=range(1008,1302,3)
n_win = len(water_in_range)

water_out_range=range(1302,1356,3)
n_wout = len(water_out_range)

sioh_range=range(432,444)+range(516,528)+range(600,612)+range(684,696)+range(768,780)+range(852,864)
n_sioh = len(sioh_range)

aloh_range=range(480,516)+range(564,600)+range(648,684)+range(732,768)+range(816,852)+range(900,936)
n_aloh = len(aloh_range)

files=['_wi-wi.dat','_si-w.dat','_w-si.dat']

hbnet=[]

for name in files:
    print(name)
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
    hbnet.append(hb)

n_frame=len(hb)-1
A = np.zeros((n_win,n_frame))

for frame in range(n_frame):
    for ind,water in enumerate(water_in_range):

        #water donates to sioh
        net = filter(lambda u: u[1] == water, hbnet[1][frame+1])
        if (len(net)):
            A[ind,frame]=1

        #water accepts from sioh
        net = filter(lambda u: u[0] == water, hbnet[2][frame+1])
        if (len(net)):
            A[ind,frame]=1

print("Autocorrelation function")
out=open("lifetime_layer.dat",'w')
n = n_frame/2

C = np.zeros((n))
for dt in range(n):
    for time in range(n_frame-dt):
        #moyenne sur les molecules
        C[dt]+=np.sum(np.multiply(A[:,time],A[:,time+dt]))
    C[dt]/=(n_win*(n_frame-dt))
    if (dt==0):
        norm = C[0]
    if (norm):
        C[dt]/=norm
    out.write(str(dt)+'   '+str(C[dt])+'\n')

out.close()
