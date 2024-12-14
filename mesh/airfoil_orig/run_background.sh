#!/bin/bash

# Clean previous tutorial cases
foamCleanTutorials
cp -r 0.orig 0
rm -r constant/polyMesh
rm -r constant/extendedFeatureEdgeMesh
# Generate the initial mesh
blockMesh

surfaceFeatureExtract
# Decompose the domain for parallel processing
decomposePar

foamJob -s -p snappyHexMesh -dict system/snappyHexMeshDict_first -parallel -overwrite
# Generate the mesh using snappyHexMesh in parallel, overwrite existing files, and log output
#mpirun -np 8 snappyHexMesh -dict system/snappyHexMeshDict_first -overwrite | tee log.shm1

# Reconstruct the mesh after parallel processing
reconstructParMesh -constant

# Extrude the mesh (if needed)
extrudeMesh -noFunctionObjects

touch para.foam
checkMesh -latestTime | tee log.checkmesh3D_1
rm -r processor*

rm constant/polyMesh/cellLevel
rm constant/polyMesh/pointLevel
rm constant/polyMesh/level0Edge

rm -rf 0


decomposePar

foamJob -s -p snappyHexMesh -dict system/snappyHexMeshDict_second -parallel -overwrite
reconstructParMesh -constant
extrudeMesh -noFunctionObjects
checkMesh -latestTime | tee log.checkmesh3D_2

rm -r processor*

rm constant/polyMesh/cellLevel
rm constant/polyMesh/pointLevel
rm constant/polyMesh/level0Edge

rm -rf 0


decomposePar

foamJob -s -p snappyHexMesh -dict system/snappyHexMeshDict_third -parallel -overwrite
reconstructParMesh -constant
extrudeMesh -noFunctionObjects
checkMesh -latestTime | tee log.checkmesh3D_3

rm -r processor*

rm constant/polyMesh/cellLevel
rm constant/polyMesh/pointLevel
rm constant/polyMesh/level0Edge

rm -rf 0


decomposePar

foamJob -s -p snappyHexMesh -dict system/snappyHexMeshDict_third_2 -parallel -overwrite
reconstructParMesh -constant
extrudeMesh -noFunctionObjects
checkMesh -latestTime | tee log.checkmesh3D_3_2

rm -r processor*

rm constant/polyMesh/cellLevel
rm constant/polyMesh/pointLevel
rm constant/polyMesh/level0Edge

rm -rf 0


decomposePar

foamJob -s -p snappyHexMesh -dict system/snappyHexMeshDict_fourth -parallel -overwrite
reconstructParMesh -constant
extrudeMesh -noFunctionObjects
checkMesh -latestTime | tee log.checkmesh3D_4

rm -r processor*

rm constant/polyMesh/cellLevel
rm constant/polyMesh/pointLevel
rm constant/polyMesh/level0Edge

rm -rf 0

