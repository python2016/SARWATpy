# SARWATpy© is an open source python code designed by ARTEMIS Lab at the University of Lethbridge, AB, Canada in 2016. The objective is to build an automated Radarsat-2 data processing to extract the surface water bodies.
import os
import sys

import SARWATpy_Engine
from SARWATpy_Engine import *


def getSARWATpySystemChoice():
    ARTeMiS_SystemChoice=input('''
    ========================================================================
                          Welcome to SARWATpy Engine

                          This is an Open Source product
                for SAR data processing and water mask extraction
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
    1- Texture-based       2- db-based       3- External Product
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
    # 6- Vectorization for water mask polygons
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
        

##    if(ARTeMiS_Action==6 or ARTeMiS_Action==11):
##        ARTeMiS_Vectorization=True;
##        lclARTeMiS_Actions['ARTeMiS_Vectorization']=True
        
    print(lclARTeMiS_Actions)
    return lclARTeMiS_Actions


def getSARWATpyGPTActions_dbBased():
    
    ARTeMiS_Action=input('''

                                Key SAR Processing Steps (db-Based)
                                --------------------------------------------
    1- SAR Radiometric Calibration (Cal)(SNAP Standard Format .dim, sigma0- based)
    2- Speckle Filtering (LEE) (Optional Step)
    3- db-backscatter
    4- Water Mask Extraction
    5- Orthorectification (.geotif)

    ===============================================================================
                                    Batch Processing 
    ===============================================================================
    6- --- Steps 1 .. 5
    7- --- Steps 1,3,4,5

    ''')
    # 6- Vectorization for water mask polygons
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
        

##    if(ARTeMiS_Action==6 or ARTeMiS_Action==11):
##        ARTeMiS_Vectorization=True;
##        lclARTeMiS_Actions['ARTeMiS_Vectorization']=True
        
    print(lclARTeMiS_Actions)
    return lclARTeMiS_Actions





def getSARWATpyGPTActions_General():
    
    ARTeMiS_Action=input('''
    (SNAP Standard Format .dim, sigma0- based)
    
                                            Filtered
                                --------------------------------------
    
    1- SAR Radiometric Calibration (Cal) Filtered 
    2- Orthorectification (.geotif)

    Batch Processing 
    =================
    3- --- Steps 1 .. 2

                                            Not Filtered
                                --------------------------------------
    4- SAR Radiometric Calibration (Cal)
    5- Orthorectification (.geotif)
    
    Batch Processing 
    =================
    6- --- Steps 4 .. 5
    ''')


##    
##
##
##
##
##
##    ===============================================================================
##                                    Miscellaneous Processes 
##    ===============================================================================
##
##    3- Orthorectification on calibrated & filtered product ONLY
##    4- Orthorectification on calibrated product ONLY  (Not Filtered)
##    
##                                     Complementary Steps
##                                ------------------------------
##    5- GLCM texture analysis on Orthorectified ONLY
##    6- Water Threshold based on our selected texture band (dissimilarity, entropy ...) ONLY
##    
##    ===============================================================================
##    A sequqnce of operations
##    ===============================================================================
##    7-  ---- Steps 1 & 2        ( in a sequential order)
##    8-  ---- Steps 1,2 & 3      ( in a sequential order)
##    9-  ---- Steps 1 & 4       ( in a sequential order)
##    10- ---- Steps 1,2,3 & 5    ( in a sequential order)
##    11- ---- Steps 1,4 & 5      ( in a sequential order)
##    12- ---- Steps 1,2,3,5 & 6  ( in a sequential order)
##    13- ---- Steps 1,4,5 & 6    ( in a sequential order)
##    ===============================================================================
##    Other Option for the output format 
##    ===============================================================================
##    14- SAR Radiometric Calibration (sigma0) ONLY  as GEOTIFF
##    15- LEE Filtering on calibrated product  ONLY  as GEOTIFF
##    16- BandMaths on GLCM with segma0_dissimilarity band as GEOTIFF 
##
##
##    2- Filtering on Cal product ONLY (LEE Filter)
##
##    GLCM texture analysis on the Filtered SAR
##
##    ===============================================================================
##    External Product 
##    ===============================================================================
##    3- Orthorectification on calibrated & filtered product ONLY
##    4- Orthorectification on calibrated product ONLY  (Not Filtered)
    
    # 6- Vectorization for water mask polygons
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
        

##    if(ARTeMiS_Action==6 or ARTeMiS_Action==11):
##        ARTeMiS_Vectorization=True;
##        lclARTeMiS_Actions['ARTeMiS_Vectorization']=True
        
    print(lclARTeMiS_Actions)
    return lclARTeMiS_Actions




def createOutPutFolder(paraOutPutFolder):
    try: 
        os.makedirs(paraOutPutFolder)
    except OSError:
        print("Fail to create folder, it could be already exist....")



def get_ContainerDirectory_subdirectories(paraContainerDir):
    return [name for name in os.listdir(paraContainerDir)
            if os.path.isdir(os.path.join(paraContainerDir, name))]


def processFolders(paraSourceContainerDir,paraOutPutDir,paraARTeMiS_Config
                   ,paraSARWATpy_ExternlDemPath,paraSARWATpy_WindowSize
                   ,paraSARWATpy_WaterMaskFormula,paraSARWATpy_NewBandName):
      myFolderList=get_ContainerDirectory_subdirectories(paraSourceContainerDir)
      for lclFolder in myFolderList:
          lclOutPutFolder=paraOutPutDir + "\\"  + lclFolder + "_Out" 
          createOutPutFolder(lclOutPutFolder)
          print (os.getcwd())
          if(paraARTeMiS_Config['ARTeMiS_Caliboration']==True):
              callCalibration(lclFolder,lclOutPutFolder)
          if(paraARTeMiS_Config['ARTeMiS_Filtering']==True):
              callSpeckle_Filter(lclFolder,lclOutPutFolder)
          if(paraARTeMiS_Config['ARTeMiS_Orthorectification_on_filtered_SAR']==True):
              Terrain_Correction_on_filtered_SAR(lclFolder,lclOutPutFolder,paraSARWATpy_ExternlDemPath)
          if(paraARTeMiS_Config['ARTeMiS_Orthorectification_on_caliborated_SAR']==True):
              Terrain_Correction_on_caliborated_SAR(lclFolder,lclOutPutFolder)              
          if(paraARTeMiS_Config['ARTeMiS_GLCM']==True):
              GLCM(lclFolder,lclOutPutFolder,paraSARWATpy_WindowSize)
          if(paraARTeMiS_Config['ARTeMiS_EntropyThreshhold']==True):
              EntropyThreshhold(lclFolder,lclOutPutFolder)
          if(paraARTeMiS_Config['ARTeMiS_Vectorization']==True):
              Vectorization(lclFolder,lclOutPutFolder)
          if(paraARTeMiS_Config['ARTeMiS_Caliboration_As_GEOTIFF']==True):
              callCalibration_As_GEOTIFF(lclFolder,lclOutPutFolder)
          if(paraARTeMiS_Config['ARTeMiS_Speckle_Filter_As_GEOTIFF']==True):
              callSpeckle_Filter_As_GEOTIFF(lclFolder,lclOutPutFolder)
          if(paraARTeMiS_Config['ARTeMiS_BandMaths_As_GEOTIFF']==True):
              generate_SARWATpy_BandMathXMLFile(lclFolder
                                                ,paraSARWATpy_WaterMaskFormula
                                                ,paraSARWATpy_NewBandName)
              BandMaths(lclFolder,lclOutPutFolder,lclFolder)




##========================== Old ====================================================================##
def getSARWATpyActions():
    
    ARTeMiS_Action=input('''
    \n
    Please select the process you want to perform: \n
    1- SAR Radiometric Caliboration & Orthorectification ONLY
    2- GLCM texture analysis ONLY
    3- ---- Steps 1 & 2 
    4- Water Threshhold based on our selected texture band (dissimilarity, entropy ...) ONLY
    5- ---- Steps 2 & 4
    6- ---- Stepts 1,2 & 4
    7- Vectorization for water mask polygons
    8- ---- Steps 1,2,4 & 7
    ''')

    print("\n***********************************************************\n")

    #lclARTeMiS_Actions={'ARTeMiSOrtho':False,'ARTeMiSGLCM':False,'ARTeMiSEntropyThreshhold':False}
    lclARTeMiS_Actions={}
    lclARTeMiS_Actions['ARTeMiS_Interface']="snappy" 
    lclARTeMiS_Actions['ARTeMiS_Orthorectification_on_filtered_SAR']=False
    lclARTeMiS_Actions['ARTeMiS_Orthorectification_on_caliborated_SAR']=False
    lclARTeMiS_Actions['ARTeMiSGLCM']=False
    lclARTeMiS_Actions['ARTeMiSEntropyThreshhold']=False
    
    if(ARTeMiS_Action==1 or ARTeMiS_Action==3 or ARTeMiS_Action==6):
        ARTeMiSOrtho=True;
        lclARTeMiS_Actions['ARTeMiSOrtho']=True
        
    if(ARTeMiS_Action==2 or ARTeMiS_Action==3 or ARTeMiS_Action==6 or ARTeMiS_Action==5):
        ARTeMiSGLCM=True;
        lclARTeMiS_Actions['ARTeMiSGLCM']=True
        
    if(ARTeMiS_Action==4 or ARTeMiS_Action==5 or ARTeMiS_Action==6):
        ARTeMiSEntropyThreshhold=True;
        lclARTeMiS_Actions['ARTeMiSEntropyThreshhold']=True
    print(lclARTeMiS_Actions)
    return lclARTeMiS_Actions              
