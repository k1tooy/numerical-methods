#Use the portion of the given steam table for superheated 
#H2O at 200 MPa to (a) find the corresponding entropy s for a specifi c volume v of 0.108 m3/kg with quadratic interpolation
 #v(m3/kg) 0.10377 0.11144 0.1254
 #s(kJ/kg ? K) 6.4147 6.5453 6.7664

import numpy as np
from scipy.interpolate import interp1d

# Data
specific_volume = np.array([0.10377, 0.11144, 0.1254])
entropy = np.array([6.4147, 6.5453, 6.7664])

# Quadratic interpolation
quadratic_interp = interp1d(specific_volume, entropy, kind='quadratic')
v = 0.108
estimated_entropy_quadratic = quadratic_interp(v)
print(f"Estimated entropy at v = 0.108 m³/kg using quadratic interpolation: {estimated_entropy_quadratic:.4f} kJ/kg·K")
