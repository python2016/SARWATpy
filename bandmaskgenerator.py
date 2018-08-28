# SARWATpy© is an open source python code designed by ARTEMIS Lab at the University of Lethbridge, AB, Canada in 2016. The objective is to build an automated Radarsat-2 data processing to extract the surface water bodies.


def generate_SARWATpy_BandMathXMLFile(paraFileName):
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
      SARWATpy_BandMathXMLFile.write("            <name>sam_0</name>\n")
      SARWATpy_BandMathXMLFile.write("            <type>Float32</type>\n")
      SARWATpy_BandMathXMLFile.write("            <expression>if(isNaN(Sigma0_HH_Dissimilarity)) then 0.0 else 1.0</expression>\n")
      SARWATpy_BandMathXMLFile.write("            <description>test</description>\n")
      SARWATpy_BandMathXMLFile.write("	    <NoDataValueUsed>true</NoDataValueUsed>\n")
      SARWATpy_BandMathXMLFile.write("            <noDataValue>0.0</noDataValue>\n")
      SARWATpy_BandMathXMLFile.write("          </targetBand>\n")
      SARWATpy_BandMathXMLFile.write("        </targetBands>\n")
      SARWATpy_BandMathXMLFile.write("      </parameters>\n")
      SARWATpy_BandMathXMLFile.write("    </node>\n")
      SARWATpy_BandMathXMLFile.write("  </graph>\n")

      SARWATpy_BandMathXMLFile.close()
