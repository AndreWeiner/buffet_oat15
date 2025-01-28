import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from utils import average_surface_data, fetch_force_coefficients, interpolate_uniform_1D
import os
from flow_conditions import *

mpl.rcParams['figure.dpi'] = 160
os.makedirs("output", exist_ok = True)

conv_time = CHORD/U_INF

fig, ax = plt.subplots(figsize=(6, 4))
lw = 1.5
ms = 15

cwd = os.getcwd()
path_surf = os.path.join(cwd, "postProcessing/surface/")
data_cp = average_surface_data(path_surf, "total(p)_coeff_airfoil.raw", 0.001, 0.0031, symmetric=False)

ax.plot(data_cp[0], data_cp[2], c="C0", ls="-")
ax.plot(data_cp[1], data_cp[3], c="C0", ls="--")
ax.set_xlabel(r"$\tilde{x}$")
#ax.legend(ncol=2, loc="lower center")
ax.set_ylabel(r"$c_p$")
ax.set_title(r"Variation of pressure Coefficient along chord")
fig.gca().invert_yaxis()




every = 1
path = os.path.join(cwd, "postProcessing/forces/")
t, cd, cl = fetch_force_coefficients(path)
ti, cl = interpolate_uniform_1D(t[::every], cl[::every], 10000)
_, cd = interpolate_uniform_1D(t[::every], cd[::every], 10000)

fig1, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 4))

ax1.plot(ti/conv_time, cd, lw=1)
ax2.plot(ti/conv_time, cl, lw=1)

#ax1.set_ylim(-0.005, 0.05)
ax1.set_ylabel(r"$c_d$")
#ax2.set_xlim(ti["ref. 0"][0], ti_2D["ref. 0"][-1])
#ax2.set_ylim(0.8, 1.1)
ax2.set_xlabel(r"$t$ in $s$")
ax2.set_ylabel(r"$c_l$")
#plt.show()
fig1.suptitle("Lift and drag coefficent")

data_cf = average_surface_data(path_surf, "wallShearStress_airfoil.raw", 0.001, 0.0031, symmetric=False)
fig2, ax3 = plt.subplots(figsize=(6, 4))

ax3.plot(data_cf[0], data_cf[2]/(-0.5*U_INF**2), c="C0", ls="-")
ax3.plot(data_cf[1], data_cf[3]/(-0.5*U_INF**2), c="C0", ls="--")
ax3.set_xlabel(r"$\tilde{x}$")
#ax.legend(ncol=2, loc="lower center")
ax3.set_ylabel(r"$C_f$")
ax3.set_title(r"Skin friction $C_f$")


fig.savefig(os.path.join(cwd, "output/pressure_coeff_along_chord.png"))
fig1.savefig(os.path.join(cwd, "output/lift_and_drag.png"))
fig2.savefig(os.path.join(cwd, "output/skin_coeff_along_chord.png"))

plt.show()