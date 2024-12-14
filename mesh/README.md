## Mesh Generator

This folder contains the neccessary files to generate the mesh for OAT15 airfoil using snappyHexMesh. 
The mesh generation is done in two steps using two different scripts.
The first script generates the mesh upto snapping stage (no boundary layer) and the second script uses this mesh and creates a boundary layer on it.
This is done to adjust the firstLayerThickness of the mesh, to reduce the y+ value.

The steps to generate the mesh are as follows:

1. The mesh upto the snapping stage is generated in the "airfoil_orig" folder. Go into this folder.
```
cd airfoil_orig
```
2. Copy the stl file of OAT15 airfoil geometry into "constant/triSurface". The file should be named as "airfoil.stl".
3. From the top level of this folder run the "run_background.sh" script using
```
sh run_background.sh
```
The mesh can be cleared using
```
sh AllClean.sh
```
4. The mesh is now generated. The snappyHexMesh is done in multiple steps to save memory, the log file of each step is made.
5. To generate the boundary layer run the second script, which is in the top level of the "mesh" folder. 
```
cd ..
sh run_bl.sh
```
6. The mesh with boundary layer is created in a folder called "airfoil_with_bl". The parameters for the boundary layer like "firstLayerThickness" can be changed in the file "airfoil_orig/system/snappyHexMeshDict_fifth". After changing the parameter value, remove the folder already present, then run the script again.
```
rm -r airfoil_with_bl
sh run_bl.sh
```



