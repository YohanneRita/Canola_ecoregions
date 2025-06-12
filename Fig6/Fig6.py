import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import cm
from matplotlib import colors
import numpy as np
import geopandas as gpd
import rioxarray
import shapely
from shapely.geometry import mapping
import seaborn as sns
from mpl_toolkits.basemap import Basemap
from mpl_toolkits import mplot3d
from matplotlib.cm import ScalarMappable

shp = gpd.read_file('./Prairie.shp', crs="epsg:4269")

## DIFFERENCE Water Stress from CURRENT

ds = xr.open_dataset('./GWSens_cur.nc')
y1 = ds.LATITUDE
x1 = ds.LONGITUDE
Cul = ds.HWAH
Cul.rio.set_spatial_dims(x_dim="LONGITUDE", y_dim="LATITUDE", inplace=True)
Cul.rio.write_crs("epsg:4269", inplace=True)
clip6 = Cul.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)

ds1 = xr.open_dataset('./GWSens_126.nc')
Cul = ds1.HWAH.mean(['time'])-ds.HWAH.mean(['time'])
Cul.rio.set_spatial_dims(x_dim="LONGITUDE", y_dim="LATITUDE", inplace=True)
Cul.rio.write_crs("epsg:4269", inplace=True)
clip7 = Cul.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)

ds2 = xr.open_dataset('./GWSens_245.nc')
Cul = ds2.HWAH.mean(['time'])-ds.HWAH.mean(['time'])
Cul.rio.set_spatial_dims(x_dim="LONGITUDE", y_dim="LATITUDE", inplace=True)
Cul.rio.write_crs("epsg:4269", inplace=True)
clip8 = Cul.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)

ds3 = xr.open_dataset('./GWSens_370.nc')
Cul = ds3.HWAH.mean(['time'])-ds.HWAH.mean(['time'])
Cul.rio.set_spatial_dims(x_dim="LONGITUDE", y_dim="LATITUDE", inplace=True)
Cul.rio.write_crs("epsg:4269", inplace=True)
clip9 = Cul.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)

ds4 = xr.open_dataset('./GWSens_585.nc')
Cul = ds4.HWAH.mean(['time'])-ds.HWAH.mean(['time'])
Cul.rio.set_spatial_dims(x_dim="LONGITUDE", y_dim="LATITUDE", inplace=True)
Cul.rio.write_crs("epsg:4269", inplace=True)
clip10 = Cul.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)

fig, axes = plt.subplots(nrows=1, ncols=5, figsize =(18,4))
vmin=13
vmax=2550
cmap="viridis_r"
plt.subplot(1,5,1)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
              resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[1,0,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip6.max(['time'])[:].T, cmap=cmap, levels=10, vmin=vmin, vmax=vmax)
plt.title("Current", fontsize = 8)
plt.colorbar(ScalarMappable(norm=m.norm, cmap=m.cmap), ax=axes[:], label = "kg/ha", location='top',
             pad=0.25, shrink=0.4)

vmin=-300
vmax=200
cmap="gnuplot2"
plt.subplot(1,5,2)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
              resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[1,0,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip7.T, cmap=cmap, levels=10, vmin=vmin, vmax=vmax)
plt.title("SSP1-2.6", fontsize = 8)
plt.subplot(1,5,3)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
              resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[1,0,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip8.T, cmap=cmap, levels=10, vmin=vmin, vmax=vmax)
plt.title("SSP2-4.5", fontsize = 8)
plt.subplot(1,5,4)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
              resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[1,0,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip9.T, cmap=cmap, levels=10, vmin=vmin, vmax=vmax)
plt.title("SSP3-7.0", fontsize = 8)
plt.subplot(1,5,5)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
              resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[1,0,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip10.T, cmap=cmap, levels=10, vmin=vmin, vmax=vmax)
plt.title("SSP5-8.5", fontsize = 8)
plt.colorbar(ScalarMappable(norm=m.norm, cmap=m.cmap), ax=axes[:], label = "Difference", location='top',
             pad=0.15, shrink=0.4)
plt.savefig('./YIELDMAPDIFFCURRENT.png',dpi=400, bbox_inches="tight")
plt.show()
