from cmath import log10
import math
Mx = float(input("Maximum Allowable SPL (dB): "))
Rp = float(input("Reference Pressure (Pa): "))
Pv = float(input("Particle Velocity (m/s): "))
SPL = 20*log10(Rp)