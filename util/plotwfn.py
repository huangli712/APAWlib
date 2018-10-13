import sys
import matplotlib
matplotlib.use("pdf") # setup backend
import matplotlib.pyplot as plt
import numpy as np

# get maximum number of wave functions
argu = sys.argv[1:]
if ( len(argu) > 0 ):
    maxl = int(argu[0])
else:
    maxl = 2

# check lower bound for maxl
if maxl <= 1:
    sys.exit(-1)

# check upper bound for maxl
if maxl >= 10:
    sys.exit(-1)

# create plot layout
f, axarr = plt.subplots(3,3)
plt.subplots_adjust(hspace = 0.5, wspace = 0.3)

if maxl >= 1:
    radius, pw, ps, projector = np.loadtxt('wfn1', unpack = True)
    lines = axarr[0,0].plot(radius, pw, radius, ps, radius, projector)
    plt.setp(lines[0], label = r'$\phi_i$')
    plt.setp(lines[1], label = r'$\tilde{\phi}_i$')
    plt.setp(lines[2], label = r'$\tilde{p}_i$')
    axarr[0,0].legend()
    axarr[0,0].set_title(r'$wfn1$')

if maxl >= 2:
    radius, pw, ps, projector = np.loadtxt('wfn2', unpack = True)
    lines = axarr[0,1].plot(radius, pw, radius, ps, radius, projector)
    plt.setp(lines[0], label = r'$\phi_i$')
    plt.setp(lines[1], label = r'$\tilde{\phi}_i$')
    plt.setp(lines[2], label = r'$\tilde{p}_i$')
    axarr[0,1].legend()
    axarr[0,1].set_title(r'$wfn2$')

if maxl >= 3:
    radius, pw, ps, projector = np.loadtxt('wfn3', unpack = True)
    lines = axarr[0,2].plot(radius, pw, radius, ps, radius, projector)
    plt.setp(lines[0], label = r'$\phi_i$')
    plt.setp(lines[1], label = r'$\tilde{\phi}_i$')
    plt.setp(lines[2], label = r'$\tilde{p}_i$')
    axarr[0,2].legend()
    axarr[0,2].set_title(r'$wfn3$')

if maxl >= 4:
    radius, pw, ps, projector = np.loadtxt('wfn4', unpack = True)
    lines = axarr[1,0].plot(radius, pw, radius, ps, radius, projector)
    plt.setp(lines[0], label = r'$\phi_i$')
    plt.setp(lines[1], label = r'$\tilde{\phi}_i$')
    plt.setp(lines[2], label = r'$\tilde{p}_i$')
    axarr[1,0].legend()
    axarr[1,0].set_title(r'$wfn4$')

if maxl >= 5:
    radius, pw, ps, projector = np.loadtxt('wfn5', unpack = True)
    lines = axarr[1,1].plot(radius, pw, radius, ps, radius, projector)
    plt.setp(lines[0], label = r'$\phi_i$')
    plt.setp(lines[1], label = r'$\tilde{\phi}_i$')
    plt.setp(lines[2], label = r'$\tilde{p}_i$')
    axarr[1,1].legend()
    axarr[1,1].set_title(r'$wfn5$')

if maxl >= 6:
    radius, pw, ps, projector = np.loadtxt('wfn6', unpack = True)
    lines = axarr[1,2].plot(radius, pw, radius, ps, radius, projector)
    plt.setp(lines[0], label = r'$\phi_i$')
    plt.setp(lines[1], label = r'$\tilde{\phi}_i$')
    plt.setp(lines[2], label = r'$\tilde{p}_i$')
    axarr[1,2].legend()
    axarr[1,2].set_title(r'$wfn6$')

if maxl >= 7:
    radius, pw, ps, projector = np.loadtxt('wfn7', unpack = True)
    lines = axarr[2,0].plot(radius, pw, radius, ps, radius, projector)
    plt.setp(lines[0], label = r'$\phi_i$')
    plt.setp(lines[1], label = r'$\tilde{\phi}_i$')
    plt.setp(lines[2], label = r'$\tilde{p}_i$')
    axarr[2,0].legend()
    axarr[2,0].set_title(r'$wfn7$')

if maxl >= 8:
    radius, pw, ps, projector = np.loadtxt('wfn8', unpack = True)
    lines = axarr[2,1].plot(radius, pw, radius, ps, radius, projector)
    plt.setp(lines[0], label = r'$\phi_i$')
    plt.setp(lines[1], label = r'$\tilde{\phi}_i$')
    plt.setp(lines[2], label = r'$\tilde{p}_i$')
    axarr[2,1].legend()
    axarr[2,1].set_title(r'$wfn8$')

if maxl >= 9:
    radius, pw, ps, projector = np.loadtxt('wfn9', unpack = True)
    lines = axarr[2,2].plot(radius, pw, radius, ps, radius, projector)
    plt.setp(lines[0], label = r'$\phi_i$')
    plt.setp(lines[1], label = r'$\tilde{\phi}_i$')
    plt.setp(lines[2], label = r'$\tilde{p}_i$')
    axarr[2,2].legend()
    axarr[2,2].set_title(r'$wfn9$')

plt.savefig("paw_wfn.pdf",bbox_inches='tight')
