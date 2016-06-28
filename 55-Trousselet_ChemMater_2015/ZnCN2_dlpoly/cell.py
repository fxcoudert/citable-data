#!/usr/bin/env python

import numpy as np
import math, sys

def vec(x,y,z):
  return np.array((float(x), float(y), float(z)))

def vector_angle(v1, v2):
  v1_u = v1 / np.linalg.norm(v1)
  v2_u = v2 / np.linalg.norm(v2)
  angle = np.arccos(np.dot(v1_u, v2_u))
  if math.isnan(angle):
    if np.dot(v1_u, v2_u) > 0:
      return 0.0
    else:
      return np.pi
  return angle

def read_STATIS():
  f = open("STATISdiaT300t05", "r")
  cells = []
  f.readline()
  f.readline()

  while True:
    line = f.readline()
    if line == "":
      break

    n = int(line.split()[-1])
    s = " ".join([f.readline().strip() for i in range((n+4)/5)])
    vecs = map(float, s.split()[-9:])
    a = vec(*vecs[0:3])
    b = vec(*vecs[3:6])
    c = vec(*vecs[6:9])
    cells.append(np.vstack((a,b,c)))

  f.close()
  return cells


def read_HISTORY():
  f = open("HISTORY", "r")
  cells = []

  while True:
    line = f.readline()
    if line == "":
      break
    if not "timestep" in line:
      continue

    a = vec(*map(float, f.readline().strip().split()))
    b = vec(*map(float, f.readline().strip().split()))
    c = vec(*map(float, f.readline().strip().split()))
    cells.append(np.vstack((a,b,c)))

  f.close()
  return cells


########################################################################
# Main code follows

def main():

  cells = read_STATIS()

  print str(len(cells)) + " configurations found"

  # Throw away the first 10%
  cells = cells[len(cells)/10:]

  aa=str(np.mean([np.linalg.norm(uc[0]) for uc in cells]))
  bb=str(np.mean([np.linalg.norm(uc[1]) for uc in cells]))
  cc=str(np.mean([np.linalg.norm(uc[2]) for uc in cells]))
  print "<a><b><c> = " + aa[0:7] +" " + bb[0:7] +" " +cc[0:7]

  al=np.rad2deg(np.mean([vector_angle(uc[1], uc[2]) for uc in cells]))
  be=np.rad2deg(np.mean([vector_angle(uc[0], uc[2]) for uc in cells]))
  ga=np.rad2deg(np.mean([vector_angle(uc[0], uc[1]) for uc in cells]))
  print "<alpha><beta><gamma> = %g %g %g" % (al , be , ga)

  volume = np.mean(map(np.linalg.det, cells))
  print "  <vol> = %g" % volume

  # Calculating the strain matrices
  h0m1 = np.linalg.inv(cells[0])
  h0m1t = h0m1.transpose()

  def h2eps(h):
    return (np.dot(h0m1t, np.dot(h.transpose(), np.dot(h, h0m1))) - np.identity(3)) / 2

  eps = map(h2eps, cells)

  # Elastic constants
  temp = 300
  factor = (volume * 1.e-30) / (1.3806488e-23 * temp)
  Voigt_map = ((0, 0), (1, 1), (2, 2), (2, 1), (2, 0), (1, 0))
  Smat = np.zeros((6,6))
  for i in range(6):
    fi = np.mean([ e[Voigt_map[i]] for e in eps ])
    for j in range(i+1):
      fj = np.mean([ e[Voigt_map[j]] for e in eps ])
      fij = np.mean([ e[Voigt_map[i]] * e[Voigt_map[j]] for e in eps ])
      Smat[i,j] = factor * (fij - fi * fj)

  for i in range(5):
    for j in range(i+1,6):
      Smat[i][j] = Smat[j][i]

  # And now the stiffness matrix (in GPa)
  Cmat = np.linalg.inv(Smat) / 1.e9

  print ''
  print 'Stiffness matrix C (GPa):'
  for i in range(6):
    print '    ' ,
    for j in range(6):
      if j >= i:
          print ('% 8.2f' % Cmat[i,j]) ,
      else:
          print '        ' ,
    print ''

  print 'Stiffness matrix C (GPa; mathematica format):'
  for i in range(6):
    print '    ' ,
    print "% 8.2f , % 8.2f , % 8.2f , % 8.2f , % 8.2f , % 8.2f" % (Cmat[i,0],Cmat[i,1],Cmat[i,2],Cmat[i,3],Cmat[i,4],Cmat[i,5])
    print ''


  # Eigenvalues
  print ''
  print 'Stiffness matrix eigenvalues (GPa):'
  print (6*'% 8.2f') % tuple(np.sort(np.linalg.eigvals(Cmat)))

  sys.exit(0)


if __name__ == "__main__":
  main()
