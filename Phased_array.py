import numpy as np
import random
from matplotlib import pyplot as plt
from scipy import interpolate

x_min = -10
x_max = 10
y_max = 20
x_steps = 100
y_steps = 200
F = 10.0
d = 0.25
theta = 0
wave = 0.68
noise = 0.0
x = np.linspace(x_min,x_max,x_steps)
y = np.linspace(0,y_max,y_steps)
E_field = np.zeros((y_steps,x_steps))
E_parabola = np.zeros((y_steps,x_steps))
E_linear = np.zeros((y_steps,x_steps))

for i in range(x_steps):
    for k in range(y_steps):
        for p in range(-20,20):
            n = (p-1)/2
            E_field[k,i] += np.exp(2*np.pi*1j/wave*(np.sqrt((x[i]-p*d)**2\
                +y[k]**2))-2*np.pi*1j/wave*(np.sqrt((p*d)**2+F**2)-F+ \
                noise*random.random()*(np.sqrt((p*d)**2+F**2)-F)))/\
                ((x[i]-p*d)**2+y[k]**2)**0.25
            #E_linear[k,i] += np.exp(2*np.pi*1j/wave*(np.sqrt((x[i]-p*d)**2\
            #    +y[k]**2)-0*p*d*np.sin(np.pi/6)))/\
            #    ((x[i]-p*d)**2+y[k]**2)**0.25




E_focus = np.zeros(1000)
x = np.linspace(-2,2,1000)
y_1 = np.linspace(-1,1,100)
y_2 = np.linspace(-1,1,100)
for k in range(1000):
    for p in range(-20,20):
        E_focus[k] += np.exp(2*np.pi*1j/wave*(np.sqrt((x[k]-p*d)**2\
            +10**2)-np.sqrt((p*d)**2+F**2)-F+noise*random.random()*(np.sqrt((p*d)**2+F**2)-F)))/\
            ((x[k]-p*d)**2+10**2)**0.25

f = interpolate.interp1d(x,E_focus)
E_2 = np.zeros((100,100))
for i in range(100):
    for j in range(100):
        E_2[i,j] = f(np.sqrt(y_1[i]**2+y_2[j]**2))


print(max(E_focus))
plt.figure(1)
plt.imshow(E_field[1:]**2,cmap='Purples',aspect='auto',origin = 'lower',extent=(0,10,0,10))
plt.ylabel('z [$\mu$m]')
plt.xlabel('x [$\mu$m]')
plt.title('$\lambda$ = 400 nm')
plt.figure(2)
plt.plot((E_focus/max(E_focus))**2,'b-')
plt.figure(3)
plt.title('$\lambda$ = 680 nm')
plt.ylabel('y [$\mu$m]')
plt.xlabel('x [$\mu$m]')
plt.imshow((E_2/np.amax(E_2))**2,cmap='Reds',extent=(0,2,0,2))
#plt.figure(4)
#plt.imshow(E_linear[1:]**2,aspect='auto',origin='lower')
plt.show()
