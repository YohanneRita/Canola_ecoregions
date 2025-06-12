import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#Criar GDD changes for time series
name1 = 'TmaxYMs126.nc'
name2 = 'TmaxYMs245.nc'
name3 = 'TmaxYMs370.nc'
name4 = 'TmaxYMs585.nc'
name9 = 'TmaxYMsCur.nc'
ds1 = xr.open_dataset(name1)
ds2 = xr.open_dataset(name2)
ds3 = xr.open_dataset(name3)
ds4 = xr.open_dataset(name4)
ds9 = xr.open_dataset(name9)
name5 = 'TminYMs126.nc'
name6 = 'TminYMs245.nc'
name7 = 'TminYMs370.nc'
name8 = 'TminYMs585.nc'
name10 = 'TminYMsCur.nc'
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
Tmax5 = ds9.tasmax
Tmin5 = ds10.tasmin
GDD5 = ((Tmax5 - Tmin5)/2)-5
# Substitute negative values for zero
GDD1 = GDD1.where(GDD1 >=0,0)
GDD2 = GDD2.where(GDD2 >=0,0)
GDD3 = GDD3.where(GDD3 >=0,0)
GDD4 = GDD4.where(GDD4 >=0,0)
GDD5 = GDD5.where(GDD5 >=0,0)


time = ds1.time

# Select the months May to September
selected_months = GDD1.sel(time=GDD1['time.month'].isin([5, 6, 7, 8, 9]))
# Group by month and calculate the mean for each month
monthlyGDD1 = selected_months.groupby('time.month').mean()

selected_months = GDD2.sel(time=GDD2['time.month'].isin([5, 6, 7, 8, 9]))
monthlyGDD2 = selected_months.groupby('time.month').mean()
selected_months = GDD3.sel(time=GDD3['time.month'].isin([5, 6, 7, 8, 9]))
monthlyGDD3 = selected_months.groupby('time.month').mean()
selected_months = GDD4.sel(time=GDD4['time.month'].isin([5, 6, 7, 8, 9]))
monthlyGDD4 = selected_months.groupby('time.month').mean()
selected_months = GDD5.sel(time=GDD5['time.month'].isin([5, 6, 7, 8, 9]))
monthlyGDD5 = selected_months.groupby('time.month').mean()

#Reassing month names
month_names = {5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September'}
monthlyGDD1 = monthlyGDD1.assign_coords(month=[month_names[m] for m in monthlyGDD1['month'].values])
monthlyGDD2 = monthlyGDD2.assign_coords(month=[month_names[m] for m in monthlyGDD2['month'].values])
monthlyGDD3 = monthlyGDD3.assign_coords(month=[month_names[m] for m in monthlyGDD3['month'].values])
monthlyGDD4 = monthlyGDD4.assign_coords(month=[month_names[m] for m in monthlyGDD4['month'].values])
monthlyGDD5 = monthlyGDD5.assign_coords(month=[month_names[m] for m in monthlyGDD5['month'].values])

# PLOT MONTHLY MEAN
plt.figure(figsize =(20,6))
plt.plot(mtime,monthlyGDD1.mean(['lat','lon'])[0:7],label = 'SSP1-2.6', color='black', linestyle = 'dashdot')
plt.plot(mtime,monthlyGDD2.mean(['lat','lon'])[0:7],label = 'SSP2-4.5', color='black', linestyle = 'dashed')
plt.plot(mtime,monthlyGDD3.mean(['lat','lon'])[0:7],label = 'SSP3-7.0', color='black', linestyle = 'dotted')
plt.plot(mtime,monthlyGDD4.mean(['lat','lon'])[0:7],label = 'SSP5-8.5', color='black', linestyle = 'solid')
plt.plot(mtime,monthlyGDD5.mean(['lat','lon'])[0:7],label = 'Current', color='black', linestyle = 'solid', lw=3)
plt.ylim(180,230)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Average Monthly Accumulated GDD', fontsize=14)
sns.set_theme(style="ticks", palette=["black", "black"])
plt.legend(loc='upper left', fontsize=14)
sns.despine()
plt.savefig("./GDDAccTSmonthCURRENT.png", bbox_inches="tight")
plt.show()
