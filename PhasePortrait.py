import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

#Define the dynamical system
def dynamicsStateSpace (x,t): 
    dx1dt=x[0]*(1-x[0]-x[1])
    dx2dt=x[1]*(-0.5+0.75*x[0])
    return[dx1dt,dx2dt]

#Define a grid of points at which the arrows will be shown
x0=np.linspace(-1,2,20)
x1=np.linspace(-1,2,20)

#Grid
X0,X1=np.meshgrid(x0,x1)

#Evaluating the vector field at each grid point 
dX0=np.zeros(X0.shape)
dX1=np.zeros(X1.shape) #these will store the arrow directions

shape1,shape2=X1.shape

for indexShape1 in range(shape1):
    for indexShape2 in range(shape2):
        dxdtAtx=dynamicsStateSpace([X0[indexShape1,indexShape2],X1[indexShape1,indexShape2]],0)
        dX0[indexShape1,indexShape2]=dxdtAtx[0]
        dX1[indexShape1,indexShape2]=dxdtAtx[1]
        

initial_conditions = [
    [0.2, 0.1],
    [0.4, 0.8],
    [0.9, 0.1],
    [1.2, 0.2],
    [1.1, 0.8]
]

#Plot the phase portrait
plt.figure(figsize=(8, 8))
plt.quiver(X0, X1, dX0, dX1, color='b')
plt.xlim(-1, 2)
plt.ylim(-1, 2)

#initial conditions from for trajectories observation 
simulationTime = np.linspace(0, 200, 20000)
for x0 in initial_conditions:
    solutionState = odeint(dynamicsStateSpace, x0, simulationTime)
    plt.plot(solutionState[:, 0], solutionState[:, 1], label=f'x0={x0}')
    
#marking initial conditions 
plt.plot(0, 0, 'ro', markersize=7, label='x_eq1=(0,0)')
plt.plot(1, 0, 'go', markersize=7, label='x_eq2=(1,0)')
plt.plot(2/3, 1/3, 'bo', markersize=7, label='x_eq3=(2/3,1/3)')

#nullclines
x1_vals = np.linspace(-1, 2, 200)
plt.axvline(x=0, color='orange', linestyle='--', linewidth=1.5) #x1
plt.plot(x1_vals, 1 - x1_vals, color='orange', linestyle='--', linewidth=1.5, label='x1-nullclines')
plt.axhline(y=0, color='magenta', linestyle='--', linewidth=1.5) #x2
plt.axvline(x=2/3, color='magenta', linestyle='--', linewidth=1.5, label='x2-nullclines')

#overall layout 
plt.title('Phase Portrait', fontsize=14)
plt.xlabel('x1 (prey)', fontsize=14)
plt.ylabel('x2 (predator)', fontsize=14)
plt.legend(fontsize=8)
plt.grid(True)
plt.show()





