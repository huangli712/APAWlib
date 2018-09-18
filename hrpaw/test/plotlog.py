import matplotlib
matplotlib.use("pdf") # setup backend
import matplotlib.pyplot as plt
import numpy as np

f, axarr = plt.subplots(2,2)
plt.subplots_adjust(hspace = 0.3, wspace = 0.3)

energy, exact, paw = np.loadtxt('logderiv.0', usecols = (0,1,2), unpack = True)
lines = axarr[0,0].plot(energy, exact, energy, paw)
plt.setp(lines[0], label = r'exact')
plt.setp(lines[1], label = r'paw')
axarr[0,0].legend()
axarr[0,0].set_title(r'$l = 0$')

energy, exact, paw = np.loadtxt('logderiv.1', usecols = (0,1,2), unpack = True)
lines = axarr[0,1].plot(energy, exact, energy, paw)
plt.setp(lines[0], label = r'exact')
plt.setp(lines[1], label = r'paw')
axarr[0,1].legend()
axarr[0,1].set_title(r'$l = 1$')

energy, exact, paw = np.loadtxt('logderiv.2', usecols = (0,1,2), unpack = True)
lines = axarr[1,0].plot(energy, exact, energy, paw)
plt.setp(lines[0], label = r'exact')
plt.setp(lines[1], label = r'paw')
axarr[1,0].legend()
axarr[1,0].set_title(r'$l = 2$')

energy, exact, paw = np.loadtxt('logderiv.3', usecols = (0,1,2), unpack = True)
lines = axarr[1,1].plot(energy, exact, energy, paw)
plt.setp(lines[0], label = r'exact')
plt.setp(lines[1], label = r'paw')
axarr[1,1].legend()
axarr[1,1].set_title(r'$l = 3$')

plt.savefig("paw_log.pdf",bbox_inches='tight')
