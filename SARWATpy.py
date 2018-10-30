# SARWATpy© is an open source python code designed by ARTEMIS Lab at the University of Lethbridge, AB, Canada in 2016. The objective is to build an automated Radarsat-2 data processing to extract the surface water bodies.
import os
import sys

import SARWATpy_Engine
from SARWATpy_Engine import *


def getSARWATpySystemChoice():
    ARTeMiS_SystemChoice=input('''
    ========================================================================
                           Welcome to SARWATpy Engine 

                   "SAR Water Assessment Tool python" for 
             SAR data Processing and Surface Water Body Extraction 
    ========================================================================
    \n
    Please select the processing interface (CLI by Default): 
    1- CLI                  2- SNAPPY
    ''')    
    
    if(ARTeMiS_SystemChoice==1):
        return getSARWATpyStandard()
    elif (ARTeMiS_SystemChoice==2):
        return getSARWATpyActions()
    else:
        print("The selection you choose is not supported...")

def getSARWATpyStandard():
    ARTeMiS_Base=input('''
                            SARWATpy routine:
    ========================================================================
    Please select your threshholing approach: 
    1- Texture-based       2- ONLY Orthorectification       3- External Product
    ''')    
    
    if(ARTeMiS_Base==1):
        return getSARWATpyGPTActions_TextureBased()
    elif (ARTeMiS_Base==2):
        return getSARWATpyGPTActions_dbBased()
    elif (ARTeMiS_Base==3):
        return getSARWATpyGPTActions_General()
    else:
        print("The selection you choose is not supported...")    




def getSARWATpyGPTActions_TextureBased():
    
    ARTeMiS_Action=input('''
                                Key SAR Processing Steps (Texture-Based)
                                --------------------------------------------
    1- SAR Radiometric Calibration (Cal): (SNAP Standard Format .dim, sigma0- based)
    2- Speckle Filtering (LEE): (Optional)
    3- GLCM 
    4- Water Mask Extraction
    5- Orthorectification (.geotif)

    ===============================================================================
                                    Batch Processing 
    ===============================================================================
    6- --- Steps 1 .. 5
    7- --- Steps 1,3,4,5
     ''')

    print("\n***********************************************************\n")

    #lclARTeMiS_Actions={'ARTeMiSOrtho':False,'ARTeMiSGLCM':False,'ARTeMiSEntropyThreshhold':False}
    lclARTeMiS_Actions={}
    lclARTeMiS_Actions['ARTeMiS_Interface']="gpt"    
    lclARTeMiS_Actions['ARTeMiS_Caliboration']=False
    lclARTeMiS_Actions['ARTeMiS_Filtering']=False
    lclARTeMiS_Actions['ARTeMiS_Orthorectification_on_filtered_SAR']=False
    lclARTeMiS_Actions['ARTeMiS_Orthorectification_on_caliborated_SAR']=False
    lclARTeMiS_Actions['ARTeMiS_GLCM']=False
    lclARTeMiS_Actions['ARTeMiS_EntropyThreshhold']=False
    lclARTeMiS_Actions['ARTeMiS_Vectorization']=False

    lclARTeMiS_Actions['ARTeMiS_Caliboration_As_GEOTIFF']=False
    lclARTeMiS_Actions['ARTeMiS_Speckle_Filter_As_GEOTIFF']=False
    lclARTeMiS_Actions['ARTeMiS_BandMaths_As_GEOTIFF']=False    
    
    if(ARTeMiS_Action==1 or ARTeMiS_Action==15 or (ARTeMiS_Action>6 and ARTeMiS_Action<14)):
        ARTeMiS_Caliboration=True;
        lclARTeMiS_Actions['ARTeMiS_Caliboration']=True

    if(ARTeMiS_Action==2 or ARTeMiS_Action==7 or ARTeMiS_Action==8 or ARTeMiS_Action==10 or ARTeMiS_Action==12):
        ARTeMiS_Filtering=True;
        lclARTeMiS_Actions['ARTeMiS_Filtering']=True

    if(ARTeMiS_Action==3 or ARTeMiS_Action==8 or ARTeMiS_Action==10 or ARTeMiS_Action==12):
        ARTeMiS_Orthorectification=True;
        lclARTeMiS_Actions['ARTeMiS_Orthorectification_on_filtered_SAR']=True

    if(ARTeMiS_Action==4 or ARTeMiS_Action==9 or ARTeMiS_Action==9 or ARTeMiS_Action==11 or ARTeMiS_Action==13):
        ARTeMiS_Orthorectification=True;
        lclARTeMiS_Actions['ARTeMiS_Orthorectification_on_caliborated_SAR']=True
    if(ARTeMiS_Action==5 or (ARTeMiS_Action>9 and ARTeMiS_Action<14)):
        ARTeMiS_GLCM=True;
        lclARTeMiS_Actions['ARTeMiS_GLCM']=True

    if(ARTeMiS_Action==6 or ARTeMiS_Action==12 or ARTeMiS_Action==13):
        ARTeMiS_EntropyThreshhold=True;
        lclARTeMiS_Actions['ARTeMiS_EntropyThreshhold']=True

    if(ARTeMiS_Action==14):
        ARTeMiS_EntropyThreshhold=True;
        lclARTeMiS_Actions['ARTeMiS_Caliboration_As_GEOTIFF']=True

    if(ARTeMiS_Action==15):
        ARTeMiS_EntropyThreshhold=True;
        lclARTeMiS_Actions['ARTeMiS_Speckle_Filter_As_GEOTIFF']=True

    if(ARTeMiS_Action==16):
        ARTeMiS_EntropyThreshhold=True;
        lclARTeMiS_Actions['ARTeMiS_BandMaths_As_GEOTIFF']=True
        

    print(lclARTeMiS_Actions)
    return lclARTeMiS_Actions


                              
