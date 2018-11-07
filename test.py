import numpy as np


M=np.matrix([[0,2,1,0,0],[0,0,0,1,1],[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0]])
Mk=M
print(Mk)
print('\n')
for k in range(3):
    Mk=M*Mk
    print(Mk)
    print('\n')
