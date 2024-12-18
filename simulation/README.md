## Simulation Setup
This folder contains the files necessary to carry out the shock buffet simulation of OAT15 airfoil.
The steps to execute the setup are as follows:
1. Copy the mesh files ("polyMesh") from the "mesh" folder into the "constant" folder of the current directory.
2. To execute the CFD simulation, run the "Allrun" script using
```
./Allrun
```
3. To generate plots for Skin friction and pressure coefficient, run the plotter.py script
```
python3 plotter.py
```