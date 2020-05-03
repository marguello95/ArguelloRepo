# import all needed below
import arcpy,os
from math import radians, sin, cos

# Create Workspace where all input and output data is/will be stored
arcpy.env.workspace = r"G:\Week_11"
arcpy.env.overwriteOutput = True


Coor_list = []
with arcpy.da.SearchCursor("Site_Locations.shp", ['Shape@XY', 'Site_Code']) as cursor:
    for row in cursor:
        Coor_list.append(row[0])
# print Coor_list


# Set local variables for new shape file
out_path = arcpy.env.workspace
out_name = "CC_radiating_line.shp"
geometry_type = "POLYLINE"
template = "#"
has_m = "DISABLED"
has_z = "DISABLED"

# Setting spatial reference
spatial_ref = 32130

# Execute CreateFeatureclass tool with given spatial reference and other inputs from above
arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template,
                                    has_m, has_z, spatial_ref)

input_locations = Coor_list

for i in input_locations:

    origin_x, origin_y = i[0], i[1]
    distance = 10000
    angle = 10  # in degrees

    OutputFeature = os.path.join(out_path, out_name)

    # create list of bearings
    angles = range(0, 360, angle)

    for ang in angles:
        # calculate offsets with trig
        angle = float(int(ang))
        (disp_x, disp_y) = (distance * sin(radians(angle)), distance * cos(radians(angle)))
        (end_x, end_y) = (origin_x + disp_x, origin_y + disp_y)
        (end2_x, end2_y) = (origin_x + disp_x, origin_y + disp_y)

        cur = arcpy.InsertCursor(OutputFeature)
        lineArray = arcpy.Array()

        # start point
        start = arcpy.Point()
        (start.ID, start.X, start.Y) = (1, origin_x, origin_y)
        lineArray.add(start)

        # end point
        end = arcpy.Point()
        (end.ID, end.X, end.Y) = (2, end_x, end_y)
        lineArray.add(end)

        # write out line results to empty created shapefile
        feat = cur.newRow()
        feat.shape = lineArray
        cur.insertRow(feat)

        lineArray.removeAll()
        del cur

print "Radiating lines created..."

# Setting up Clip Tool
# Set local variables
in_features = "CC_radiating_line.shp"
clip_features = "NB_Coastline.shp"
out_feature_class = "Clipped_Line_Out.shp"
xy_tolerance = ""

# Execute Clip Tool
arcpy.Clip_analysis(in_features, clip_features, out_feature_class, xy_tolerance)
print "Radiating lines clipped to coastline..."

# Following code uses  Multipart to Singlepart Tool on the output to the clip used above
# It takes all lines that may intersect land twice creating multiple line segments of a single line
# and makes each line segment stored as  individual line of its own

arcpy.MultipartToSinglepart_management(in_features="Clipped_Line_Out.shp", out_feature_class="Single_to_Multi_out.shp")

print "Individual lines created..."

# Creating a 10 meter buffer around all site locations
arcpy.Buffer_analysis(in_features="Site_Locations.shp", out_feature_class="Location_w_10m_Buff.shp",
                      buffer_distance_or_field="10 Meters", line_side="FULL", line_end_type="ROUND", dissolve_option="NONE",
                      dissolve_field="", method="PLANAR")

print "10M buffer created..."

# Select layer by location for all lines that pass through the 10 m buffer. This will allow code to select only the
# lines that originate from the site locations only, not segmants that cross land twice

# Make a feature layer to use in select by location tool
arcpy.MakeFeatureLayer_management("Single_to_Multi_out.shp","single_part")
arcpy.MakeFeatureLayer_management("Location_w_10m_Buff.shp","buffer")

# Using the select Layer by location tool with created layers
arcpy.SelectLayerByLocation_management(in_layer="single_part", overlap_type="INTERSECT", select_features="buffer",
                                       search_distance="", selection_type="NEW_SELECTION", invert_spatial_relationship="NOT_INVERT")

# Used to create a new shape file from select layer by location tool
arcpy.CopyFeatures_management("single_part", "Single_to_Multi_out_Select.shp")



arcpy.MakeFeatureLayer_management("Single_to_Multi_out_Select.shp","SM_Select")
arcpy.MakeFeatureLayer_management("Location_w_10m_Buff.shp","buffer2")

print "Calculation Mean and Std Deviation for each site... "

# Spatial Join to join Site Code to Lines
arcpy.SpatialJoin_analysis(target_features="SM_Select", join_features="buffer2", out_feature_class="Final_Lines_w_Site.shp", join_operation="JOIN_ONE_TO_MANY", join_type="KEEP_ALL",
                           field_mapping='Id "Id" true true false 6 Long 0 6 ,First,#,Single_to_Multi_out_Select,Id,-1,-1;ORIG_FID "ORIG_FID" true true false 10 Long 0 10 ,First,#,Single_to_Multi_out_Select,ORIG_FID,-1,-1;Id_1 "Id_1" true true false 6 Long 0 6 ,First,#,Location_w_10m_Buff,Id,-1,-1;Site_Code "Site_Code" true true false 5 Text 0 0 ,First,#,Location_w_10m_Buff,Site_Code,-1,-1;BUFF_DIST "BUFF_DIST" true true false 19 Double 0 0 ,First,#,Location_w_10m_Buff,BUFF_DIST,-1,-1;ORIG_FID_1 "ORIG_FID_1" true true false 10 Long 0 10 ,First,#,Location_w_10m_Buff,ORIG_FID,-1,-1',
                           match_option="INTERSECT", search_radius="", distance_field_name="")


# Adds a field for length to the Final lines with site codes file
arcpy.MakeFeatureLayer_management("Final_Lines_w_Site.shp","Fin_Line")

arcpy.AddGeometryAttributes_management(Input_Features="Fin_Line", Geometry_Properties="LENGTH", Length_Unit="METERS", Area_Unit="", Coordinate_System="")


# Summary statistics calculates the mean and STDEV for each of the 9 site
# This is where the mean and standard dev. for each will be calculated and store- see here for final values
arcpy.MakeFeatureLayer_management("Final_Lines_w_Site.shp","Fin_Line2")
arcpy.Statistics_analysis(in_table="Fin_Line2", out_table="Mean_STDEV_Table", statistics_fields="LENGTH MEAN;LENGTH STD", case_field="JOIN_FID")


print "MEAN AND STDEV CREATED IN DATA FOLDER - SEE (Mean_STDEV_Table) for values "
print "Row id represents the site number: ( 1 = A1 / 2 = A2 / 3 = A3 / 4 = B1 / 5 = B2 / 6 = B3 / 7 = C1 / 8 = C2 / 9 = C3 )"
print "Final_Lines_w_Site.shp = Final Radiating Lines Output"
