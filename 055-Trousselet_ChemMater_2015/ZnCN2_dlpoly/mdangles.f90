  program mdangles
    integer i,j,k,l,m,n,p,q1,q2,q3,r1,r2,r3,q123,zat,izn,zm,mm
    integer it,mk,ml,nex,nnt,nr,nd,nr2,nd2
    real(kind=8) errcnt
    real(kind=8), dimension(:,:), allocatable :: ri,rj,zang,dzz
    real(kind=8), dimension(3) :: Ta,Tb,Tc,cgz,cgcn,r3a,r3b
    real(kind=8), dimension(50) :: dzn
!    real(kind=8), dimension(1000,15):: zang  
    integer, dimension(1000) :: nang
    integer, dimension(180) :: gthe
    integer, dimension(:), allocatable :: gr,gd,ge
    real(kind=8) ra,rb,rc,rra,rrb,rrc,d,dd,dco,pi,rcut,rcn,rzc,dr,dzcn,dz1,dz2
    integer,dimension(:,:), allocatable :: nei,bc,nni,bcn
    character iat,truc
    character, dimension(:), allocatable :: nat
    parameter(pi=3.1415926535897,zm=16,rcut=5.8,rcn=1.18,rzc=2.8,dr=0.02)
!! max. zm neighbors per Zn (in case of strong deformations of tetrahedra!) 
!!rzc: max.distance from Zn to 4 (first) C/N, ALSO min. Zn-Zn distance
    parameter(nt=200)
    nr=int((rcut-rzc)/dr)+1
    nr2=int(2.0/dr)+1
    print *,nr,nr2
    allocate(gr(nr))
    allocate(gd(nr2))
    allocate(ge(nr2))
    gr(:)=0
    gd(:)=0
    ge(:)=0

!    open(unit=10,file='gsiP_hists/HISTORYP01p',action='read')
!    open(unit=11,file='gthetaZnCN_gsiP1p',action='write')
!    open(unit=12,file='grZnZn_gsiP1p',action='write')
    open(unit=10,action='read')
    open(unit=11,action='write')
    open(unit=12,action='write')
    open(unit=13,action='write')
    open(unit=14,action='write')

!    read(10,*) truc
    read(10,*) m,p,n
    print *,n

    allocate(nei(n/5,zm))
    allocate(bc(n/5,zm))
    allocate(nni(n/5,zm))
    allocate(bcn(n/5,zm))
    allocate(dzz(n/5,zm))

    allocate(ri(n,3))
    allocate(rj(n,3))
    allocate(zang(n,4))
    allocate(nat(n))
    
    gthe(:)=0.0
    nnt=nt

    errcnt=0.0
    do it=1,nnt
       nex=0
       if(mod(it,nt/5).eq.1) print *,'reading snapshot',it
       read(10,*) truc,m,n,p,q1,rra
       read(10,*) ta(1),ta(2),ta(3)
       read(10,*) tb(1),tb(2),tb(3)
       read(10,*) tc(1),tc(2),tc(3)
       
       if(it.le.3.or.it.eq.10.or.it.eq.nt-10) then
          print *,it
          print *,'Ta',ta
          print *,'Tb',tb
          print *,'Tc',tc
       endif

       izn=0
       icn=0
       do i=1,n
          read(10,*) iat,zat
          read(10,*) ra,rb,rc
!          read(10,*) rra,rrb,rrc
!          read(10,*) rra,rrb,rrc
          if(iat(:1).eq.'Z') then
             izn=izn+1
             ri(izn,1)=ra
             ri(izn,2)=rb
             ri(izn,3)=rc
          else
             icn=icn+1
             nat(icn)=iat
             rj(icn,1)=ra
             rj(icn,2)=rb
             rj(icn,3)=rc
          endif
       enddo
       
       if(izn.ne.n/5) print *,izn,'wrong counting!!'
       
       l=0
       do i=1,izn
          k=0
          nei(i,:)=0
          bc(i,:)=13
          dzz(i,:)=0.0
          do j=1,izn
             q123=13
             if(j.eq.i) goto 101
             r3a(:)=ri(i,:)
             r3b(:)=ri(j,:)
             call pbcdist(r3a,r3b,ta,tb,tc,d,q123)
             d=sqrt(d)
             if(d.lt.rcut) then
                k=k+1
                nei(i,k)=j
                bc(i,k)=q123
                dzz(i,k)=d
                if(k.eq.zm) stop 11
             endif             
101          continue
          enddo
          
          k=0
          nni(i,:)=0
          bcn(i,:)=13
          dzn(:)=0.0
          do j=1,icn
             r3a(:)=ri(i,:)
             r3b(:)=rj(j,:)
             call pbcdist(r3a,r3b,ta,tb,tc,d,q123)
             d=sqrt(d)
             if(d.lt.rzc) then
               
                k=k+1
                dzn(k)=d
                nni(i,k)=j
                bcn(i,k)=q123
                if(k.gt.1) then !!reordering of the neighbor's list
                   do l=1,k-1
                      if(d.le.dzn(k-L)) then !! possibility of exact equality included?
                         dzn(k-L+1)=dzn(k-L)                         
                         nni(i,k-L+1)=nni(i,k-L)
                         bcn(i,k-L+1)=bcn(i,k-L)
                         dzn(k-L)=d
                         nni(i,k-L)=j
                         bcn(i,k-L)=q123
                      endif
                   enddo
                endif

             endif
          enddo
          if(k.lt.4) print *,'WARNING: z<4-COORD',i
          if(dzn(5).lt.dzn(4)+0.001.and.k.ge.5) print *,'WARNING:4- or 5-COORD?',i,'->',nni(i,4),nni(i,5),'at',dzn(4),dzn(5)
       enddo
       
       do i=1,izn
          zang(i,:)=0.0
          mm=0
          do j=1,zm
             if(nei(i,j).eq.0) goto 200
             !1) recuperer les coord. du Zn en bout de liaison
             q1=-1+mod(bc(i,j),3) !x-shift variable (<->pbc)
             q2=-1+mod(bc(i,j)/3,3) ! ..
             q3=-1+bc(i,j)/9   
             d=0.0 !first: Zn-Zn distance (used later)
             do p=1,3
                d=d+(ri(i,p)-ri(nei(i,j),p)+q1*ta(p)+q2*tb(p)+q3*tc(p))**2             
             enddo
             d=sqrt(d)
             if(abs(d-dzz(i,j)).gt.0.001) stop 5
             
             !2) scanner pour chaque Zn les 4 premiers voisins C/N -> trouver la paire du lien
             do k=1,4 !voisins du Zn "i"
                mk=0
                ml=0
                do l=1,4 ! voisins du Zn "nei(i,j)"
                   if(nni(i,k)*nni(nei(i,j),l).eq.0.or.nat(nni(i,k)).eq.nat(nni(nei(i,j),l))) goto 300
                   if(nni(i,k).gt.2*izn.or.nni(nei(i,j),l).le.2*izn) goto 300 !!added 23/10 17h40
                   r3a(:)=rj(nni(i,k),:)
                   r3b(:)=rj(nni(nei(i,j),l),:)
                   call pbcdist(r3a,r3b,ta,tb,tc,dd,q123)
                   if(dd.le.1.0) print *,'WARNING',dd,'<--',nni(i,k),nni(nei(i,j),l),d
                   if(dd.le.1.0) goto 300
                   dd=sqrt(dd) !eventually CN (or NC) distance for ~4*2 neighbor pairs
                   if(dd<rcn) then
                      dco=0.0
                      r1=-1+mod(q123,3)
                      r2=-1+mod(q123/3,3)
                      r3=-1+mod(q123/9,3)
                      do p=1,3
                         dco=dco+(rj(nni(i,k),p)-rj(nni(nei(i,j),l),p)+r1*ta(p)+r2*tb(p)+r3*tc(p))&
                              *(ri(i,p)-ri(nei(i,j),p)+q1*ta(p)+q2*tb(p)+q3*tc(p))
                         cgz(p)=0.5*(ri(i,p)+ri(nei(i,j),p)-q1*ta(p)-q2*tb(p)-q3*tc(p))
                         cgcn(p)=0.5*(rj(nni(i,k),p)+rj(nni(nei(i,j),l),p)-r1*ta(p)-r2*tb(p)-r3*tc(p))
                      enddo

                      dco=(180/pi)*acos(dco/(d*dd))
                      mm=mm+1
                      if(mk.eq.0) ml=nni(nei(i,j),l)
                      if(mk.ne.0) ml=ml+(n+1)*nni(nei(i,j),l)
                      zang(i,mm)=dco  ! The(ZiZj|CkNl) or (ZiZj|NkCl) in deg
                      mk=mk+1

                      ! store also d(Zn-Zn) (only if the right C&N found inbetween)
                      if(dzz(i,j).le.rzc) goto 291
                      nd=1+int((dzz(i,j)-rzc)/dr)
                      gr(nd)=gr(nd)+1                      
291                   continue
                      
                      call pbcdist(cgz,cgcn,ta,tb,tc,dzcn,q123)
                      dzcn=sqrt(dzcn)
                      nd2=1+int((dzcn/dr))

                      if(nd2.gt.nr2) goto 1711
                      gd(nd2)=gd(nd2)+1
1711                  continue

                      !next: dz1 and dz2 are distances of CN's cdm to both Zns;their difference e ->g(e) in fort.14
                      r3a(:)=ri(i,:)
                      call pbcdist(cgcn,r3a,ta,tb,tc,dz1,q123)
                      dz1=sqrt(dz1)
                      
                      r3a(:)=ri(nei(i,j),:)
                      call pbcdist(cgcn,r3a,ta,tb,tc,dz2,q123)
                      dz2=abs(sqrt(dz2)-dz1)
                      nd2=1+int((dz2/dr))

                      if(nd2.gt.nr2) goto 2511
                      ge(nd2)=ge(nd2)+1
2511                  continue

 
                   endif
300                continue
                enddo
                if(mk.eq.2) then
                   print *,'!!!',i,nei(i,j),nni(i,k),mod(ml,n+1),ml/(n+1)
                   print *,nni(nei(i,j),:)
!                   print *,ri(i,:)!                   print *,rj(mod(ml,n+1),:)
                   stop 23
                endif
             enddo
200          continue
          enddo
          nang(i)=mm
       enddo  !! i("central Zn")-loop
       
       mm=0

       do i=1,izn
          if(nang(i).ge.0) then
             !		print *,i,nang(i),zang(i,1),nei(i,1),nei(i,2)
             do l=1,nang(i)  !! assumed: nang(i)>0 (i.e. >=2 neighbors of ith
                !	print *,zang(i,l)
      	    	gthe(1+int(2*zang(i,l)))=gthe(1+int(2*zang(i,l)))+1 !! chosen: 1-degree resolution..
         enddo
      endif
      mm=mm+nang(i)
   enddo
   if(mm.ne.2*izn) print *,2*izn-mm,'bonds not included at step',it
   errcnt=errcnt+(2*izn-mm)*1.0/(2*izn)   
enddo
errcnt=errcnt/nt

do i=1,180 !! 180: ~pi/2, pas lié à nt..
   write(11,*) (i-1)*0.5d0,gthe(i)*1.0/(1*nnt)
enddo
do i=1,nr
   d=rzc+(i-1)*(rcut-rzc)/nr
   write(12,*) d,gr(i)*(1.0/nnt)
enddo
do i=1,nr2
   d2=(i-1)*dr
   write(13,*) d2,gd(i)*(1.0/nnt)
   write(14,*) d2,ge(i)*(1.0/nnt)
enddo
print *,errcnt    
end program mdangles


!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!                  
subroutine pbcdist(r3a,r3b,ta,tb,tc,d,q123)
integer p,q123,r1,r2,r3
real(kind=8), dimension(3) :: r3a,r3b,ta,tb,tc
real(kind=8) d,d2
  d=0.
  do p=1,3
     d=d+(r3a(p)-r3b(p))**2
  enddo

  q123=13 ! now find right PBC-shift, among 3^3                                                                                          
  do r1=-1,1
     do r2=-1,1
        do r3=-1,1
           d2=0.0
           do p=1,3
              d2=d2+(r3a(p)-r3b(p)+r1*ta(p)+r2*tb(p)+r3*tc(p))**2
           enddo
           if(d2<d) then
              d=d2
              q123=(r1+1)+3*(r2+1)+9*(r3+1)
           endif
           enddo
     enddo
  enddo
end subroutine pbcdist

