#!/bin/bash
. ${WM_PROJECT_DIR:?}/bin/tools/RunFunctions        # Tutorial run functions
# Clean previous tutorial cases
rm -r airfoil_with_bl
cp -r airfoil_orig airfoil_with_bl
{
cd airfoil_with_bl || exit
decomposePar

foamJob -s -p snappyHexMesh -dict system/snappyHexMeshDict_fifth -parallel -overwrite
reconstructParMesh -constant
extrudeMesh -noFunctionObjects
checkMesh -latestTime | tee log.checkmesh3D_5
runApplication createPatch -overwrite
}
