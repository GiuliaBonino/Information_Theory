import numpy as np

mi=8.48
ci=[5, 0, 7, 8, 0, 10,0, 0, 0,0 , 15]
pi=[]
for i in range(len(ci)):
    if ci[i]!=0:
        pi.append(ci[i]-mi)
    else:
        pi.append(0)        


print(np.roots(pi))

