#%%
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import entropy

fig = plt.figure()
ax = plt.axes(projection='3d')

def f(x, y):
    if x ==0:
        if y==0:
            return 0
        return y*math.log2(1/y)+(1-x-y)*math.log2(1/(1-x-y))
    elif y==0:
        return x*math.log2(1/x)+(1-x-y)*math.log2(1/(1-x-y))
    
    return x*math.log2(1/x)+y*math.log2(1/y)+(1-x-y)*math.log2(1/(1-x-y))

f2=np.vectorize(f)
x=np.linspace(0.001,1,30)
y=np.linspace(0.001,1,30)

X,Y=np.meshgrid(x,y)
Z=f2(X,Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')





# %%
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import entropy
fig = plt.figure()
ax = plt.axes(projection='3d')

x=np.linspace(0.001,1,30)
y=np.linspace(0.001,1,30)

X,Y=np.meshgrid(x,y)
Z=entropy([X,Y, X-Y], base=2)
fig = plt.figure()


ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
# %%
import matplotlib as mt
from scipy.stats import entropy
x=np.linspace(0.001,1,30)
y=np.linspace(0.001,1,30)

X,Y=np.meshgrid(x,y)
Z=entropy([X,Y, X-Y], base=2)
