#Title: Extracting hiking trails that occur within South Kingstown, Rhode Island
#Created By: Michael Arguello

#Code Summary:
#First, uses Rhode Island Municipality boundaries data and using the select tool selects South Kingstown as a seperate shape file.

#Second, uses the created south kingstown boundary (South_Kingstown_Boundary.shp) to clip all hiking trails (hikeTrails15.shp)
#within south kingstown and outputs final product(Trails_In_South_Kingstown.shp) in the results folder.

#Import Arcpy and allow files to overwrite if same file name already exists in workspace
import arcpy
arcpy.env.overwriteOutput = True

#Set Workspace (ONLY PLACE THAT NEEDS TO BE CHANGED USER TO USER) - Location where files located on computer
arcpy.env.workspace = r"G:\py_mid" #Workplace for all my files for this project on my computer
workspace = arcpy.env.workspace #Sets workspace as a variable that can be used in code/helps limit changes needed to be made by user

#Create an output folder for the results to be stored
arcpy.CreateFolder_management(workspace, "results")

print "Executing clip tool..."

#Input Features for select tool to select south kingstown from Municipality boundaries
in_features = "muni89.shp"
out_feature_class = "results\South_Kingstown_Boundary.shp"
where_clause = "NAME = 'SOUTH KINGSTOWN'" #Can easily be changed to any other district other than South Kingstown by changing here
#Code that Runs Select Tool/output will be South Kingstown boundary only
arcpy.Select_analysis(in_features, out_feature_class, where_clause)

#Set local variables to be used in clip tool
#The code below will clip the hiking trails that fall within the South Kingstown Boundary
in_features = "hikeTrails15.shp"
clip_features = "results\South_Kingstown_Boundary.shp"
out_feature_class = "results\Trails_In_South_Kingstown.shp"
xy_tolerance = "#"

#Code to run the clip tool with all the given inputs above/output will be hiking trails
arcpy.Clip_analysis(in_features, clip_features, out_feature_class, xy_tolerance)

#Delete Intermediate Data (South Kingstown Boundary shape file) from results folder
arcpy.Delete_management("results\South_Kingstown_Boundary.shp", "")

print "The clip tool has run successfully!" #Lets user know that the clip tool has run successfully
print "Shapefile displaying hiking trails within South Kingstown has been created! - See results folder "
