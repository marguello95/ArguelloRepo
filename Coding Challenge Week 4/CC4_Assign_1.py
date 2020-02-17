
# Import system module (arcpy) that will be used
import arcpy
#using env from arcpy
from arcpy import env

# Set workspace to the folder where the data sets being processed can be found
env.workspace = "G:/Arguello_data"

# Set local variables to be used in clip file
#The code below will clip the local conservation areas that fall within the 100 year storm flood zones
in_features = "Local_Conservation_Areas.shp"
clip_features = "Inundation_Polygons_Major_Event_100year_with_3ft_SLR.shp"
out_feature_class = "G:/output/ConservationAreas_within_Floodzone.shp" #G:/ is the location on my PC, may be different on others
xy_tolerance = "#"

# Code to run the clip tool with all the given inputs above
arcpy.Clip_analysis(in_features, clip_features, out_feature_class, xy_tolerance)

#Note 1: output has clip output in currently, will have to delete in order to run
#Note 2: Data will have to be removed from zip file to C: drive location and may need to change G:/ to C:/ in code
