# 3D House Project

- Developer : `Ujjwal Kandel`
- Repository: `3D_houses`
- Type of Challenge: `Learning & Consolidation`
- Duration: `2 weeks`
- Deadline: `04/11/21 17:00 PM`
- Deployment strategy :
- GitHub page
- PowerPoint
- Jupyter Notebook
- Webpage
- App
- Team challenge : `solo`


### Mission Objectives
- Consolidate the knowledge in Python specifically in `Numpy, Pandas` and `Matplotlib`

### Learning Objectives
- Learn how to search and implement new libraries
- Learn how to read and use shapefiles
- Learn how to read and use geoTIFFs
- Learn how to render a 3D plot
- Learn how to present a final product


## Learning Objectives

- to be able to search and implement new libraries
- to be able to read and use the [shapefile](https://en.wikipedia.org/wiki/Shapefile) format
- to be able to read and use geoTIFFs
- to be able to render a 3D plot
- to be able to present a final product


## The Mission
__model a house in 3D with only a home address.__


### Terms you need to know


**LIDAR** is a method to measure distance using light. The device will illuminate a target with a laser light and a sensor will measure the reflection. Differences in wavelenght and return times will be used to get the 3D representations of an area. 

**Digital Surface Model (DSM)** includes ground surface, vegetation and man-made objects. DSM demonstrate the natural and artificial features on the Earth’s surface. DSM may be useful for RF planning, landscape modelling, city modelling, visualization applications and more.

**Digital Terrain Model (DTM)** is often required for flood or ground rupture modeling, land-use studies, geological analysis DSM demonstrate the natural and artificial features on the Earth’s surface.

**Canopy Height Model (CHM)** is the height or residual distance between the ground and the top of the of objects above the ground. This includes the actual heights of trees, builds and any other objects on the earth's surface. The CHM is created by subtracting the DTM from the DSM.


# Libraries for the project
```
import requests
import json
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

import rasterio as rs

from shapely.geometry import Polygon
from rasterio.mask import mask
import plotly.graph_objects as go
```




   **Requests** 
  - Requests library is the de facto standard for making HTTP requests in Python. 
  - In this project, requests is used to make requests_get from an API to get the addresses' details

    **json** 
  - JSON JavaScript Object Notation is a format for structuring data. It is mainly used for storing and transferring data between the browser and the server.
  - In this project, I use json to read the adress specifications in a dict format.

    **Numpy** 
  - NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays
  - In this project, I use Numpy to create meshgrid to create a rectangular grid out of two given one-dimensional arrays representing the Cartesian indexing or Matrix indexing.

    **Pandas** 
  - Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.
  - In this project, I use pandas read to create and read boundingbox.csv.

    **Pandas** 
  - Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.
  - In this project, I use pandas read to create and read boundingbox.csv.

    **matplotlib** 
  - Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy.. 
  - In this project, plotly is used to successfully plot the 3D version of the address.

    **Rasterio** 
  - Rasterio reads and writes geospatial raster data. 
  - In this project, rasterio is used to read the raster files and rasterio.mask is also used to create the masked tiff files.

    **Shapely** https://pypi.org/project/Shapely/
  - Shapely is a BSD-licensed Python package for manipulation and analysis of planar geometric objects.
  - In this project, Polygon is imported from Shapely.geometry to get the geometry polygon of the address.

    **Plotly** https://plotly.com/python
  - Plotly allows users to import, copy and paste, or stream data to be analyzed and visualized.
  - In this project, plotly is used to successfully plot the 3D version of the address.




## Repo Architecture 

```
3D_houses
│
│    bounding_box.csv             : explanation about the project
│   
│__   
│   
|    create_csv_bounds            : Jupyter notebook file
│   
│__ 
│   
|    OOP_3d_house                 : to create csv of boundingbox of each files
│  
│__ 
|
|    list_of_bounds.csv           : boundingbox of each files in csv
│

```

## Installation
  - If you wish to clone/fork this repository, you can just click on the repository, then click the Clone/fork button and follow the instructions.
  - This project was made with python 3.8


## Good Luck!