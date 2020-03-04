import arcpy
import csv
arcpy.env.overwriteOutput = True

#Set Workspace
arcpy.env.workspace = r"G:\W6_CC" #Workplace for all my files for this project on my computer
workspace = r"G:\W6_CC"

# Creating an empty species list to populate with a loop clause from imported csv.
species_list = []

with open("FloKey2.csv") as species_csv:
    csv_reader = csv.reader(species_csv, delimiter=',')
    line_count = 0

    for row in csv_reader:
        if line_count != 0:
            if row[0] not in species_list:
                species_list.append(row[0])
        if line_count == 0:
            print "Columns: " + str(row)
            line_count += 1
        line_count += 1

print species_list
print("Processed " + str(line_count) + " lines.")


#Code does a Loop through the csv species list and seperates the species that have the same name together
# In this case it will be 2 species that are included in the FloKey2.csv file
for spc in species_list:
    with open("FloKey2.csv") as species_csv:
        csv_reader = csv.reader(species_csv, delimiter=',')
        file = open(spc[0:2] + ".csv", "w")
        file.write("sciName,decLat,decLong\n")
        for row in csv_reader:
            if row[0] == spc:

                string = ",".join(row)
                string = string + "\n"
                file.write(string)


#Code to create a shape file for each species present
for spc in species_list:
    in_Table = spc[0:2] + ".csv"
    x_coords = "decLat"
    y_coords = "decLong"
    z_coords = ""
    out_Layer = spc[0:2] + "_data"
    saved_Layer = spc[0:2] + ".shp"

    spRef = arcpy.SpatialReference(4326)
    lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)
    arcpy.CopyFeatures_management(lyr, saved_Layer)

    if arcpy.Exists(saved_Layer):
        print "Created shape file successfully!"
    else:
        print "An Error has occured"


#Extracting and printing the extent of the data file
    desc = arcpy.Describe(spc[0:2] + ".shp")
    XMin = desc.extent.XMin
    XMax = desc.extent.XMax
    YMin = desc.extent.YMin
    YMax = desc.extent.YMax

    # prints the extent
    print ("Extent:\n  XMin: {0},\n XMax: {1}".format(desc.extent.XMin, desc.extent.XMax))
    print ("Extent:\n  YMin: {0},\n YMax: {1}".format(desc.extent.YMin, desc.extent.YMax))


# Code to create fishnet for each shape file
    arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)

    outFeatureClass = spc[0:2] + "_Fishnet.shp"

    originCoordinate = str(XMin) + " " + str(YMin)
    yAxisCoordinate = str(XMin) + " " + str(YMin + 10)
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

# Print statement if file was created correctly
    if arcpy.Exists(outFeatureClass):
        print "Created Fishnet file successfully!"

# Creates a heat map for each species data

    target_features = spc[0:2] + "_Fishnet.shp"
    join_features = spc[0:2] + ".shp"
    out_feature_class = spc[0:2] + "_heatmap.shp"
    join_operation = "JOIN_ONE_TO_ONE"
    join_type = "KEEP_ALL"
    field_mapping = ""
    match_option = "INTERSECT"
    search_radius = ""
    distance_field_name = ""

    arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                               join_operation, join_type, field_mapping, match_option,
                               search_radius, distance_field_name)

# Print statement to make sure the heat map was created sucesfully
    if arcpy.Exists(out_feature_class):
        print "Created Heatmap file successfully!"

# Deletes the intermediate files that were created
    print "Deleting intermediate files"
    arcpy.Delete_management(target_features)
    arcpy.Delete_management(join_features)
