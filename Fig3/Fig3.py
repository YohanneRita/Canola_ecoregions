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

## DIFFERENCE SM, T from CURRENT

ds = xr.open_dataset('./GWSens_cur.nc')
y1 = ds.LATITUDE
x1 = ds.LONGITUDE
SW = (ds.SW1D + ds.SW2D + ds.SW3D + ds.SW4D + ds.SW5D)/5
SW.rio.set_spatial_dims(x_dim="LONGITUDE", y_dim="LATITUDE", inplace=True)
SW.rio.write_crs("epsg:4269", inplace=True)
clip1 = SW.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
Cul = ds.TMAXA
Cul.rio.set_spatial_dims(x_dim="LONGITUDE", y_dim="LATITUDE", inplace=True)
Cul.rio.write_crs("epsg:4269", inplace=True)
clip11 = Cul.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
Cul = ds.TMINA
Cul.rio.set_spatial_dims(x_dim="LONGITUDE", y_dim="LATITUDE", inplace=True)
Cul.rio.write_crs("epsg:4269", inplace=True)
clip16 = Cul.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)

ds1 = xr.open_dataset('./GWSens_126.nc')
y2 = ds1.LATITUDE
x2 = ds1.LONGITUDE
SW1 = (ds1.SW1D + ds1.SW2D + ds1.SW3D + ds1.SW4D + ds1.SW5D)/5
SW1 = SW1.mean(['time'])-SW.mean(['time'])
SW1.rio.set_spatial_dims(x_dim="LONGITUDE", y_dim="LATITUDE", inplace=True)
SW1.rio.write_crs("epsg:4269", inplace=True)
clip2 = SW1.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
Cul = ds1.TMAXA.mean(['time'])-ds.TMAXA.mean(['time'])
Cul.rio.set_spatial_dims(x_dim="LONGITUDE", y_dim="LATITUDE", inplace=True)
Cul.rio.write_crs("epsg:4269", inplace=True)
clip12 = Cul.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
Cul = ds1.TMINA.mean(['time'])-ds.TMINA.mean(['time'])
Cul.rio.set_spatial_dims(x_dim="LONGITUDE", y_dim="LATITUDE", inplace=True)
Cul.rio.write_crs("epsg:4269", inplace=True)
clip17 = Cul.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)

ds2 = xr.open_dataset('./GWSens_245.nc')
SW2 = (ds2.SW1D + ds2.SW2D + ds2.SW3D + ds2.SW4D + ds2.SW5D)/5
SW2 = SW2.mean(['time'])-SW.mean(['time'])
SW2.rio.set_spatial_dims(x_dim="LONGITUDE", y_dim="LATITUDE", inplace=True)
SW2.rio.write_crs("epsg:4269", inplace=True)
clip3 = SW2.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
Cul = ds2.TMAXA.mean(['time'])-ds.TMAXA.mean(['time'])
Cul.rio.set_spatial_dims(x_dim="LONGITUDE", y_dim="LATITUDE", inplace=True)
Cul.rio.write_crs("epsg:4269", inplace=True)
clip13 = Cul.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
Cul = ds2.TMINA.mean(['time'])-ds.TMINA.mean(['time'])
Cul.rio.set_spatial_dims(x_dim="LONGITUDE", y_dim="LATITUDE", inplace=True)
Cul.rio.write_crs("epsg:4269", inplace=True)
clip18 = Cul.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)


ds3 = xr.open_dataset('./GWSens_370.nc')
SW3 = (ds3.SW1D + ds3.SW2D + ds3.SW3D + ds3.SW4D + ds3.SW5D)/5
SW3 = SW3.mean(['time'])-SW.mean(['time'])
SW3.rio.set_spatial_dims(x_dim="LONGITUDE", y_dim="LATITUDE", inplace=True)
SW3.rio.write_crs("epsg:4269", inplace=True)
clip4 = SW3.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
Cul = ds3.TMAXA.mean(['time'])-ds.TMAXA.mean(['time'])
Cul.rio.set_spatial_dims(x_dim="LONGITUDE", y_dim="LATITUDE", inplace=True)
Cul.rio.write_crs("epsg:4269", inplace=True)
clip14 = Cul.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
Cul = ds3.TMINA.mean(['time'])-ds.TMINA.mean(['time'])
Cul.rio.set_spatial_dims(x_dim="LONGITUDE", y_dim="LATITUDE", inplace=True)
Cul.rio.write_crs("epsg:4269", inplace=True)
clip19 = Cul.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)

ds4 = xr.open_dataset('./GWSens_585.nc')
SW4 = (ds4.SW1D + ds4.SW2D + ds4.SW3D + ds4.SW4D + ds4.SW5D)/5
SW4 = SW4.mean(['time'])-SW.mean(['time'])
SW4.rio.set_spatial_dims(x_dim="LONGITUDE", y_dim="LATITUDE", inplace=True)
SW4.rio.write_crs("epsg:4269", inplace=True)
clip5 = SW4.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
Cul = ds4.TMAXA.mean(['time'])-ds.TMAXA.mean(['time'])
Cul.rio.set_spatial_dims(x_dim="LONGITUDE", y_dim="LATITUDE", inplace=True)
Cul.rio.write_crs("epsg:4269", inplace=True)
clip15 = Cul.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
Cul = ds4.TMINA.mean(['time'])-ds.TMINA.mean(['time'])
Cul.rio.set_spatial_dims(x_dim="LONGITUDE", y_dim="LATITUDE", inplace=True)
Cul.rio.write_crs("epsg:4269", inplace=True)
clip20 = Cul.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)

fig, axes = plt.subplots(nrows=3, ncols=5, figsize =(20,6))

## Row 1 - Soil Water
vmin=0.1
vmax=0.26
cmap="terrain_r"
plt.subplot(3,5,1)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
               resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[0,1,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip1.mean(['time'])[:].T, cmap=cmap, levels=10, vmin=vmin, vmax=vmax)
plt.title("Current", fontsize = 8)
plt.ylabel("Soil Water", fontsize = 8, labelpad = 10)
plt.annotate('a', map(-130.,54.), fontsize=12, color='black', annotation_clip=False)
plt.colorbar(ScalarMappable(norm=m.norm, cmap=m.cmap), ax=axes[0,:], label = "cm$^3$ cm$^{-3}$", location='left',
             shrink=0.8, pad=0.03)

vmin=-0.002
vmax=0.008
cmap="gist_rainbow_r"
plt.subplot(3,5,2)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
               resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[0,1,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x2,y2)
x,y = map(lons,lats)
m = map.contourf(x,y,clip2.T, cmap=cmap, levels=10, vmin=vmin, vmax=vmax)
plt.title("SSP1-2.6", fontsize = 8)
plt.subplot(3,5,3)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
               resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[0,1,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x2,y2)
x,y = map(lons,lats)
m = map.contourf(x,y,clip3.T, cmap=cmap, levels=10, vmin=vmin, vmax=vmax)
plt.title("SSP2-4.5", fontsize = 8)
plt.subplot(3,5,4)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
               resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[0,1,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x2,y2)
x,y = map(lons,lats)
m = map.contourf(x,y,clip4.T, cmap=cmap, levels=10, vmin=vmin, vmax=vmax)
plt.title("SSP3-7.0", fontsize = 8)
plt.subplot(3,5,5)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
               resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[0,1,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x2,y2)
x,y = map(lons,lats)
m = map.contourf(x,y,clip5.T, cmap=cmap, levels=10, vmin=vmin, vmax=vmax)
plt.title("SSP5-8.5", fontsize = 8)
plt.colorbar(ScalarMappable(norm=m.norm, cmap=m.cmap), ax=axes[0,:], label = "Difference", location='right',
             shrink=0.8, pad=0.03)

## Row 2 - Max Temperature
vmin=20
vmax=27
cmap="rainbow"
plt.subplot(3,5,6)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
               resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[0,1,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip11.mean(['time'])[:].T, cmap=cmap, levels=18, vmin=vmin, vmax=vmax)
plt.title("Current", fontsize = 8)
plt.ylabel("Maximum Temperature", fontsize = 8, labelpad = 10)
plt.annotate('b', map(-130.,54.), fontsize=12, color='black', annotation_clip=False)
plt.colorbar(ScalarMappable(norm=m.norm, cmap=m.cmap), ax=axes[1,:], label = "°C", location='left',
             shrink=0.8, pad=0.03)

vmin=0.7
vmax=2
cmap="gist_rainbow_r"
plt.subplot(3,5,7)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
               resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[0,1,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip12.T, cmap=cmap, levels=18, vmin=vmin, vmax=vmax)
plt.title("SSP1-2.6", fontsize = 8)
plt.subplot(3,5,8)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
               resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[0,1,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x2,y2)
x,y = map(lons,lats)
m = map.contourf(x,y,clip13.T, cmap=cmap, levels=10, vmin=vmin, vmax=vmax)
plt.title("SSP2-4.5", fontsize = 8)
plt.subplot(3,5,9)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
               resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[0,1,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip14.T, cmap=cmap, levels=18, vmin=vmin, vmax=vmax)
plt.title("SSP3-7.0", fontsize = 8)
plt.subplot(3,5,10)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
               resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[0,1,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip15.T, cmap=cmap, levels=18, vmin=vmin, vmax=vmax)
plt.title("SSP5-8.5", fontsize = 8)
plt.colorbar(ScalarMappable(norm=m.norm, cmap=m.cmap), ax=axes[1,:], label = "Difference", location='right',
             shrink=0.8, pad=0.03)

## Row 3 - Min Temperature
vmin=5
vmax=13
cmap="winter"
plt.subplot(3,5,11)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
               resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[0,1,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip16.mean(['time'])[:].T, cmap=cmap, levels=18, vmin=vmin, vmax=vmax)
plt.title("Current", fontsize = 8)
plt.ylabel("Minimum Temperature", fontsize = 8, labelpad = 10)
plt.annotate('c', map(-130.,54.), fontsize=12, color='black', annotation_clip=False)
plt.colorbar(ScalarMappable(norm=m.norm, cmap=m.cmap), ax=axes[2,:], label = "°C", location='left',
             shrink=0.8, pad=0.03)

vmin=0.5
vmax=3.5
cmap="gist_rainbow_r"
plt.subplot(3,5,12)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
               resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[0,1,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip17.T, cmap=cmap, levels=18, vmin=vmin, vmax=vmax)
plt.title("SSP1-2.6", fontsize = 8)
plt.subplot(3,5,13)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
               resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[0,1,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x2,y2)
x,y = map(lons,lats)
m = map.contourf(x,y,clip18.T, cmap=cmap, levels=10, vmin=vmin, vmax=vmax)
plt.title("SSP2-4.5", fontsize = 8)
plt.subplot(3,5,14)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
               resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[0,1,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip19.T, cmap=cmap, levels=18, vmin=vmin, vmax=vmax)
plt.title("SSP3-7.0", fontsize = 8)
plt.subplot(3,5,15)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
               resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[0,1,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip20.T, cmap=cmap, levels=18, vmin=vmin, vmax=vmax)
plt.title("SSP5-8.5", fontsize = 8)
plt.colorbar(ScalarMappable(norm=m.norm, cmap=m.cmap), ax=axes[2,:], label = "Difference", location='right',
             shrink=0.8, pad=0.03)

plt.savefig('./MAP3x5mean.png',dpi=400, bbox_inches="tight")
plt.show()
