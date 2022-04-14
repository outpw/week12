#******************************
# Week11 Workalong: Scipy filtering and convolution techniques
# Created by:  Phil White (modified from "Geoprocessing with Python, C. Garrard)
# Updated on:  04/04/2022, PW
# Description: A quick zonal stats appraoch using scipy
#******************************
#%%
import numpy as np
import arcpy
from arcpy import env
from arcpy import sa
import scipy.stats

#%% Environment settings, etc:
env.workspace = r'C:\Users\phwh9568\GEOG_4303\Week11\data\results' # change to your workspace
env.overwriteOutput = 1
arcpy.CheckOutExtension('SPATIAL')

#%%
ecoRaster = sa.Raster(r'C:\Users\phwh9568\GEOG_4303\Week11\Data\CO_EcoRegions_Excerpt.tif')
nlcdRaster = sa.Raster(r'C:\Users\phwh9568\GEOG_4303\Week11\Data\NLCD_CO_Excerpt.tif')

#%%
assert ecoRaster.meanCellWidth - nlcdRaster.meanCellWidth < 0.0001
#%%
cellSize = ecoRaster.meanCellWidth
llpt = ecoRaster.extent.lowerLeft
crs = ecoRaster.spatialReference 

#%%
ecoArray = arcpy.RasterToNumPyArray(ecoRaster).flatten()
nlcdArray = arcpy.RasterToNumPyArray(nlcdRaster).flatten()

#%% bins:
ecoBins = np.unique(ecoArray)
nlcdBins = np.unique(nlcdArray)

#%% bin boundaries:
ecoBound = max(ecoBins) + 1
nlcdBound = max(nlcdBins)+1

#%% Add bounds to the bins
ecoBins = np.append(ecoBins,ecoBound)
nlcdBins = np.append(nlcdBins,nlcdBound)

#%% scipy.stats.binned_statistic_2d
hist, ecoBins2, nlcdBins2, bn = scipy.stats.binned_statistic_2d(ecoArray,nlcdArray,nlcdArray,'count',[ecoBins,nlcdBins])

# although this function returns four different values, we really only need the histogram, so these other variables go unused this time
# This time, we took 'count' as the stat, but there are other options... see docs
#%%
hist = np.insert(hist, 0, nlcdBins[:-1], 0)

# Add a top row that represents your nlcdBins (think of these as column labels)

#%%
row_labels = np.insert(ecoBins[:-1],0,0)
# a vertical column of the ecoregions

#%%
hist = np.insert(hist,0,row_labels,1)

#add the row labels to the hist as a vertical column at index 0
#%%
np.savetxt('histogram.csv',hist,fmt='%1.0f',delimiter=',')
