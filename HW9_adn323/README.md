# HW 9
# Andrew Nell

# HW9_Assignment 1 - Review Plots
I reviewed the work of jlk635 and mjs639.

# HW9_Assignment 2 - Census Data Analysis
I worked predominantly on my own, howvever, discussed several questions with Jon Kastelan (jlk635).

Shape files were read in for PUMA's and these were then merged with various data sets (percentage broadband access, Number of LinkNYC connection per 100 people per PUMA). The data sets to be merged were found through the ACS API at the PUMA level so that these could just be merged. LinkNYC data was also brought in to determine the number if LinkNYC sites per PUMA and so we could see where free wireless internet is available relative to where there is broadband access in households. 

There were several tricky steps along the way, including:
* spatially merging the data sets where the coordinate systems need to be converted
* using the chorpleth function designed by FBB to plot geospatial data
* using the standard geopandas plot function and ensuring we have an understanding of formatting techniques 
* standard data wrangling techniques that have been used up to this point in the course like ensuring data type consistencies, merging, cleaning and removing unlikely/false data
* creating geopandas geometry from latitudes and longitudes in standard data frames
* using standard geopandas schemes to better visualise data sets and variance spatially

