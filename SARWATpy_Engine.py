import time

from subprocess import check_output


def callCalibration(paraProductName,paraOutPutDir):
      start_time = time.time()
      print(paraOutPutDir)
      test=check_output("gpt Calibration -Ssource='SARWAT_src\\" + paraProductName + "\\product.xml' -PsourceBands='Intensity_HH'  -t '" + paraOutPutDir + "\\" + paraProductName + "_cal.dim'", shell=True)
      elapsed_time = time.time() - start_time
      print(test)
      print("Calibration Completed... The execution time: " + str(elapsed_time))
      writeLogFile("Calibration for " + paraProductName + "  Completed... The execution time: " + str(elapsed_time))


def callCalibration_As_GEOTIFF(paraProductName,paraOutPutDir):
      start_time = time.time()
      test=check_output("gpt Calibration -Ssource='SARWAT_src\\" + paraProductName + "\\product.xml' -PsourceBands='Intensity_HH'  -t '" + paraOutPutDir + "\\" + paraProductName + "_cal.tif'  -f 'GeoTIFF'", shell=True)
      elapsed_time = time.time() - start_time
      print(test)
      print("Calibration Completed... The execution time: " + str(elapsed_time))
      writeLogFile("Calibration for " + paraProductName + "  Completed... The execution time: " + str(elapsed_time))



def callSpeckle_Filter(paraProductName,paraOutPutDir):
      start_time = time.time()
      test=check_output("gpt Speckle-Filter -Ssource='" + paraOutPutDir + "\\" + paraProductName + "_cal.dim' -Pfilter='Lee' -PfilterSizeX=11 -PfilterSizeY=11 -t '" + paraOutPutDir + "\\" + paraProductName + "_fil.dim'", shell=True)
      elapsed_time = time.time() - start_time
      print(test)
      print("Speckle-Filter Completed... The execution time: " + str(elapsed_time))
      writeLogFile("Speckle-Filter for " + paraProductName + "  Completed... The execution time: " + str(elapsed_time))

def callSpeckle_Filter_As_GEOTIFF(paraProductName,paraOutPutDir):
      start_time = time.time()
      test=check_output("gpt Speckle-Filter -Ssource='" + paraOutPutDir + "\\" + paraProductName + "_cal.dim' -Pfilter='Lee' -PfilterSizeX=11 -PfilterSizeY=11 -t '" + paraOutPutDir + "\\" + paraProductName + "_fil.tif'  -f 'GeoTIFF'", shell=True)
      elapsed_time = time.time() - start_time
      print(test)
      print("Speckle-Filter Completed... The execution time: " + str(elapsed_time))
      writeLogFile("Speckle-Filter for " + paraProductName + "  Completed... The execution time: " + str(elapsed_time))


def Terrain_Correction_on_filtered_SAR(paraProductName,paraOutPutDir,paraSARWATpy_ExternlDemPath):
      start_time = time.time()
      print("\n\n======================================\ngpt Terrain-Correction -Ssource='" + paraOutPutDir + "\\" + paraProductName + "_fil.dim' "
            + "-PapplyRadiometricNormalization=false -PoutputComplex=false -PpixelSpacingInMeter=5  -PsaveDEM=false -PsaveLocalIncidenceAngle=false "
            + "-PsaveSigmaNought=true -PmapProjection='EPSG:32611' -PexternalDEMFile='" + paraSARWATpy_ExternlDemPath + "' -PsourceBands='Sigma0_HH' "
            + "-PimgResamplingMethod='BILINEAR_INTERPOLATION' -t '" + paraOutPutDir + "\\" + paraProductName + "_ourtho.tif' -f 'GeoTIFF'\n====================\n\n")

      test=check_output("gpt Terrain-Correction -Ssource='" + paraOutPutDir + "\\" + paraProductName + "_fil.dim' "
                        + "-PapplyRadiometricNormalization=false -PoutputComplex=false -PpixelSpacingInMeter=5  -PsaveDEM=false "
                        + " -PsaveLocalIncidenceAngle=false -PsaveSigmaNought=true -PmapProjection='EPSG:32611' "
                        + "-PexternalDEMFile='" + paraSARWATpy_ExternlDemPath + "' -PsourceBands='Sigma0_HH' "
                        + "-PimgResamplingMethod='BILINEAR_INTERPOLATION' -t '" + paraOutPutDir + "\\" + paraProductName + "_ourtho.tif' "
                        +"-f 'GeoTIFF'", shell=True)
      #test=check_output("gpt Terrain-Correction -Ssource='" + paraOutPutDir + "\\" + paraProductName + "_fil.dim' -PapplyRadiometricNormalization=false -PoutputComplex=false -PpixelSpacingInMeter=5  -PsaveDEM=false -PsaveLocalIncidenceAngle=false -PsaveSigmaNought=true -PmapProjection='EPSG:32611' -PdemName='SRTM 3Sec' -PsourceBands='Sigma0_HH' -PimgResamplingMethod='BILINEAR_INTERPOLATION' -t '" + paraOutPutDir + "\\" + paraProductName + "_ourtho.tif' -f 'GeoTIFF'", shell=True)
      #test=check_output("gpt Terrain-Correction -Ssource='" + paraOutPutDir + "\\" + paraProductName + "_fil.dim' -PapplyRadiometricNormalization=false -PoutputComplex=false -PpixelSpacingInMeter=5  -PsaveDEM=false -PsaveLocalIncidenceAngle=false -PsaveSigmaNought=true -PmapProjection='EPSG:32612' -PexternalDEMFile='lidarDEM_ShepherS\SS_LiDAR_DEM_Mosaic.tif' -PsourceBands='Sigma0_HH' -PimgResamplingMethod='BILINEAR_INTERPOLATION' -t 'SARWAT_out\\" + paraProductName + "_ourtho.tif' -f 'GeoTIFF'", shell=True)
      elapsed_time = time.time() - start_time
      print(test)
      print("Terrain-Correction Completed... The execution time: " + str(elapsed_time))
      writeLogFile("Terrain-Correction for " + paraProductName + "  Completed... The execution time: " + str(elapsed_time))

def Terrain_Correction_on_caliborated_SAR(paraProductName,paraOutPutDir):
      start_time = time.time()
      test=check_output("gpt Terrain-Correction -Ssource='" + paraOutPutDir + "\\" + paraProductName + "_cal.dim' -PapplyRadiometricNormalization=false "
                        + "-PoutputComplex=false -PpixelSpacingInMeter=5  -PsaveDEM=false -PsaveLocalIncidenceAngle=false -PsaveSigmaNought=true "
                        + "-PmapProjection='EPSG:32611' -PdemName='SRTM 3Sec' -PsourceBands='Sigma0_HH' -PimgResamplingMethod='BILINEAR_INTERPOLATION' "
                        + "-t '" + paraOutPutDir + "\\" + paraProductName + "_ourtho.tif' -f 'GeoTIFF'", shell=True)
      #test=check_output("gpt Terrain-Correction -Ssource='" + paraOutPutDir + "\\" + paraProductName + "_fil.dim' -PapplyRadiometricNormalization=false -PoutputComplex=false -PpixelSpacingInMeter=5  -PsaveDEM=false -PsaveLocalIncidenceAngle=false -PsaveSigmaNought=true -PmapProjection='EPSG:32612' -PexternalDEMFile='lidarDEM_ShepherS\SS_LiDAR_DEM_Mosaic.tif' -PsourceBands='Sigma0_HH' -PimgResamplingMethod='BILINEAR_INTERPOLATION' -t '" + paraOutPutDir + "\\" + paraProductName + "_ourtho.tif' -f 'GeoTIFF'", shell=True)
      elapsed_time = time.time() - start_time
      print(test)
      print("Terrain-Correction Completed... The execution time: " + str(elapsed_time))
      writeLogFile("Terrain-Correction for " + paraProductName + "  Completed... The execution time: " + str(elapsed_time))

def GLCM(paraProductName,paraOutPutDir,paraSARWATpy_WindowSize):
      start_time = time.time()  ## -PnoDataValue=0.0 
      test=check_output("gpt GLCM -Ssource='" + paraOutPutDir + "\\" + paraProductName + "_ourtho.tif' " +
                        " -PoutputMAX=false -PoutputCorrelation=false -PoutputMean=false " +
                        " -PoutputVariance=false -PquantizationLevelsStr='32' -PwindowSizeStr='" + paraSARWATpy_WindowSize + "x" + paraSARWATpy_WindowSize + "' " +
                        " -PoutputDissimilarity=true -PoutputEntropy=false -PoutputHomogeneity=false " +
                        " -PoutputASM=false -PoutputEnergy=false -PsourceBands='Sigma0_HH' -PoutputContrast=false -t '"
                        + paraOutPutDir + "\\" + paraProductName + "_glcm.tif' -f 'GeoTIFF'", shell=True)
      #test=check_output("gpt GLCM -Ssource='" + paraOutPutDir + "\\" + paraProductName + "_ourtho.tif' -PoutputMAX=false -PoutputCorrelation=false -PoutputMean=false  -PoutputVariance=false -PquantizationLevelsStr='32' -PwindowSizeStr='11x11' -PoutputDissimilarity=true -PoutputEntropy=true -PoutputHomogeneity=false -PoutputASM=false -PoutputEnergy=false -PsourceBands='Sigma0_HH' -PoutputContrast=false -t '" + paraOutPutDir + "\\" + paraProductName + "_glcm.tif' -f 'GeoTIFF'", shell=True)
      elapsed_time = time.time() - start_time
      print(test)
      print("GLCM Completed... The execution time: " + str(elapsed_time))
      writeLogFile("GLCM for " + paraProductName + "  Completed... The execution time: " + str(elapsed_time))

def DissimilarityThreshhold(paraProductName,paraOutPutDir):
      start_time = time.time()
      #test=check_output("gpt GLCM -Ssource='ourtho.tif' -PoutputMAX=false -PoutputCorrelation=true -PoutputMean=true  -PoutputVariance=true -PquantizationLevelsStr='32' -PwindowSizeStr='7x7' -PoutputDissimilarity=true -PoutputEntropy=false -PsourceBands='Sigma0_HH' -PoutputContrast=true -t 'glcm.tif' -f 'GeoTIFF'", shell=True)
      elapsed_time = time.time() - start_time
      #print(test)
      print("Sorry this feature is not implemented yet...")
      print("Dissimilarity Threshhold Completed... The execution time: " + str(elapsed_time))
      writeLogFile("Dissimilarity Threshhold for " + paraProductName + "  Completed... The execution time: " + str(elapsed_time))




def generate_SARWATpy_BandMathXMLFile(paraFileName,paraFormula,paraNewlyCreatedPandName):
      SARWATpy_BandMathXMLFile=open(paraFileName + ".xml","w")

      SARWATpy_BandMathXMLFile.write("  <graph id=\"someGraphId\">\n")
      SARWATpy_BandMathXMLFile.write("    <version>1.0</version>\n")
      SARWATpy_BandMathXMLFile.write("    <node id=\"someNodeId\">\n")
      SARWATpy_BandMathXMLFile.write("      <operator>BandMaths</operator>\n")
      SARWATpy_BandMathXMLFile.write("      <sources>\n")
      SARWATpy_BandMathXMLFile.write("        <sourceProducts>${sourceProducts}</sourceProducts>\n")
      SARWATpy_BandMathXMLFile.write("      </sources>\n")
      SARWATpy_BandMathXMLFile.write("      <parameters>\n")
      SARWATpy_BandMathXMLFile.write("        <targetBands>\n")
      SARWATpy_BandMathXMLFile.write("          <targetBand>\n")
      SARWATpy_BandMathXMLFile.write("            <name>" + paraNewlyCreatedPandName + "</name>\n")
      SARWATpy_BandMathXMLFile.write("            <type>Float32</type>\n")
      SARWATpy_BandMathXMLFile.write("            <expression>" + paraFormula + "</expression>\n")
      SARWATpy_BandMathXMLFile.write("            <description>test</description>\n")
      SARWATpy_BandMathXMLFile.write("	    <NoDataValueUsed>true</NoDataValueUsed>\n")
      SARWATpy_BandMathXMLFile.write("            <noDataValue>0.0</noDataValue>\n")
      SARWATpy_BandMathXMLFile.write("          </targetBand>\n")
      SARWATpy_BandMathXMLFile.write("        </targetBands>\n")
      SARWATpy_BandMathXMLFile.write("      </parameters>\n")
      SARWATpy_BandMathXMLFile.write("    </node>\n")
      SARWATpy_BandMathXMLFile.write("  </graph>\n")

      SARWATpy_BandMathXMLFile.close()


def BandMaths(paraProductName,paraOutPutDir,paraFileName):
      print(paraOutPutDir + "\\" + paraProductName + "_BMATH.tif ")
      #print(os.getcwd())
      start_time = time.time()
      test=check_output("gpt " + paraFileName + ".xml  -t " + paraOutPutDir + "\\" + paraProductName + "_BMATH.tif " + paraOutPutDir + "\\" + paraProductName + "_glcm.tif", shell=True)
      elapsed_time = time.time() - start_time
      print(test)
      print("GLCM Completed... The execution time: " + str(elapsed_time))
      writeLogFile("GLCM for " + paraProductName + "  Completed... The execution time: " + str(elapsed_time))


def writeLogFile(paraMesage):
      logFile = open("log.txt", "a")
      logFile.write(paraMesage + "\n")
      logFile.close()


