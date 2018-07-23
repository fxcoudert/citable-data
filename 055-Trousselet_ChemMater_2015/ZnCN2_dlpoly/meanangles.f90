  program meanangles
    implicit integer(A-Z)
    real(kind=8) errcnt
    real(kind=8), dimension(:,:), allocatable :: ri,zang,rint
    real(kind=8), dimension(3) :: cgz,cgcn,nri,tat,tbt,tct,rri,ori
    real(kind=8), dimension(3) :: Ta,Tb,Tc,Tbp,Tcp,r3a,r3b
    real(kind=8), dimension(3,3) :: Tabc,TM1
    logical ok_flag
    real(kind=8), dimension(50) :: dzn
    real(kind=8),dimension(:), allocatable :: dzz
    integer, dimension(500) :: gthe !! currently: considered over [0;50]degrees, 0.1deg.resolution
    integer, dimension(:), allocatable :: gr,gd,ge,nang
    real(kind=8) ra,rb,rc,rra,rrb,rrc,d,dd,dco,pi,rcut,rcn,rzc,dr,dzcn,dz1,dz2,pab,pac,pbc,d2
    integer,dimension(:,:), allocatable :: nei,bc,nni,bcn
    character iat,truc
    character, dimension(:), allocatable :: nat
    parameter(pi=3.1415926535897,zm=16,rcut=6.0,rcn=1.18,rzc=3.0,dr=0.01)
!! max. zm neighbors per Zn (in case of strong deformations of tetrahedra!) 
!!rzc: max.distance from Zn to 4 (first) C/N, ALSO min. Zn-Zn distance
    parameter(nt=5000)
    nr=int((rcut-rzc)/dr)+1
    nr2=int(2.0/dr)+1
    print *,nr,nr2
    allocate(gr(nr))
    allocate(gd(nr2))
    allocate(ge(nr2))

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

    allocate(ri(n,3))
    allocate(rint(n,3))
    allocate(nat(n))
    
    nnt=nt

    icn=4*n/5
    izn=n/5
       read(10,*) truc,m,n,p,q1,rra
       read(10,*) ta(1),ta(2),ta(3)
       read(10,*) tb(1),tb(2),tb(3)
       read(10,*) tc(1),tc(2),tc(3)
       Tabc(:,1)=ta(:)
       Tabc(:,2)=tb(:)
       Tabc(:,3)=tc(:)
       call m33inv(Tabc,TM1,OK_FLAG)
    do i=1,n
       read(10,*) iat,zat
       nat(i)=iat
       read(10,*) nri(1),nri(2),nri(3)
       call m33mult(TM1,nri,rri)
       ri(i,:)=rri(:)
       rint(i,:)=ri(i,:)
    enddo
          
	nt5=max(5,nt/5)
 do it=1,nnt-1
    if(mod(it,nt5).eq.1) print *,'reading snapshot',it+1
    read(10,*) truc,m,n,p,q1,rra
    read(10,*) tat(1),tat(2),tat(3)
    read(10,*) tbt(1),tbt(2),tbt(3)
    read(10,*) tct(1),tct(2),tct(3)
    call gramschmidt(tat,tbt,tct,tbp,tcp)       
    Tabc(:,1)=tat(:)
    Tabc(:,2)=tbt(:)
    Tabc(:,3)=tct(:)
    call m33inv(tabc,tm1,ok_flag)               !! for later (get reduct coord)                                             
    ta(:)=ta(:)+tat(:)
    tb(:)=tb(:)+tbt(:)
    tc(:)=tc(:)+tct(:)
    
    if(it.le.5.or.it.eq.10.or.it.eq.nt-10) then
       print *,it+1
       print *,'Tc',tct
    endif
    
    do i=1,n
       read(10,*) iat,zat
       read(10,*) ra,rb,rc
       nri(1)=ra
       nri(2)=rb
       nri(3)=rc

!reconstruct former i'th position for comparison
       ori(:)=0.0
       do p=1,3
          ori(p)=ori(p)+ri(i,1)*tat(p)+ri(i,2)*tbt(p)+ri(i,3)*tct(p)
       enddo
       call pbcdist(nri,ori,tat,tbt,tct,d,q123)
       do p=1,3
          nri(p)=nri(p)+(mod(q123,3)-1)*tat(p)+(mod(q123/3,3)-1)*tbt(p)+(mod(q123/9,3)-1)*tct(p)
       enddo       
       call m33mult(tm1,nri,rri)
       rint(i,:)=rint(i,:)+rri(:)
       ri(i,:)=rri(:)
    enddo
 enddo

 do i=1,n       
    rint(i,:)=rint(i,:)/nnt
 enddo
 ta(:)=ta(:)/nnt
 tb(:)=tb(:)/nnt
 tc(:)=tc(:)/nnt
 do i=1,n
    ri(i,:)=0.0
    do p=1,3
       ri(i,p)=ri(i,p)+rint(i,1)*ta(p)+rint(i,2)*tb(p)+rint(i,3)*tc(p)
    enddo
 enddo
       
!	do i=1,n ! write(11,*) i,ri(i,1),ri(i,2),ri(i,3) !enddo

 allocate(nei(n,zm))
 allocate(bc(n,zm))
 allocate(nni(n,zm))
 allocate(bcn(n,zm))
 allocate(dzz(zm))
 allocate(zang(n,4))
 allocate(nang(n))
 gthe(:)=0
 gr(:)=0
 gd(:)=0
 ge(:)=0
 izn=n/5
 icn=4*izn
    
 l1=0
 do i=1,izn
    iz=i+icn
    k=0
    nei(i,:)=0
    bc(i,:)=13
    do j=1,izn
       jz=j+icn
       q123=13
       if(j.eq.i) goto 101
       r3a(:)=ri(iz,:)
       r3b(:)=ri(jz,:)
       call pbcdist(r3a,r3b,ta,tb,tc,d,q123)
       d=sqrt(d)
       if(d.lt.rcut) then
          k=k+1
          l1=l1+1
          nei(i,k)=jz
          bc(i,k)=q123
          dzz(k)=d
          if(k.eq.zm) stop 11
       endif
       
101    continue
    enddo
 enddo
 print *,'!!',l1
 do i=1,izn
    iz=i+icn
    k=0
    nni(i,:)=0
    bcn(i,:)=13
    dzn(:)=0.0
    do j=1,icn
       
       r3a(:)=ri(iz,:)
       r3b(:)=ri(j,:)
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
 
 nang(:)=0
 do i=1,izn
    iz=i+icn
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
          d=d+(ri(iz,p)-ri(nei(i,j),p)+q1*ta(p)+q2*tb(p)+q3*tc(p))**2             
       enddo
       d=sqrt(d)
       i2=nei(i,j)-icn
       !2) scanner pour chaque Zn les 4 premiers voisins C/N -> trouver la paire du lien
       do k=1,4 !voisins du Zn "i"
          mk=0
          ml=0
          do l=1,4 ! voisins du Zn "nei(i,j)"
             if(nni(i,k)*nni(i2,l).eq.0.or.nat(nni(i,k)).eq.nat(nni(i2,l))) goto 300
             if(nni(i,k).gt.2*izn.or.nni(i2,l).le.2*izn) goto 300 !!added 23/10 17h40
             
             r3a(:)=ri(nni(i,k),:)
             r3b(:)=ri(nni(i2,l),:)
             call pbcdist(r3a,r3b,ta,tb,tc,dd,q123)
             dd=sqrt(dd) !eventually CN (or NC) distance for ~4*2 neighbor pairs
             if(dd<rcn) then
                dco=0.0
                r1=-1+mod(q123,3)
                r2=-1+mod(q123/3,3)
                r3=-1+mod(q123/9,3)
                do p=1,3
                   dco=dco+(ri(nni(i,k),p)-ri(nni(i2,l),p)+r1*ta(p)+r2*tb(p)+r3*tc(p))&
                        *(ri(iz,p)-ri(nei(i,j),p)+q1*ta(p)+q2*tb(p)+q3*tc(p))
                   cgz(p)=0.5*(ri(iz,p)+ri(nei(i,j),p)-q1*ta(p)-q2*tb(p)-q3*tc(p))
                   cgcn(p)=0.5*(ri(nni(i,k),p)+ri(nni(i2,l),p)-r1*ta(p)-r2*tb(p)-r3*tc(p))
                enddo
                
                dco=(180/pi)*acos(dco/(d*dd))
                mm=mm+1
                if(mk.eq.0) ml=nni(i2,l)
                if(mk.eq.1) ml=ml+(n+1)*nni(i2,l)
                zang(i,mm)=dco  ! The(ZiZj|CkNl) or (ZiZj|NkCl) in deg
                mk=mk+1
                
                ! store also d(Zn-Zn) (only if the right C&N found inbetween)
                if(dzz(j).le.rzc) goto 291
                nd=1+int((dzz(j)-rzc)/dr)
                gr(nd)=gr(nd)+1                      
291             continue
                
                r3a(:)=cgz(:)
                r3b(:)=cgcn(:)
                call pbcdist(r3a,r3b,ta,tb,tc,dzcn,q123)
                dzcn=sqrt(dzcn)
                nd2=1+int((dzcn/dr))
                
                if(nd2.gt.nr2) goto 1711
                gd(nd2)=gd(nd2)+1
1711            continue
                
                !next: dz1 and dz2 are distances of CN's cdm to both Zns;their difference e ->g(e) in fort.14                   
                r3a(:)=ri(iz,:)
                r3b(:)=cgcn(:)
                call pbcdist(r3a,r3b,ta,tb,tc,dz1,q123)
                dz1=sqrt(dz1)
                   
                r3a(:)=ri(nei(i,j),:)
                r3b(:)=cgcn(:)
                call pbcdist(r3a,r3b,ta,tb,tc,dz2,q123)
                dz2=abs(sqrt(dz2)-dz1)
                nd2=1+int((dz2/dr))
                
                if(nd2.gt.nr2) goto 2511
                ge(nd2)=ge(nd2)+1
2511            continue
                
             endif
300          continue
          enddo
          if(mk.eq.2) then
             print *,'!!!',i,i2,nni(i,k)
             print *,nni(i2,:)
             stop 23
          endif
       enddo
200    continue
    enddo
    nang(i)=mm
 enddo  !! i("central Zn")-loop
 
 mm=0
 do i=1,izn
    if(nang(i).ge.0) then
       !print *,i,nang(i),zang(i,1),nei(i,1),nei(i,2)
       if(nang(i).gt.4) then
          print *,i,zang(i,1:nang(i))
       endif
       do l=1,nang(i)  !! assumed: nang(i)>0 (i.e. >=2 neighbors of ith
          gthe(1+int(10*zang(i,l)))=gthe(1+int(10*zang(i,l)))+1 !! chosen: 0.1-degree resolution..
       enddo
    endif
    mm=mm+nang(i)
 enddo
 if(mm.ne.2*izn) print *,2*izn-mm,'bonds not included at step'
 errcnt=(2*izn-mm)*1.0/(2*izn)   
 
!!!!!!!!!!!!FINALLY WRITING OUTPUT FILES
 do i=1,500 !! 180<- [0:pi/2] avec pas de 0.1 degre ; mais 2 liens/Zn
    write(11,*) (i-1)*0.1d0,gthe(i)*0.5/(izn*0.1)
 enddo
 do i=1,nr
    d=rzc+(i-1)*(rcut-rzc)/nr
    write(12,*) d,gr(i)/(izn*2*dr)
 enddo
 do i=1,nr2
    d2=(i-1)*dr
    write(13,*) d2,gd(i)/(izn*2*dr)
    write(14,*) d2,ge(i)/(izn*2*dr)
 enddo
 print *,errcnt    
end program meanangles

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
subroutine gramschmidt(ta,tb,tc,tbp,tcp)
  real(kind=8), dimension(3) :: Ta,Tb,Tc,Tbp,Tcp
  real(kind=8) pab,pac,pbc,na,nb
  integer p
  pab=0.0
  pac=0.0
  pbc=0.0
  paa=0.0
  pbb=0.0
  do p=1,3
     pab=pab+ta(p)*tb(p)
     paa=paa+ta(p)**2
  enddo
  do p=1,3
     tbp(p)=tb(p)-pab*ta(p)/paa
     pac=pac+tc(p)*ta(p)
     pbc=pbc+tc(p)*tbp(p)
     pbb=pbb+tbp(p)**2
  enddo
  do p=1,3
     tcp(p)=tc(p)-ta(p)*pac/paa-tbp(p)*pbc/pbb
  enddo
end subroutine gramschmidt

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

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!                                                               
subroutine m33mult(A,nri,rri)
integer i,j
double precision, dimension(3,3) :: a
double precision, dimension(3) :: nri,rri
rri(:)=0.0
do i=1,3
   do j=1,3
      rri(i)=rri(i)+a(i,j)*nri(j)
   enddo
enddo
end subroutine m33mult

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!                                                               
 SUBROUTINE M33INV (A, AINV, OK_FLAG)

   IMPLICIT NONE

   DOUBLE PRECISION, DIMENSION(3,3), INTENT(IN)  :: A
   DOUBLE PRECISION, DIMENSION(3,3), INTENT(OUT) :: AINV
   LOGICAL, INTENT(OUT) :: OK_FLAG

   DOUBLE PRECISION, PARAMETER :: EPS = 1.0D-10
   DOUBLE PRECISION :: DET
   DOUBLE PRECISION, DIMENSION(3,3) :: COFACTOR

   DET =   A(1,1)*A(2,2)*A(3,3)  &
        - A(1,1)*A(2,3)*A(3,2)  &
        - A(1,2)*A(2,1)*A(3,3)  &
        + A(1,2)*A(2,3)*A(3,1)  &
        + A(1,3)*A(2,1)*A(3,2)  &
        - A(1,3)*A(2,2)*A(3,1)

   IF (ABS(DET) .LE. EPS) THEN
      AINV = 0.0D0
      OK_FLAG = .FALSE.
      RETURN
   END IF

   COFACTOR(1,1) = +(A(2,2)*A(3,3)-A(2,3)*A(3,2))
   COFACTOR(1,2) = -(A(2,1)*A(3,3)-A(2,3)*A(3,1))
   COFACTOR(1,3) = +(A(2,1)*A(3,2)-A(2,2)*A(3,1))
   COFACTOR(2,1) = -(A(1,2)*A(3,3)-A(1,3)*A(3,2))
   COFACTOR(2,2) = +(A(1,1)*A(3,3)-A(1,3)*A(3,1))
   COFACTOR(2,3) = -(A(1,1)*A(3,2)-A(1,2)*A(3,1))
   COFACTOR(3,1) = +(A(1,2)*A(2,3)-A(1,3)*A(2,2))
   COFACTOR(3,2) = -(A(1,1)*A(2,3)-A(1,3)*A(2,1))
   COFACTOR(3,3) = +(A(1,1)*A(2,2)-A(1,2)*A(2,1))

   AINV = TRANSPOSE(COFACTOR) / DET

   OK_FLAG = .TRUE.

   RETURN

 END SUBROUTINE M33INV

