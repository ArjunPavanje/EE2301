import numpy as np

ie = 1.0755e-3
Vt = 0.025875
re = Vt/ie 
RC = 2200
RL = 10e3
Rc = RC*RL/(RC+RL)
A = Rc/re
RE = 1e3
Ri = RE*re/(re+RE)
print("Rin: ", re)
print("gain: ", A)
