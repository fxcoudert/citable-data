import numpy as np

water_in_range=range(1008,1302,3)
n_win = len(water_in_range)
print("n_win "+str(n_win)+'\n')

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

nsteps=len(hb)-1
water_network=np.zeros((n_win,4))
# to SiOH, from SiOH, to W, from W
A = np.zeros((4,4,4,4))

for frame in range(nsteps):
    for ind,water in enumerate(water_in_range):

        #water donates to sioh
        net = filter(lambda u: u[1] == water, hbnet[1][frame+1])
        water_network[ind,0]=len(net)
        if (water_network[ind,0]>3):
            water_network[ind,0]=3

        #water accepts from sioh
        net = filter(lambda u: u[0] == water, hbnet[2][frame+1])
        water_network[ind,1]=len(net)
        if (water_network[ind,1]>3):
            water_network[ind,1]=3

        #water donates to water
        net = filter(lambda u: u[1] == water, hbnet[0][frame+1])
        water_network[ind,2]=len(net)
        if (water_network[ind,2]>3):
            water_network[ind,2]=3

        #water accepts from water
        net = filter(lambda u: u[0] == water, hbnet[0][frame+1])
        water_network[ind,3]=len(net)
        if (water_network[ind,3]>3):
            water_network[ind,3]=3
    
    for ind in range(n_win):
        A[water_network[ind,0],water_network[ind,1],water_network[ind,2],water_network[ind,3]] += 1

A[:,:,:,:] /= float(nsteps)

out=open("numberHB.dat",'w')
out1=open("numberHB_sel.dat",'w')

cpt = np.zeros(4*4)
first_layer = 0
mean_hb = 0

for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                if A[i,j,k,l] > 5:
                    out1.write(str(i)+' '+str(j)+' '+str(k)+' '+str(l)+' '+str(A[i,j,k,l]/n_win*100)+'\n')
                out.write(str(i)+' '+str(j)+' '+str(k)+' '+str(l)+' '+str(A[i,j,k,l]/n_win*100)+'\n')

                cpt[i]+=A[i,j,k,l]
                cpt[4+j]+=A[i,j,k,l]
                cpt[8+k]+=A[i,j,k,l]
                cpt[12+l]+=A[i,j,k,l]
                if (i==0 and j==0):
                    first_layer+=A[i,j,k,l]
                    mean_hb+=(k+l)*A[i,j,k,l]

out1.write('\nTotal: \n')
out1.write('\nNot in first layer: '+str(first_layer/n_win*100)+'\n')
out1.write('\nMean hb in bulk layer: '+str(mean_hb/first_layer)+'\n')

for typ in range(4*4):
    out1.write(str(typ) + ' ')
    out1.write(str(cpt[typ]/n_win*100) + '\n')

out.close()
out1.close()
