# importing libraries
import numpy as np
import matplotlib.pyplot as plt

# setting constant values (on 20˚C)
g = 9.81 # gravitational acceleration
rho = 998.23 # water density on 20˚C
alpha = 0.07286 # water surface tension on 20˚C

# give an l interval
l = np.arange(0.001, 0.2, 0.001)

# create three functions that gives the velocity of the wave in function of wavelength (here 'l' is the wavelength)
c_neh = lambda l : np.sqrt((g*l) / (2*np.pi)) # the velocity of the gravitational wave
c_kap = lambda l : np.sqrt((2*np.pi*alpha) / (l*rho)) # the velocity of the capillat wave
c = lambda l : np.sqrt(( (g*l) / (2*np.pi) ) + ( (2*np.pi*alpha) / (l*rho) )) # the velocity of the mixed wave

# check if the minimum value is in the error range
error_limit = 0.1 # give an error range

c_min = ((4*alpha*g) / (rho))**(1/4) # the minimal value of the velocity
l_min = 2*np.pi*np.sqrt(alpha/(rho*g)) # the wavelength of the minimal velocity
c_ = 0 # the velocity from the derivative
l_ = 0 # the wavelength from the derivative

# calcuating the minimal value with the differential quotient
for i in range(len(c(l))-1):
    differential = ( c(l[i+1])-c(l[i]) ) / (0.001)
    if np.abs(c_min-differential) < error_limit:
      c_ = c(l[i])
      l_ = l[i]

# printing values
print("The minimal value of the velocity from the derivative:", '%.5g'%c_, "m/s", "\nThe calculated minimal velocity:", '%.5g'%c_min, "m/s", "\nThe error:", '%.3g'%np.abs(c_-c_min), "m/s")
print("The minimal value of the wavelength from the derivative:", l_, "m", "\nThe calculated minimal wavelength:", '%.5g'%l_min, "m", "\nThe error:", '%-5g'%np.abs(l_-l_min), "m")

if np.abs(c_-c_min) < error_limit and np.abs(l_-l_min) < error_limit:
    print("The results are in the error range.")

# plotting the graph
fig, ax = plt.subplots()
ax.set_xlabel("wavelength (m)")
ax.set_ylabel("velocity (m/s)")

ax.plot(l, c_neh(l), label="gravitational wave")
ax.plot(l, c_kap(l), label="capillar wave")
ax.plot(l, c(l), label="mixed wave")
ax.legend()
plt.grid()
plt.show()
