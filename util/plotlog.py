import sys
import matplotlib
matplotlib.use("pdf") # setup backend
import matplotlib.pyplot as plt
import numpy as np

# get maximum l
argu = sys.argv[1:]
if ( len(argu) > 0 ):
    maxl = int(argu[0])
else:
    maxl = 0

# check lower bound for maximum l
if maxl <= 0:
    sys.exit(-1)

# check upper bound for maximum l
if maxl >= 4:
    sys.exit(-1)

# create plot layout
f, axarr = plt.subplots(2,2)
plt.subplots_adjust(hspace = 0.3, wspace = 0.3)

# for l == 0, s orbital
if maxl >= 0:
    energy, exact, paw = np.loadtxt('logderiv.0', usecols = (0,1,2), unpack = True)
    lines = axarr[0,0].plot(energy, exact, energy, paw)
    plt.setp(lines[0], label = r'exact')
    plt.setp(lines[1], label = r'paw')
    axarr[0,0].legend()
    axarr[0,0].set_title(r'$l = 0$')

# for l == 1, p orbital
if maxl >= 1:
    energy, exact, paw = np.loadtxt('logderiv.1', usecols = (0,1,2), unpack = True)
    lines = axarr[0,1].plot(energy, exact, energy, paw)
    plt.setp(lines[0], label = r'exact')
    plt.setp(lines[1], label = r'paw')
    axarr[0,1].legend()
    axarr[0,1].set_title(r'$l = 1$')

# for l == 2, d orbital
if maxl >= 2:
    energy, exact, paw = np.loadtxt('logderiv.2', usecols = (0,1,2), unpack = True)
    lines = axarr[1,0].plot(energy, exact, energy, paw)
    plt.setp(lines[0], label = r'exact')
    plt.setp(lines[1], label = r'paw')
    axarr[1,0].legend()
    axarr[1,0].set_title(r'$l = 2$')

# for l == 3, f orbital
if maxl >= 3:
    energy, exact, paw = np.loadtxt('logderiv.3', usecols = (0,1,2), unpack = True)
    lines = axarr[1,1].plot(energy, exact, energy, paw)
    plt.setp(lines[0], label = r'exact')
    plt.setp(lines[1], label = r'paw')
    axarr[1,1].legend()
    axarr[1,1].set_title(r'$l = 3$')

plt.savefig("paw_log.pdf",bbox_inches='tight')
