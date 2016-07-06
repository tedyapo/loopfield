#!/usr/bin/env python3

import math
import numpy as np
import scipy.special

nm = 1.e-9
um = 1.e-6
mm = 1.e-3
cm = 1.e-2
m = 1.
uA = 1.e-6
mA = 1.e-3
A = 1.
km = 1.e3
nT = 1.e-9
uT = 1.e-6
mT = 1.e-3
T = 1.

def normalize(v):
  l = np.linalg.norm(v)
  epsilon = 1e-9
  if l < epsilon:
    raise ValueError("Vector with |v| < e normalized")
  return v / l

# filamentary current loop
class Loop(object):
  def __init__(self, position, normal, radius, current):
    self.p = np.array(position, dtype = np.float64)
    self.n = normalize(np.array(normal, dtype = np.float64))
    self.r = np.float64(radius)
    self.i = np.float64(current)

# vector magnetic field (B) produced by collection of current loops
class Field(object):
  def __init__(self,
               length_units = m,
               current_units = A,
               field_units = T):
    self.loops = []
    self._length_units = length_units
    self._field_units = field_units
    self._epsilon = np.finfo(np.float64).eps
    
  def addLoop(self, loop):
    self.loops.append(loop)
    
  def evaluate(self, position):
    _p = np.array(position)
    B = np.array([0., 0., 0.])
    for loop in self.loops:
      B += self._evalLoop(_p, loop)
    return B / self._field_units
  
  def _evalLoop(self, p, loop):
    r_vect = (p - loop.p) * self._length_units
    r = np.linalg.norm(r_vect)
    z = loop.n.dot(r_vect)
    rho_vect = r_vect - z * loop.n
    rho = np.linalg.norm(rho_vect)
    if rho > self._epsilon:
      rho_vect = rho_vect / rho

    a = loop.r * self._length_units
    alpha2 = a*a + rho*rho + z*z - 2.*a*rho
    beta2 = a*a + rho*rho + z*z + 2.*a*rho
    beta = math.sqrt(beta2)        
    c = 4.e-7 * loop.i  # \mu_0  I / \pi
    a2b2 = alpha2 / beta2
    Ek2 = scipy.special.ellipe(1. - a2b2)
    Kk2 = scipy.special.ellipkm1(a2b2)
    
    denom = (2. * alpha2 * beta * rho)
    if math.fabs(denom) > self._epsilon:
      Brho = c*z*(((a*a + rho*rho + z*z)*Ek2 - alpha2*Kk2) /
                denom)
    else:
      Brho = 0.

    denom = (2. * alpha2 * beta)
    if math.fabs(denom) > self._epsilon:
      Bz = c*(((a*a - rho*rho - z*z)*Ek2 + alpha2*Kk2) /
              denom)
    else:
      Bz = np.inf

    M = np.array([rho_vect, loop.n]).transpose()
    B = np.array([Brho, Bz])
    return M.dot(B)

