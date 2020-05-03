#The created code will take inputs from 2 choosen shape files, the function will then:
#1.) Describes the shape type for each of the 2 shapefile that were used as the input from the data source
#2.) Create a shape file with a 100 meter buffer for each of the 2 shape files

import arcpy
arcpy.env.overwriteOutput = True

#Setting workspace for files occur and outputs will be exported to
arcpy.env.workspace = r"G:\Week_10\CC_8_A"
workspace = arcpy.env.workspace #Sets workspace as a variable that can be used in code/helps limit changes needed to be made by user

#Create an output folder for the results to be stored
arcpy.CreateFolder_management(workspace, "results")

#creating the function that will be used to buffer the each of shapefiles that will be input
def Buff_Des_shp(input_Shapefile,input_Shapefile2): #Represents each of the 2 inputs that this function will accept

#This section of the code addresses the first task (Task #1)
# It prints out a description of the shape type of each input shapefile (i.e. point, polygon and polyline)
    desc = arcpy.Describe(input_Shapefile)
    desc2 = arcpy.Describe(input_Shapefile2)
    print "Input shapefile #1 shape type is: " + str(desc.shapeType)
    print "Input shapefile #2 shape type is: " + str(desc2.shapeType)

    print "Now Creating Buffers..."

#This section of the code addresses Task #2 - Creates a 100 meter buffer for each input shapefile
#Setting up buffer inputs for first input shapefile
    in_features = input_Shapefile #Where the first input shapefile will be input into the buffer function
    out_feature_class = "results\Buffer_Output_Shpfile_1.shp" #Creates third output shape file
    buffer_distance_or_field = "100 meter"
    line_side = "#"
    line_end_type = "#"
    dissolve_option = "#"
    dissolve_field = "#"
    method = "GEODESIC"
    arcpy.Buffer_analysis(in_features, out_feature_class, buffer_distance_or_field, line_side, line_end_type,
                          dissolve_option, dissolve_field, method)

#Sets up buffer inputs for second input shapefile
    in_features = input_Shapefile2 #Where the second input shapefile will be input into the buffer function
    out_feature_class = "results\Buffer_Output_Shpfile_2.shp" #Creates second output shape file
    buffer_distance_or_field = "100 meter"
    line_side = "#"
    line_end_type = "#"
    dissolve_option = "#"
    dissolve_field = "#"
    method = "GEODESIC"
    arcpy.Buffer_analysis(in_features, out_feature_class, buffer_distance_or_field, line_side, line_end_type,
                          dissolve_option, dissolve_field, method)

    print "Buffer Tool Completed for both shapefiles! - See results folder for created buffer outputs!"


#Entering files that are going to be input
#This is where file inputs be changed here to whatever shapefile you would like to run
input_shapefile = "Lakes.shp" #Lakes in Rhode Island
input_shapefile2 = "Rivers.shp" #Rivers in Rhode Island

#Running the created funtion with example data defined above
Buff_Des_shp(input_shapefile, input_shapefile2)
