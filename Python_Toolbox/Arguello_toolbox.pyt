# Python Toolbox Assignment
# Created by: Michael Arguello
# Toolbox Includes Buffer, Intersect and Erase Tools

import arcpy

arcpy.env.overwriteOutput = True

# Define workspace where all input and output data will be stored
arcpy.env.workspace = r"G:\Week_13\Arguello_Data_Used"

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Arguello Python Toolbox"
        self.alias = ""

        # List of tool Included in toolbox
        # All 3 tools that are shown below will be listed here
        self.tools = [Buff, Inter, Erase]

# Creating the first tool, Buffer tool
# This tool will take the wetland shape file and create a 100 foot buffer around all wetland areas in Rhode Island
class Buff(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Buffer Tool"
        self.description = ""
        self.canRunInBackground = False

    # Code below defines all the input and output parameters that will be used to in the buffer tool
    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        input_polygon = arcpy.Parameter(name="input_polygon",
                                        displayName="Input Polygon",
                                        datatype="DEFeatureClass",
                                        parameterType="Required",
                                        direction="Input",  # Indicates this shape file as Input value used in tool
                                        )
        input_polygon.value = "wetlands.shp" # This is a default input value shapefile for tool
        params.append(input_polygon)
        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",
                                 direction="Output",  # Indicates this shape file will be output parameter for the tool
                                 )
        output.value = "Wetland_Buff_out.shp" # Default output shape file for buffer tool
        params.append(output)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    # Code used to execute the buffer tool and define which inputs are used from parameters section above
    def execute(self, parameters, messages):
        """The source code of the tool."""
        input_polygon = parameters[0].valueAsText
        output = parameters[1].valueAsText

        # Code that runs the buffer analysis with specified inputs
        arcpy.Buffer_analysis(in_features=input_polygon,
                              out_feature_class=output,
                              buffer_distance_or_field="100 Feet", # Will create a 100 foot buffer
                              line_side="FULL",
                              line_end_type="ROUND",
                              dissolve_option="NONE",
                              dissolve_field="")
        return



# Creating the intersect tool
# This tool takes the 100 ft wetland buffer and all roads in Rhode Island and
# creates a line output shape file of all roads that pass through the 100 ft buffers
class Inter(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Intersect Tool"
        self.description = ""
        self.canRunInBackground = False

    # Code below defines all the input and output parameters that will be used to in the intersect tool
    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        input_line = arcpy.Parameter(name="input_line",
                                     displayName="Input Line",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",
                                     direction="Input",  # Indicates shape file as a Input  used in tool
                                     )
        input_line.value = "RIDOTrds16.shp"  # This is a default input value shapefile for tool
        params.append(input_line)
        input_polygon2 = arcpy.Parameter(name="input_polygon",
                                        displayName="Input Polygon",
                                        datatype="DEFeatureClass",
                                        parameterType="Required",
                                        direction="Input",  # Indicates this shape file as Input value used in tool
                                        )
        input_polygon2.value = "Wetland_Buff_out.shp"  # This is a default input value shapefile for tool
        params.append(input_polygon2)
        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",
                                 direction="Output",  # Indicates this shapefile will be output parameter for the tool
                                 )
        output.value = "Roads_in_Wetland_Buffer.shp"  # Default output shapefile for intersect tool
        params.append(output)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    # Code used to execute the buffer tool and define which inputs are used from parameters section above
    def execute(self, parameters, messages):
        """The source code of the tool."""
        input_line = parameters[0].valueAsText
        input_polygon = parameters[1].valueAsText
        output = parameters[2].valueAsText

        # Code that runs the buffer analysis with specified inputs
        arcpy.Intersect_analysis(in_features=[input_polygon, input_line],
                                 out_feature_class=output,
                                 join_attributes="ALL",
                                 cluster_tolerance="",
                                 output_type="LINE")
        return

# Creating the erase tool
# This tool Erase any polygons of Rhode Isalnd that are within 100 feet(100 foot buffer) of a wetland shape files
# The output will be Area of Rhode Island that are not considered wetlands, or within 100 feet of wetlands
class Erase(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Erase Tool"
        self.description = ""
        self.canRunInBackground = False

    # Code below defines all the input and output parameters that will be used  in the erase tool
    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        input_polygon = arcpy.Parameter(name="input_polygon",
                                        displayName="Input Polygon",
                                        datatype="DEFeatureClass",
                                        parameterType="Required",
                                        direction="Input",  # Indicates this shape file as Input value used in tool
                                        )
        input_polygon.value = "RI.shp" # This is a default input value shapefile for tool
        params.append(input_polygon)
        input_polygon2 = arcpy.Parameter(name="input_polygon2",
                                        displayName="Input Polygon2",
                                        datatype="DEFeatureClass",
                                        parameterType="Required",
                                        direction="Input",  # Indicates this shape file as Input value used in tool
                                        )
        input_polygon2.value = "Wetland_Buff_out.shp"  # This is a default input value shapefile for tool
        params.append(input_polygon2)
        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",
                                 direction="Output",  # Indicates this shape file will be output parameter for the tool
                                 )
        output.value = "RI_Without_wetlands.shp" # Default output shape file for erase tool
        params.append(output)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    # Code used to execute the erase tool and define which inputs are used from parameters section above
    def execute(self, parameters, messages):
        """The source code of the tool."""
        input_polygon = parameters[0].valueAsText
        input_polygon2 = parameters[1].valueAsText
        output = parameters[2].valueAsText

        # Code that runs the erase tool for with specified inputs
        arcpy.Erase_analysis(in_features=input_polygon,
                             erase_features=input_polygon2,
                             out_feature_class=output,
                             cluster_tolerance="")
        return
