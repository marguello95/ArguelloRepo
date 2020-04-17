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

##PROBLEM HERE??
arcpy.SelectLayerByLocation_management(in_layer="Single_to_Multi_out.shp", overlap_type="INTERSECT", select_features="Location_w_10m_Buff.shp",
                                       search_distance="", selection_type="NEW_SELECTION", invert_spatial_relationship="NOT_INVERT")

