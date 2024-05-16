#Use the portion of the given steam table for superheated 
#H2O at 200 MPa to (a) find the corresponding entropy s for a specifi c volume v of 0.108 m3/kg with quadratic interpolation
 #v(m3/kg) 0.10377 0.11144 0.1254
 #s(kJ/kg ? K) 6.4147 6.5453 6.7664

import numpy as np

# Data
specific_volume = np.array([0.10377, 0.11144, 0.1254])
entropy = np.array([6.4147, 6.5453, 6.7664])

# Linear interpolation
def linear_interpolation(x, xp, yp):
    return np.interp(x, xp, yp)

v = 0.108
estimated_entropy_linear = linear_interpolation(v, specific_volume, entropy)
print(f"Estimated entropy for specific volume {v} m³/kg using linear interpolation: {estimated_entropy_linear:.4f} kJ/kg·K")
