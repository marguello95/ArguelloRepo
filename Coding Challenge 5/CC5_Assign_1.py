import arcpy
import csv

arcpy.env.overwriteOutput = True

# Set  workspace
arcpy.env.workspace = r"G:\Week_6_CC" #Workplace for all my files for this project on my computer



in_Table = r"Apogon.csv"
x_coords = "decLat"
y_coords = "decLong"
z_coords = ""
out_Layer = "Apogon"
saved_Layer = r"Apong_Specie.shp"


# Sets the spatial reference
spRef = arcpy.SpatialReference(4326)

lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)

# Displays the total number of rows in the shape file
print (arcpy.GetCount_management(out_Layer))

# saves the created layer file
arcpy.CopyFeatures_management(lyr, saved_Layer)

#prints sucessful completion of shape file
if arcpy.Exists(saved_Layer):
    print "Created file successfully!"

#Extracting and printing the extent of the data file
desc = arcpy.Describe(saved_Layer)

XMin = desc.extent.XMin
XMax = desc.extent.XMax
YMin = desc.extent.YMin
YMax = desc.extent.YMax

#prints the extent
print ("Extent:\n  XMin: {0},\n XMax: {1}".format(desc.extent.XMin, desc.extent.XMax))
print ("Extent:\n  YMin: {0},\n YMax: {1}".format(desc.extent.YMin, desc.extent.YMax))

#Creating fishnet file using the extent found above

outFeatureClass = "Fishnet_Apogon.shp"
originCoordinate = str(XMin) + " " + str(YMin)
yAxisCoordinate = str(XMin) + " " + str(YMin + 1.0)
cellSizeWidth = "0.25"
cellSizeHeight = "0.25"
numRows = ""
numColumns = ""
oppositeCorner = str(XMax) + " " + str(YMax)
labels = "NO_LABELS"
templateExtent = "#"
geometryType = "POLYGON"

arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
                               cellSizeWidth, cellSizeHeight, numRows, numColumns,
                               oppositeCorner, labels, templateExtent, geometryType)

#Outputs that the file has been susesfully created
if arcpy.Exists(outFeatureClass):
    print "Created Fishnet file successfully!"

target_features="Fishnet_Apogon.shp"
join_features="Apong_Specie.shp"
out_feature_class="Apong_HeatMap.shp"
join_operation="JOIN_ONE_TO_ONE"
join_type="KEEP_ALL"
field_mapping=""
match_option="INTERSECT"
search_radius=""
distance_field_name=""

arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                           join_operation, join_type, field_mapping, match_option,
                           search_radius, distance_field_name)


#Deletes everything but the final heatmap and deletes shape file and fish net

if arcpy.Exists(out_feature_class):
    print "Created Heatmap file successfully!"
    print "Deleting intermediate files"
    arcpy.Delete_management(target_features)
    arcpy.Delete_management(join_features)


###Repeat For second Shape FIle #######

in_Table = r"Scarus.csv"
x_coords = "decLat"
y_coords = "decLong"
z_coords = ""
out_Layer = "Scarus"
saved_Layer = r"Scarus_Specie.shp"


# Sets the spatial reference
spRef = arcpy.SpatialReference(4326)

lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)

# Displays the total number of rows in the shape file
print (arcpy.GetCount_management(out_Layer))

# saves the created layer file
arcpy.CopyFeatures_management(lyr, saved_Layer)

#prints sucessful completion of shape file
if arcpy.Exists(saved_Layer):
    print "Created file successfully!"

#Extracting and printing the extent of the data file
desc = arcpy.Describe(saved_Layer)

XMin = desc.extent.XMin
XMax = desc.extent.XMax
YMin = desc.extent.YMin
YMax = desc.extent.YMax

#prints the extent
print ("Extent:\n  XMin: {0},\n XMax: {1}".format(desc.extent.XMin, desc.extent.XMax))
print ("Extent:\n  YMin: {0},\n YMax: {1}".format(desc.extent.YMin, desc.extent.YMax))






outFeatureClass = "Fishnet_Scarus.shp"
originCoordinate = str(XMin) + " " + str(YMin)
yAxisCoordinate = str(XMin) + " " + str(YMin + 1.0)
cellSizeWidth = "0.25"
cellSizeHeight = "0.25"
numRows = ""
numColumns = ""
oppositeCorner = str(XMax) + " " + str(YMax)
labels = "NO_LABELS"
templateExtent = "#"
geometryType = "POLYGON"

arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
                               cellSizeWidth, cellSizeHeight, numRows, numColumns,
                               oppositeCorner, labels, templateExtent, geometryType)

#Outputs that the file has been susesfully created
if arcpy.Exists(outFeatureClass):
    print "Created Fishnet file successfully!"

target_features="Fishnet_Scarus.shp"
join_features="Scarus_Specie.shp"
out_feature_class="Scarus_HeatMap.shp"
join_operation="JOIN_ONE_TO_ONE"
join_type="KEEP_ALL"
field_mapping=""
match_option="INTERSECT"
search_radius=""
distance_field_name=""

arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                           join_operation, join_type, field_mapping, match_option,
                           search_radius, distance_field_name)


#Deletes everything but the final heatmap and deletes shape file and fish net

if arcpy.Exists(out_feature_class):
    print "Created Heatmap file successfully!"
    print "Deleting intermediate files"
    arcpy.Delete_management(target_features)
    arcpy.Delete_management(join_features)
