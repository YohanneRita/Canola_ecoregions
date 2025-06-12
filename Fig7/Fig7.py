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

#USAR Tmax e Tmin pra criar GDD
#MAY
name9 = 'TmaxMAYcurS.nc'
name1 = 'TmaxMAY126.nc'
name2 = 'TmaxMAY245.nc'
name3 = 'TmaxMAY370.nc'
name4 = 'TmaxMAY585.nc'
ds1 = xr.open_dataset(name1)
ds2 = xr.open_dataset(name2)
ds3 = xr.open_dataset(name3)
ds4 = xr.open_dataset(name4)
ds9 = xr.open_dataset(name9)
name10 = 'TminMAYcurS.nc'
name5 = 'TminMAY126.nc'
name6 = 'TminMAY245.nc'
name7 = 'TminMAY370.nc'
name8 = 'TminMAY585.nc'
ds5 = xr.open_dataset(name5)
ds6 = xr.open_dataset(name6)
ds7 = xr.open_dataset(name7)
ds8 = xr.open_dataset(name8)
ds10 = xr.open_dataset(name10)
ds1 = ds1.assign_coords(lon=(((ds1.lon+180)%360)-180))
ds2 = ds2.assign_coords(lon=(((ds2.lon+180)%360)-180))
ds3 = ds3.assign_coords(lon=(((ds3.lon+180)%360)-180))
ds4 = ds4.assign_coords(lon=(((ds4.lon+180)%360)-180))
ds5 = ds5.assign_coords(lon=(((ds5.lon+180)%360)-180))
ds6 = ds6.assign_coords(lon=(((ds6.lon+180)%360)-180))
ds7 = ds7.assign_coords(lon=(((ds7.lon+180)%360)-180))
ds8 = ds8.assign_coords(lon=(((ds8.lon+180)%360)-180))
ds9 = ds9.assign_coords(lon=(((ds9.lon+180)%360)-180))
ds10 = ds10.assign_coords(lon=(((ds10.lon+180)%360)-180))
#Criar GDD

Tmax1 = ds1.tasmax
Tmin1 = ds5.tasmin
GDD1 = ((Tmax1 - Tmin1)/2)-5

Tmax2 = ds2.tasmax
Tmin2 = ds6.tasmin
GDD2 = ((Tmax2 - Tmin2)/2)-5

Tmax3 = ds3.tasmax
Tmin3 = ds7.tasmin
GDD3 = ((Tmax3 - Tmin3)/2)-5

Tmax4 = ds4.tasmax
Tmin4 = ds8.tasmin
GDD4 = ((Tmax4 - Tmin4)/2)-5

Tmax21 = ds9.tasmax
Tmin21 = ds10.tasmin
GDD21 = ((Tmax21 - Tmin21)/2)-5
# Substitute negative values for zero
GDD1 = GDD1.where(GDD1 >=0,0)
GDD2 = GDD2.where(GDD2 >=0,0)
GDD3 = GDD3.where(GDD3 >=0,0)
GDD4 = GDD4.where(GDD4 >=0,0)
GDD21 = GDD21.where(GDD21 >=0,0)

#JUNE
name1 = 'TmaxJUN126.nc'
name2 = 'TmaxJUN245.nc'
name3 = 'TmaxJUN370.nc'
name4 = 'TmaxJUN585.nc'
name9 = 'TmaxJUNcurS.nc'
ds1 = xr.open_dataset(name1)
ds2 = xr.open_dataset(name2)
ds3 = xr.open_dataset(name3)
ds4 = xr.open_dataset(name4)
ds9 = xr.open_dataset(name9)
name5 = 'TminJUN126.nc'
name6 = 'TminJUN245.nc'
name7 = 'TminJUN370.nc'
name8 = 'TminJUN585.nc'
name10 = 'TminJUNcurS.nc'
ds5 = xr.open_dataset(name5)
ds6 = xr.open_dataset(name6)
ds7 = xr.open_dataset(name7)
ds8 = xr.open_dataset(name8)
ds10 = xr.open_dataset(name10)
ds1 = ds1.assign_coords(lon=(((ds1.lon+180)%360)-180))
ds2 = ds2.assign_coords(lon=(((ds2.lon+180)%360)-180))
ds3 = ds3.assign_coords(lon=(((ds3.lon+180)%360)-180))
ds4 = ds4.assign_coords(lon=(((ds4.lon+180)%360)-180))
ds5 = ds5.assign_coords(lon=(((ds5.lon+180)%360)-180))
ds6 = ds6.assign_coords(lon=(((ds6.lon+180)%360)-180))
ds7 = ds7.assign_coords(lon=(((ds7.lon+180)%360)-180))
ds8 = ds8.assign_coords(lon=(((ds8.lon+180)%360)-180))
ds9 = ds9.assign_coords(lon=(((ds9.lon+180)%360)-180))
ds10 = ds10.assign_coords(lon=(((ds10.lon+180)%360)-180))
Tmax1 = ds1.tasmax
Tmin1 = ds5.tasmin
GDD5 = ((Tmax1 - Tmin1)/2)-5
Tmax2 = ds2.tasmax
Tmin2 = ds6.tasmin
GDD6 = ((Tmax2 - Tmin2)/2)-5
Tmax3 = ds3.tasmax
Tmin3 = ds7.tasmin
GDD7 = ((Tmax3 - Tmin3)/2)-5
Tmax4 = ds4.tasmax
Tmin4 = ds8.tasmin
GDD8 = ((Tmax4 - Tmin4)/2)-5
Tmax22 = ds9.tasmax
Tmin22 = ds10.tasmin
GDD22 = ((Tmax22 - Tmin22)/2)-5
# Substitute negative values for zero
GDD5 = GDD5.where(GDD5 >=0,0)
GDD6 = GDD6.where(GDD6 >=0,0)
GDD7 = GDD7.where(GDD7 >=0,0)
GDD8 = GDD8.where(GDD8 >=0,0)
GDD22 = GDD22.where(GDD22 >=0,0)

#JULY
name1 = 'TmaxJUL126.nc'
name2 = 'TmaxJUL245.nc'
name3 = 'TmaxJUL370.nc'
name4 = 'TmaxJUL585.nc'
name9 = 'TmaxJULcurS.nc'
ds1 = xr.open_dataset(name1)
ds2 = xr.open_dataset(name2)
ds3 = xr.open_dataset(name3)
ds4 = xr.open_dataset(name4)
ds9 = xr.open_dataset(name9)
name10 = 'TminJULcurS.nc'
name5 = 'TminJUL126.nc'
name6 = 'TminJUL245.nc'
name7 = 'TminJUL370.nc'
name8 = 'TminJUL585.nc'
ds5 = xr.open_dataset(name5)
ds6 = xr.open_dataset(name6)
ds7 = xr.open_dataset(name7)
ds8 = xr.open_dataset(name8)
ds10 = xr.open_dataset(name10)
ds1 = ds1.assign_coords(lon=(((ds1.lon+180)%360)-180))
ds2 = ds2.assign_coords(lon=(((ds2.lon+180)%360)-180))
ds3 = ds3.assign_coords(lon=(((ds3.lon+180)%360)-180))
ds4 = ds4.assign_coords(lon=(((ds4.lon+180)%360)-180))
ds5 = ds5.assign_coords(lon=(((ds5.lon+180)%360)-180))
ds6 = ds6.assign_coords(lon=(((ds6.lon+180)%360)-180))
ds7 = ds7.assign_coords(lon=(((ds7.lon+180)%360)-180))
ds8 = ds8.assign_coords(lon=(((ds8.lon+180)%360)-180))
ds9 = ds9.assign_coords(lon=(((ds9.lon+180)%360)-180))
ds10 = ds10.assign_coords(lon=(((ds10.lon+180)%360)-180))
Tmax1 = ds1.tasmax
Tmin1 = ds5.tasmin
GDD9 = ((Tmax1 - Tmin1)/2)-5
Tmax2 = ds2.tasmax
Tmin2 = ds6.tasmin
GDD10 = ((Tmax2 - Tmin2)/2)-5
Tmax3 = ds3.tasmax
Tmin3 = ds7.tasmin
GDD11 = ((Tmax3 - Tmin3)/2)-5
Tmax4 = ds4.tasmax
Tmin4 = ds8.tasmin
GDD12 = ((Tmax4 - Tmin4)/2)-5
Tmax23 = ds9.tasmax
Tmin23 = ds10.tasmin
GDD23 = ((Tmax23 - Tmin23)/2)-5
# Substitute negative values for zero
GDD9 = GDD9.where(GDD9 >=0,0)
GDD10 = GDD10.where(GDD10 >=0,0)
GDD11 = GDD11.where(GDD11 >=0,0)
GDD12 = GDD12.where(GDD12 >=0,0)
GDD23 = GDD23.where(GDD23 >=0,0)

#AUGUST
name1 = 'TmaxAGO126.nc'
name2 = 'TmaxAGO245.nc'
name3 = 'TmaxAGO370.nc'
name4 = 'TmaxAGO585.nc'
name9 = 'TmaxAGOcurS.nc'
ds1 = xr.open_dataset(name1)
ds2 = xr.open_dataset(name2)
ds3 = xr.open_dataset(name3)
ds4 = xr.open_dataset(name4)
ds9 = xr.open_dataset(name9)
name10 = 'TminAGOcurS.nc'
name5 = 'TminAGO126.nc'
name6 = 'TminAGO245.nc'
name7 = 'TminAGO370.nc'
name8 = 'TminAGO585.nc'
ds5 = xr.open_dataset(name5)
ds6 = xr.open_dataset(name6)
ds7 = xr.open_dataset(name7)
ds8 = xr.open_dataset(name8)
ds10 = xr.open_dataset(name10)
ds1 = ds1.assign_coords(lon=(((ds1.lon+180)%360)-180))
ds2 = ds2.assign_coords(lon=(((ds2.lon+180)%360)-180))
ds3 = ds3.assign_coords(lon=(((ds3.lon+180)%360)-180))
ds4 = ds4.assign_coords(lon=(((ds4.lon+180)%360)-180))
ds5 = ds5.assign_coords(lon=(((ds5.lon+180)%360)-180))
ds6 = ds6.assign_coords(lon=(((ds6.lon+180)%360)-180))
ds7 = ds7.assign_coords(lon=(((ds7.lon+180)%360)-180))
ds8 = ds8.assign_coords(lon=(((ds8.lon+180)%360)-180))
ds9 = ds9.assign_coords(lon=(((ds9.lon+180)%360)-180))
ds10 = ds10.assign_coords(lon=(((ds10.lon+180)%360)-180))
Tmax1 = ds1.tasmax
Tmin1 = ds5.tasmin
GDD13 = ((Tmax1 - Tmin1)/2)-5
Tmax2 = ds2.tasmax
Tmin2 = ds6.tasmin
GDD14 = ((Tmax2 - Tmin2)/2)-5
Tmax3 = ds3.tasmax
Tmin3 = ds7.tasmin
GDD15 = ((Tmax3 - Tmin3)/2)-5
Tmax4 = ds4.tasmax
Tmin4 = ds8.tasmin
GDD16 = ((Tmax4 - Tmin4)/2)-5
Tmax24 = ds9.tasmax
Tmin24 = ds10.tasmin
GDD24 = ((Tmax24 - Tmin24)/2)-5
# Substitute negative values for zero
GDD13 = GDD13.where(GDD13 >=0,0)
GDD14 = GDD14.where(GDD14 >=0,0)
GDD15 = GDD15.where(GDD15 >=0,0)
GDD16 = GDD16.where(GDD16 >=0,0)
GDD24 = GDD24.where(GDD24 >=0,0)

#SEPTEMBER
name1 = 'TmaxSEP126.nc'
name2 = 'TmaxSEP245.nc'
name3 = 'TmaxSEP370.nc'
name4 = 'TmaxSEP585.nc'
name9 = 'TmaxSEPcurS.nc'
ds1 = xr.open_dataset(name1)
ds2 = xr.open_dataset(name2)
ds3 = xr.open_dataset(name3)
ds4 = xr.open_dataset(name4)
ds9 = xr.open_dataset(name9)
name10 = 'TminSEPcurS.nc'
name5 = 'TminSEP126.nc'
name6 = 'TminSEP245.nc'
name7 = 'TminSEP370.nc'
name8 = 'TminSEP585.nc'
ds5 = xr.open_dataset(name5)
ds6 = xr.open_dataset(name6)
ds7 = xr.open_dataset(name7)
ds8 = xr.open_dataset(name8)
ds10 = xr.open_dataset(name10)
ds1 = ds1.assign_coords(lon=(((ds1.lon+180)%360)-180))
ds2 = ds2.assign_coords(lon=(((ds2.lon+180)%360)-180))
ds3 = ds3.assign_coords(lon=(((ds3.lon+180)%360)-180))
ds4 = ds4.assign_coords(lon=(((ds4.lon+180)%360)-180))
ds5 = ds5.assign_coords(lon=(((ds5.lon+180)%360)-180))
ds6 = ds6.assign_coords(lon=(((ds6.lon+180)%360)-180))
ds7 = ds7.assign_coords(lon=(((ds7.lon+180)%360)-180))
ds8 = ds8.assign_coords(lon=(((ds8.lon+180)%360)-180))
ds9 = ds9.assign_coords(lon=(((ds9.lon+180)%360)-180))
ds10 = ds10.assign_coords(lon=(((ds10.lon+180)%360)-180))
Tmax1 = ds1.tasmax
Tmin1 = ds5.tasmin
GDD17 = ((Tmax1 - Tmin1)/2)-5
Tmax2 = ds2.tasmax
Tmin2 = ds6.tasmin
GDD18 = ((Tmax2 - Tmin2)/2)-5
Tmax3 = ds3.tasmax
Tmin3 = ds7.tasmin
GDD19 = ((Tmax3 - Tmin3)/2)-5
Tmax4 = ds4.tasmax
Tmin4 = ds8.tasmin
GDD20 = ((Tmax4 - Tmin4)/2)-5
Tmax25 = ds9.tasmax
Tmin25 = ds10.tasmin
GDD25 = ((Tmax25 - Tmin25)/2)-5
# Substitute negative values for zero
GDD17 = GDD17.where(GDD17 >=0,0)
GDD18 = GDD18.where(GDD18 >=0,0)
GDD19 = GDD19.where(GDD19 >=0,0)
GDD20 = GDD20.where(GDD20 >=0,0)
GDD25 = GDD25.where(GDD25 >=0,0)

# Accumulated GDD 26-year average
GDD1 = GDD1.sum(['time'])/26
GDD2 = GDD2.sum(['time'])/26
GDD3 = GDD3.sum(['time'])/26
GDD4 = GDD4.sum(['time'])/26
GDD5 = GDD5.sum(['time'])/26
GDD6 = GDD6.sum(['time'])/26
GDD7 = GDD7.sum(['time'])/26
GDD8 = GDD8.sum(['time'])/26
GDD9 = GDD9.sum(['time'])/26
GDD10 = GDD10.sum(['time'])/26
GDD11 = GDD11.sum(['time'])/26
GDD12 = GDD12.sum(['time'])/26
GDD13 = GDD13.sum(['time'])/26
GDD14 = GDD14.sum(['time'])/26
GDD15 = GDD15.sum(['time'])/26
GDD16 = GDD16.sum(['time'])/26
GDD17 = GDD17.sum(['time'])/26
GDD18 = GDD18.sum(['time'])/26
GDD19 = GDD19.sum(['time'])/26
GDD20 = GDD20.sum(['time'])/26
GDD21 = GDD21.sum(['time'])/26
GDD22 = GDD22.sum(['time'])/26
GDD23 = GDD23.sum(['time'])/26
GDD24 = GDD24.sum(['time'])/26
GDD25 = GDD25.sum(['time'])/26

# MAP GDD WITH DIFFERENCE
#MAY
GDD21.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
GDD21.rio.write_crs("epsg:4269", inplace=True)
clip21 = GDD21.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
GDD1 = GDD1-GDD21
GDD1.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
GDD1.rio.write_crs("epsg:4269", inplace=True)
clip1 = GDD1.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
GDD2 = GDD2-GDD21
GDD2.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
GDD2.rio.write_crs("epsg:4269", inplace=True)
clip2 = GDD2.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
GDD3 = GDD3-GDD21
GDD3.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
GDD3.rio.write_crs("epsg:4269", inplace=True)
clip3 = GDD3.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
GDD4 = GDD4-GDD21
GDD4.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
GDD4.rio.write_crs("epsg:4269", inplace=True)
clip4 = GDD4.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)

#JUNE
GDD22.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
GDD22.rio.write_crs("epsg:4269", inplace=True)
clip22 = GDD22.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
GDD5 = GDD5-GDD22
GDD5.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
GDD5.rio.write_crs("epsg:4269", inplace=True)
clip5 = GDD5.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
GDD6 = GDD6-GDD22
GDD6.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
GDD6.rio.write_crs("epsg:4269", inplace=True)
clip6 = GDD6.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
GDD7 = GDD7-GDD22
GDD7.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
GDD7.rio.write_crs("epsg:4269", inplace=True)
clip7 = GDD7.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
GDD8 = GDD8-GDD22
GDD8.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
GDD8.rio.write_crs("epsg:4269", inplace=True)
clip8 = GDD8.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)

#JULY
GDD23.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
GDD23.rio.write_crs("epsg:4269", inplace=True)
clip23 = GDD23.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
GDD9 = GDD9-GDD23
GDD9.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
GDD9.rio.write_crs("epsg:4269", inplace=True)
clip9 = GDD9.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
GDD10 = GDD10-GDD23
GDD10.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
GDD10.rio.write_crs("epsg:4269", inplace=True)
clip10 = GDD10.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
GDD11 = GDD11-GDD23
GDD11.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
GDD11.rio.write_crs("epsg:4269", inplace=True)
clip11 = GDD11.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
GDD12 = GDD12-GDD23
GDD12.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
GDD12.rio.write_crs("epsg:4269", inplace=True)
clip12 = GDD12.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)

#AUGUST
GDD24.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
GDD24.rio.write_crs("epsg:4269", inplace=True)
clip24 = GDD24.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
GDD13 = GDD13-GDD24
GDD13.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
GDD13.rio.write_crs("epsg:4269", inplace=True)
clip13 = GDD13.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
GDD14 = GDD14-GDD24
GDD14.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
GDD14.rio.write_crs("epsg:4269", inplace=True)
clip14 = GDD14.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
GDD15 = GDD15-GDD24
GDD15.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
GDD15.rio.write_crs("epsg:4269", inplace=True)
clip15 = GDD15.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
GDD16 = GDD16-GDD24
GDD16.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
GDD16.rio.write_crs("epsg:4269", inplace=True)
clip16 = GDD16.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)

#SEPTEMBER
GDD25.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
GDD25.rio.write_crs("epsg:4269", inplace=True)
clip25 = GDD25.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
GDD17 = GDD17-GDD25
GDD17.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
GDD17.rio.write_crs("epsg:4269", inplace=True)
clip17 = GDD17.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
GDD18 = GDD18-GDD25
GDD18.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
GDD18.rio.write_crs("epsg:4269", inplace=True)
clip18 = GDD18.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
GDD19 = GDD19-GDD25
GDD19.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
GDD19.rio.write_crs("epsg:4269", inplace=True)
clip19 = GDD19.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)
GDD20 = GDD20-GDD25
GDD20.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
GDD20.rio.write_crs("epsg:4269", inplace=True)
clip20 = GDD20.rio.clip(shp.geometry.apply(mapping), shp.crs, drop=False)

y1 = ds1.lat
x1 = ds1.lon

# MAPA GDD COM DIFERENCA
fig, axes = plt.subplots(nrows=5, ncols=5, figsize =(18,7))
#MAY
vmin=133
vmax=222
cmap="gnuplot2"
plt.subplot(5,5,1)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
              resolution='i')
#map.drawparallels(np.arange(48.9, 54., 1.), labels=[1,0,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip21, cmap=cmap, levels=20, vmin=vmin, vmax=vmax)
plt.title("Current", fontsize = 10)
plt.ylabel('May', fontsize = 10, rotation=90)

vmin=-14
vmax=57
cmap="nipy_spectral"
plt.subplot(5,5,2)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
              resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[1,0,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip1, cmap=cmap, levels=20, vmin=vmin, vmax=vmax)
plt.title("SSP1-2.6", fontsize = 10)
plt.subplot(5,5,3)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
              resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[1,0,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip2, cmap=cmap, levels=20, vmin=vmin, vmax=vmax)
plt.title("SSP2-4.5", fontsize = 10)
plt.subplot(5,5,4)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
              resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[1,0,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip3, cmap=cmap, levels=20, vmin=vmin, vmax=vmax)
plt.title("SSP3-7.0", fontsize = 10)
plt.subplot(5,5,5)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
              resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[1,0,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip4, cmap=cmap, levels=20, vmin=vmin, vmax=vmax)
plt.title("SSP5-8.5", fontsize = 10)

#JUNE
vmin=133
vmax=222
cmap="gnuplot2"
plt.subplot(5,5,6)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
              resolution='i')
#map.drawparallels(np.arange(48.9, 54., 1.), labels=[1,0,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip22, cmap=cmap, levels=20, vmin=vmin, vmax=vmax)
plt.title("Current", fontsize = 10)
plt.ylabel('June', fontsize = 10, rotation=90)

vmin=-14
vmax=57
cmap="nipy_spectral"
plt.subplot(5,5,7)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
              resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[1,0,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip5, cmap=cmap, levels=20, vmin=vmin, vmax=vmax)
plt.title("SSP1-2.6", fontsize = 10)
plt.subplot(5,5,8)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
              resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[1,0,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip6, cmap=cmap, levels=20, vmin=vmin, vmax=vmax)
plt.title("SSP2-4.5", fontsize = 10)
plt.subplot(5,5,9)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
              resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[1,0,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip7, cmap=cmap, levels=20, vmin=vmin, vmax=vmax)
plt.title("SSP3-7.0", fontsize = 10)
plt.subplot(5,5,10)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
              resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[1,0,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip8, cmap=cmap, levels=20, vmin=vmin, vmax=vmax)
plt.title("SSP5-8.5", fontsize = 10)

#JULY
vmin=133
vmax=222
cmap="gnuplot2"
plt.subplot(5,5,11)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
              resolution='i')
#map.drawparallels(np.arange(48.9, 54., 1.), labels=[1,0,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip23, cmap=cmap, levels=20, vmin=vmin, vmax=vmax)
plt.title("Current", fontsize = 10)
plt.ylabel('July', fontsize = 10, rotation=90)

vmin=-14
vmax=57
cmap="nipy_spectral"
plt.subplot(5,5,12)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
              resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[1,0,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip9, cmap=cmap, levels=20, vmin=vmin, vmax=vmax)
plt.title("SSP1-2.6", fontsize = 10)
plt.subplot(5,5,13)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
              resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[1,0,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip10, cmap=cmap, levels=20, vmin=vmin, vmax=vmax)
plt.title("SSP2-4.5", fontsize = 10)
plt.subplot(5,5,14)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
              resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[1,0,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip11, cmap=cmap, levels=20, vmin=vmin, vmax=vmax)
plt.title("SSP3-7.0", fontsize = 10)
plt.subplot(5,5,15)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
              resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[1,0,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip12, cmap=cmap, levels=20, vmin=vmin, vmax=vmax)
plt.title("SSP5-8.5", fontsize = 10)

#AUGUST
vmin=133
vmax=222
cmap="gnuplot2"
plt.subplot(5,5,16)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
              resolution='i')
#map.drawparallels(np.arange(48.9, 54., 1.), labels=[1,0,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip24, cmap=cmap, levels=20, vmin=vmin, vmax=vmax)
plt.title("Current", fontsize = 10)
plt.ylabel('August', fontsize = 10, rotation=90)

vmin=-14
vmax=57
cmap="nipy_spectral"
plt.subplot(5,5,17)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
              resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[1,0,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip13, cmap=cmap, levels=20, vmin=vmin, vmax=vmax)
plt.title("SSP1-2.6", fontsize = 10)
plt.subplot(5,5,18)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
              resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[1,0,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip14, cmap=cmap, levels=20, vmin=vmin, vmax=vmax)
plt.title("SSP2-4.5", fontsize = 10)
plt.subplot(5,5,19)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
              resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[1,0,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip15, cmap=cmap, levels=20, vmin=vmin, vmax=vmax)
plt.title("SSP3-7.0", fontsize = 10)
plt.subplot(5,5,20)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
              resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[1,0,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip16, cmap=cmap, levels=20, vmin=vmin, vmax=vmax)
plt.title("SSP5-8.5", fontsize = 10)

#SEPTEMBER
vmin=133
vmax=222
cmap="gnuplot2"
plt.subplot(5,5,21)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
              resolution='i')
#map.drawparallels(np.arange(48.9, 54., 1.), labels=[1,0,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip25, cmap=cmap, levels=20, vmin=vmin, vmax=vmax)
plt.title("Current", fontsize = 10)
plt.ylabel('September', fontsize=10, rotation=90)
plt.colorbar(ScalarMappable(norm=m.norm, cmap=m.cmap), ax=axes[:], label = "GDD (°C)", location='left',
             pad=0.03, shrink=0.3)
vmin=-14
vmax=57
cmap="nipy_spectral"
plt.subplot(5,5,22)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
              resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[1,0,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip17, cmap=cmap, levels=20, vmin=vmin, vmax=vmax)
plt.title("SSP1-2.6", fontsize = 10)
plt.subplot(5,5,23)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
              resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[1,0,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip18, cmap=cmap, levels=20, vmin=vmin, vmax=vmax)
plt.title("SSP2-4.5", fontsize = 10)
plt.subplot(5,5,24)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
              resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[1,0,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip19, cmap=cmap, levels=20, vmin=vmin, vmax=vmax)
plt.title("SSP3-7.0", fontsize = 10)
plt.subplot(5,5,25)
map = Basemap(projection='aea',llcrnrlon=-115.5,llcrnrlat=48.,urcrnrlon=-95.9,urcrnrlat=54., lon_0=-105., lat_0=51.,
              resolution='i')
map.drawparallels(np.arange(48.9, 54., 1.), labels=[1,0,0,0], fontsize=5, linewidth=0.3)
map.drawmeridians(np.arange(-115.5, -96.5, 5.), labels=[0,0,0,1], fontsize=5, linewidth=0.3)
lons,lats= np.meshgrid(x1,y1)
x,y = map(lons,lats)
m = map.contourf(x,y,clip20, cmap=cmap, levels=20, vmin=vmin, vmax=vmax)
plt.title("SSP5-8.5", fontsize = 10)
plt.colorbar(ScalarMappable(norm=m.norm, cmap=m.cmap), ax=axes[:], label = "Difference", location='right',
             pad=0.03, shrink=0.3)

plt.savefig('./GDDmonthMAPDIFFCURR.png',dpi=400, bbox_inches="tight")
plt.show()
