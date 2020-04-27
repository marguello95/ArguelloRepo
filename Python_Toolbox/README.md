# Arguello Python Toolbox
 
 Created by: **Michael Arguello**


 University of Rhode Island:
 1st Year MESM Student, Wetland, Watershed and Ecosystem Track


**Description of Toolbox:**

This toolbox was created as a python toolbox

**The toolbox includes the following 3 tool:**
Tool | Tool Description 
------------ | -------------
Buffer | Cretaes a 100 foot buffer around the input shapefile
Intersect | Computes a geometric intersection of the input features
Erase | Keeps portions of the input shapefiles falling outside the bondaries of the erase input shapefile and creates a new output feature class

What each tool does:

**Buffer Tool** takes an input shapefile and creates a 100 foot buffer around it in the output shapefile. With the example data used the tool takes the wetland shapefile and creates a 100 foot buffer around each wetland feature for all of Rhode Island.

**Intersect Tool** takes **2** input shapefiles and computes a geometric intersection of the input features. For the example data provided this tool takes the wetland with 100 ft buffer shapefile and Rhode Island roads shapefile  and
creates a line output shapefile of all roads that pass through the 100 ft buffers in Rhode Island.

**Erase Tool** takes  **2** input shapefiles and Keeps portions of the input shapefiles falling outside the bondaries of the erase input shapefile and creates a new output feature class. For the example data provided this tool takes Rhode Island state shapefile as the input and wetland with 100ft buffer as erase shapefile. The output is Rhode Island shapefile minus all wetlands and the 100 ft buffer around each 

These tools were built using sample data that was obtained from the RIGIS websit.

Below you can find a table describing the sample data that was used to test each tool.

Data File Name | File Description 
------------ | -------------
wetlands.shp | Shapefile that contains all areas classified as wetlands in Rhode Island as polygons
RIDOTrds16.shp | Shapefile that contains all roads in Rhode Island as polyline segments
RI.shp | Shapefile of Rhode Island state boundary. Contains RHode Island area polygon shapefile
Wetland_Buff_out.shp | Shapefile that is the output of the buffer tool / All wetland feature in RI with 100 ft buffer
Roads_in_Wetland_Buffer.shp | Output of Intersect tool / All roads in RI that are within the 100 ft wetland buffer
RI_Without_wetlands.shp | Output of Erase tool / Rhode Island state shapefile minus all wetlands and the 100 ft buffer
