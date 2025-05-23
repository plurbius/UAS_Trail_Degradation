# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2025-04-19 13:55:47
"""
import arcpy
from arcpy.ia import *
from arcpy.sa import *
from arcpy.sa import *
from arcpy.sa import *
from arcpy.sa import *

def NARugosity():  # NARugosity

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    # Check out any necessary licenses.
    arcpy.CheckOutExtension("spatial")
    arcpy.CheckOutExtension("ImageAnalyst")
    arcpy.CheckOutExtension("3D")

    NA_Elevation_tif = arcpy.Raster("Admin\\NA_Elevation.tif")
    Trail_DSM = arcpy.Raster("Admin\\NA_Elevation_P_M")

    # Process: Aspect (Aspect) (sa)
    Trail_Tread_Aspect = "F:\\Grad\\Thesis\\Thesis_Working\\Thesis_Working.gdb\\NA_Aspect"
    Aspect = Trail_Tread_Aspect
    with arcpy.EnvManager(snapRaster="Admin\\NA_Elevation.tif"):
        Trail_Tread_Aspect = arcpy.sa.Aspect(NA_Elevation_tif, "PLANAR", "METER", "GEODESIC_AZIMUTHS", "GPU_THEN_CPU")
        Trail_Tread_Aspect.save(Aspect)


    # Process: Slope (Slope) (sa)
    Trail_Slope = "F:\\Grad\\Thesis\\Thesis_Working\\Thesis_Working.gdb\\NA_Slope"
    Slope = Trail_Slope
    with arcpy.EnvManager(snapRaster="Admin\\NA_Elevation.tif"):
        Trail_Slope = arcpy.sa.Slope(NA_Elevation_tif, "DEGREE", 1, "PLANAR", "METER", "GPU_THEN_CPU")
        Trail_Slope.save(Slope)


    # Process: Focal Statistics (Focal Statistics) (ia)
    Trail_Local_Elevation_SD = "F:\\Grad\\Thesis\\Thesis_Working\\Thesis_Working.gdb\\NA_3x3SD"
    Focal_Statistics = Trail_Local_Elevation_SD
    with arcpy.EnvManager(mask="F:\\Grad\\Thesis\\Thesis_Working\\Thesis_Working.gdb\\NA_TreadSmoothed", snapRaster="Admin\\NA_Elevation_P_M"):
        Trail_Local_Elevation_SD = arcpy.ia.FocalStatistics(Trail_DSM, "Rectangle 0.5 0.5 MAP", "STD", "DATA", 90)
        Trail_Local_Elevation_SD.save(Focal_Statistics)


    # Process: Times (Times) (sa)
    Trail_Rugosity = "F:\\Grad\\Thesis\\Thesis_Working\\Thesis_Working.gdb\\NA_Rugosity"
    Times = Trail_Rugosity
    with arcpy.EnvManager(cellSize="MAXOF", mask="F:\\Grad\\Thesis\\Thesis_Working\\Thesis_Working.gdb\\NA_TreadSmoothed", snapRaster="ModelBuilder\\Rugosity\\NA_3x3SD:NA_3x3SD"):
        Trail_Rugosity = arcpy.sa.Times(Trail_Local_Elevation_SD, Trail_Local_Elevation_SD)
        Trail_Rugosity.save(Times)


    # Process: Reclassify (Reclassify) (sa)
    Rugosity_Reclass = "F:\\Grad\\Thesis\\Thesis_Working\\Thesis_Working.gdb\\NA_Rugosity_SD_Reclass"
    Reclassify = Rugosity_Reclass
    with arcpy.EnvManager(cellSize="MAXOF"):
        Rugosity_Reclass = arcpy.sa.Reclassify(Trail_Rugosity, "VALUE", "0.000001 0.000536 1;0.000536 0.002433 2;0.002433 0.004330 3;0.004330 0.006228 4;0.006228 0.019811 5", "DATA")
        Rugosity_Reclass.save(Reclassify)


if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace="F:\\Grad\\Thesis\\Thesis_Working\\Thesis_Working.gdb", workspace="F:\\Grad\\Thesis\\Thesis_Working\\Thesis_Working.gdb"):
        NARugosity()
