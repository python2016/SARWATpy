# SARWATpy© is an open source python code designed by ARTEMIS Lab at the University of Lethbridge, AB, Canada in 2016. The objective is to build an automated Radarsat-2 data processing to extract the surface water bodies.
import sys
sys.path.append('SARWATpy')
import SARWATpy
from SARWATpy import *



#===========================   Change Container Foldr    ===========
ARTeMiS_SourceContainerDir="SARWATpy_src"  # this is for looping via folders
ARTeMiS_OutputContainerDir="SARWAT_out"
#===================================================================

SARWATpy_ExternlDemPath="LIDAR_DEM.tif"
SARWATpy_GLCMWindowSize="7"   ## example 11x11 type 11, 7x7 type 7
SARWATpy_WaterMaskFormula="if(isNaN(Sigma0_HH_Dissimilarity)) then 0.0 else 1.0"
SARWATpy_NewBandName="SARWATpy_Band_1"
 
ARTeMiS_Config=getSARWATpySystemChoice()

processFolders(ARTeMiS_SourceContainerDir,ARTeMiS_OutputContainerDir
               ,ARTeMiS_Config,SARWATpy_ExternlDemPath
               ,SARWATpy_GLCMWindowSize,SARWATpy_WaterMaskFormula
               ,SARWATpy_NewBandName)
