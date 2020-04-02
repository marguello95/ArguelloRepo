import os
import arcpy

arcpy.env.overwriteOutput = True
arcpy.CheckOutExtension("Spatial")

listMonths = ["02", "04", "05", "07", "10", "11"]
outputDirectory = r"G:/Week_7/Step_3_data_lfs/NVDI_Outputs"
if not os.path.exists(outputDirectory):
    os.mkdir(outputDirectory)


for months in listMonths:
    arcpy.env.workspace = r"G:/Week_7/Step_3_data_lfs/2015" + months
    print "Extracting Bands..."
    print "G:/Week_7/Step_3_data_lfs/2015" + months
    band4 = arcpy.ListRasters("*", "TIF")
    band4 = [x for x in band4 if "B4" in x]
    print "The file for Band 4 is " + str(band4) + "."
    band5 = arcpy.ListRasters("*", "TIF")
    band5 = [x for x in band5 if "B5" in x]
    print "The file for Band 5 is " + str(band5) + "."
    arcpy.gp.RasterCalculator_sa('Float("' + band5[0] + '"-"' + band4[0] + '") / Float("' + band5[0] + '"+"' + band4[0] + '")',
                                 os.path.join(outputDirectory, "NVDI_2015" + months + ".tif"))

print "Process Completed!"
