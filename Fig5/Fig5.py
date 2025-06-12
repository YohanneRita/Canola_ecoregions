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

## MAP WITH Difference

ds = xr.open_dataset('./GWSens_cur.nc')
y1 = ds.LATITUDE
x1 = ds.LONGITUDE
Cul = ds.WSPD
Cul.rio.set_spatial_dims(x_dim="LONGITUDE", y_dim="LATITUDE", inplace=True)
Cul.rio.write_crs("epsg:4269", inplace=True)
clip21 = Cul.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
Cul = ds.WSGD
Cul.rio.set_spatial_dims(x_dim="LONGITUDE", y_dim="LATITUDE", inplace=True)
Cul.rio.write_crs("epsg:4269", inplace=True)
clip26 = Cul.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)

ds1 = xr.open_dataset('./GWSens_126.nc')
Cul = ds1.WSPD.mean(['time'])-ds.WSPD.mean(['time'])
Cul.rio.set_spatial_dims(x_dim="LONGITUDE", y_dim="LATITUDE", inplace=True)
Cul.rio.write_crs("epsg:4269", inplace=True)
clip22 = Cul.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
Cul = ds1.WSGD.mean(['time'])-ds.WSGD.mean(['time'])
Cul.rio.set_spatial_dims(x_dim="LONGITUDE", y_dim="LATITUDE", inplace=True)
Cul.rio.write_crs("epsg:4269", inplace=True)
clip27 = Cul.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)

ds4 = xr.open_dataset('./GWSens_245.nc')
Cul = ds4.WSPD.mean(['time'])-ds.WSPD.mean(['time'])
Cul.rio.set_spatial_dims(x_dim="LONGITUDE", y_dim="LATITUDE", inplace=True)
Cul.rio.write_crs("epsg:4269", inplace=True)
clip23 = Cul.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
Cul = ds4.WSGD.mean(['time'])-ds.WSPD.mean(['time'])
Cul.rio.set_spatial_dims(x_dim="LONGITUDE", y_dim="LATITUDE", inplace=True)
Cul.rio.write_crs("epsg:4269", inplace=True)
clip28 = Cul.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)

ds2 = xr.open_dataset('./GWSens_370.nc')
Cul = ds2.WSPD.mean(['time'])-ds.WSPD.mean(['time'])
Cul.rio.set_spatial_dims(x_dim="LONGITUDE", y_dim="LATITUDE", inplace=True)
Cul.rio.write_crs("epsg:4269", inplace=True)
clip24 = Cul.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
Cul = ds2.WSGD.mean(['time'])-ds.WSGD.mean(['time'])
Cul.rio.set_spatial_dims(x_dim="LONGITUDE", y_dim="LATITUDE", inplace=True)
Cul.rio.write_crs("epsg:4269", inplace=True)
clip29 = Cul.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)

ds3 = xr.open_dataset('./GWSens_585.nc')
Cul = ds3.WSPD.mean(['time'])-ds.WSPD.mean(['time'])
Cul.rio.set_spatial_dims(x_dim="LONGITUDE", y_dim="LATITUDE", inplace=True)
Cul.rio.write_crs("epsg:4269", inplace=True)
clip25 = Cul.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
Cul = ds3.WSGD.mean(['time'])-ds.WSGD.mean(['time'])
Cul.rio.set_spatial_dims(x_dim="LONGITUDE", y_dim="LATITUDE", inplace=True)
Cul.rio.write_crs("epsg:4269", inplace=True)
clip30 = Cul.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)

fig, axes = plt.subplots(nrows=2, ncols=5, figsize =(18,3))
cmap="gnuplot2"
vmin=0
vmax=0.4
plt.subplot(2,5,1)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
               resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[0,1,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip21.mean(['time'])[:].T, cmap=cmap, levels=10, vmin=vmin, vmax=vmax)
plt.title("Current", fontsize = 10)
plt.ylabel("WSFPhotos", fontsize = 10)

cmap='seismic'
vmin=-0.06
vmax=0.06
plt.subplot(2,5,2)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
               resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[0,1,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip22.T, cmap=cmap, levels=10, vmin=vmin, vmax=vmax)
plt.title("SSP1-2.6", fontsize = 10)
plt.subplot(2,5,3)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
               resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[0,1,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip23.T, cmap=cmap, levels=10, vmin=vmin, vmax=vmax)
plt.title("SSP2-4.5", fontsize = 10)
plt.subplot(2,5,4)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
               resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[0,1,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip24.T, cmap=cmap, levels=10, vmin=vmin, vmax=vmax)
plt.title("SSP3-7.0", fontsize = 10)
plt.subplot(2,5,5)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
               resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[0,1,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip25.T, cmap=cmap, levels=10, vmin=vmin, vmax=vmax)
plt.title("SSP5-8.5", fontsize = 10)

cmap="gnuplot2"
vmin=0
vmax=0.4
plt.subplot(2,5,6)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
               resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[0,1,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip26.max(['time'])[:].T, cmap=cmap, levels=10, vmin=vmin, vmax=vmax)
plt.title("Current", fontsize = 10)
plt.ylabel("WSFGrowth", fontsize = 10)
plt.colorbar(ScalarMappable(norm=m.norm, cmap=m.cmap), ax=axes[:], label = 'Index',
             location='left', shrink=0.4, pad=0.02)
cmap='seismic'
vmin=-0.06
vmax=0.06
plt.subplot(2,5,7)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
               resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[0,1,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip27.T, cmap=cmap, levels=10, vmin=vmin, vmax=vmax)
plt.title("SSP1 2.6", fontsize = 10)
plt.subplot(2,5,8)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
               resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[0,1,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip28.T, cmap=cmap, levels=10, vmin=vmin, vmax=vmax)
plt.title("SSP2-4.5", fontsize = 10)
plt.subplot(2,5,9)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
               resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[0,1,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip29.T, cmap=cmap, levels=10, vmin=vmin, vmax=vmax)
plt.title("SSP3-7.0", fontsize = 10)
plt.subplot(2,5,10)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
               resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[0,1,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip30.T, cmap=cmap, levels=10, vmin=vmin, vmax=vmax)
plt.title("SSP5-8.5", fontsize = 10)
plt.colorbar(ScalarMappable(norm=m.norm, cmap=m.cmap), ax=axes[:], label = 'Difference',
             location='right', shrink=0.4, pad=0.03)

plt.savefig('./MAPwaterStressDIFFCURRENT.png',dpi=400, bbox_inches="tight")
plt.show()
