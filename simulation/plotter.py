import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#from utils import average_surface_data
import os

#mpl.rcParams['figure.dpi'] = 160
#mpl.rc('text', usetex=True)


os.makedirs("output", exist_ok = True)
# free stream Mach number based on chord
MA_INF = 0.72
# free stream velocity in m/s
U_INF = 246.96
# free stream speed of sound in m/s
A_INF = U_INF / MA_INF
# chord length
CHORD = 0.15
RHO_INF = 1.186
fig, ax = plt.subplots(figsize=(7, 5))
fig1, ax1 = plt.subplots(figsize=(7, 5))

path = os.getcwd() + "/postProcessing/surface/"
time_li = os.listdir(path)
time_win = [0.0001, 10]
time_li.sort(key=float)
filtered_time_li = list(filter(lambda x: float(x)>= time_win[0] and float(x)<= time_win[1], time_li))
print(filtered_time_li)
cp_file = os.path.join(path, filtered_time_li[0], "total(p)_coeff_airfoil.raw")
cols = ["x", "y", "z", "Cp"]
df = pd.read_csv(cp_file, delimiter=" ", header=None, skiprows=2, names=cols)
cp_avg = np.zeros(df.shape[0])
cf_avg = np.zeros(df.shape[0])
#fig, ax = plt.subplots()
for time in filtered_time_li:
    cp_file = os.path.join(path, time, "total(p)_coeff_airfoil.raw")
    cf_file = os.path.join(path, time, "wallShearStress_airfoil.raw")

    cols_cp = ["x", "y", "z", "Cp"]
    cols_cf = ["x", "y", "z", "tau_x", "tau_y", "tau_z"]
    df_cp = pd.read_csv(cp_file, delimiter=" ", header=None, skiprows=2, names=cols_cp)
    df_cf = pd.read_csv(cf_file, delimiter=" ", header=None, skiprows=2, names=cols_cf)
    cp_avg = cp_avg + np.array(df["Cp"])
    cf_avg = cf_avg + np.sqrt(df_cf['tau_x']**2 + df_cf['tau_y']**2 + df_cf['tau_z']**2)

cp_avg /= len(filtered_time_li)
cf_avg /= len(filtered_time_li)
cf_avg /= 0.5*RHO_INF*U_INF*U_INF
ax.scatter(df_cp["x"]/0.15, cp_avg)
ax.set_title("Variation of pressure coefficient along chord")
ax.set_xlabel(r"$x/c$")
ax.set_ylabel(r"$C_{p}$")
fig.savefig("./output/pressure_coeff_along_chord")
        
ax1.scatter(df_cp["x"]/0.15, cf_avg)
ax1.set_title("Variation of skin friction coefficient along chord")
ax1.set_xlabel(r"$x/c$")
ax1.set_ylabel(r"$C_{f}$")
fig1.savefig("./output/skin_coeff_along_chord")


plt.show()