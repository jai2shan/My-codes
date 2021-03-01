#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 22:50:06 2021

@author: jai
"""

import numpy as np
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns
import os
from descartes import PolygonPatch

sns.set(style="whitegrid", palette="pastel", color_codes=True)
sns.mpl.rc("figure", figsize=(10,6))


shp_path = "/home/jai/Documents/shpfiles/TM_WORLD_BORDERS-0.3.shp"

import geopandas as gpd
df = gpd.read_file(shp_path)
fig, ax = plt.subplots()
df.plot(ax=ax,color='white', edgecolor='black')
ax.set_aspect('equal')
plt.show()

#%%
shp_path = "/home/jai/Documents/shpfiles/TM_WORLD_BORDERS-0.3.shp"
import matplotlib.pyplot as plt
import geopandas as gpd
from descartes import PolygonPatch

world = gpd.read_file(shp_path)

def plotCountryPatch( axes, country_name, fcolor ):
    # plot a country on the provided axes
    nami = world[world.NAME == country_name]
    namigm = nami.__geo_interface__['features']  # geopandas's geo_interface
    namig0 = {'type': namigm[0]['geometry']['type'], 
              'coordinates': namigm[0]['geometry']['coordinates']}
    axes.add_patch(PolygonPatch( namig0, fc=fcolor, ec="black", alpha=0.85, zorder=1 ))

# plot the whole world
#ax2 = world.plot( figsize=(8,4), edgecolor=u'darkgray', cmap='Set2' )

# or plot Africa continent
ax2 = world.plot(figsize=(8,8), facecolor="grey", hatch="")

# then plot some countries on top
plotCountryPatch(ax2, 'Namibia', 'red')
plotCountryPatch(ax2, 'India', 'green')

# the place to plot additional vector data (points, lines)

# plt.ylabel('Latitude')
# plt.xlabel('Longitude')
plt.axis('off')

#ax2.axis('scaled')
plt.show()
