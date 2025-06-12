import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib.patches as mpatches

ACCESS_CM2 = './ACCESS_CM2/SUM_y_126.nc'
dsACCESS_CM2 = xr.open_dataset(ACCESS_CM2).to_dataframe()
aACCESS_CM2 = dsACCESS_CM2.dropna()
ACCESS_ESM1 = './ACCESS_ESM1/SUM_y_126.nc'
dsACCESS_ESM1 = xr.open_dataset(ACCESS_ESM1).to_dataframe()
aACCESS_ESM1 = dsACCESS_ESM1.dropna()
Can_ESM5 = './CAN-ESM5/SUM_y_126.nc'
dsCan_ESM5 = xr.open_dataset(Can_ESM5).to_dataframe()
aCan_ESM5 = dsCan_ESM5.dropna()
CMCC_ESM2 = './CMCC/SUM_y_126.nc'
dsCMCC_ESM2 = xr.open_dataset(CMCC_ESM2).to_dataframe()
aCMCC_ESM2 = dsCMCC_ESM2.dropna()
Earth3 = './EARTH3/SUM_y_126.nc'
dsEarth3 = xr.open_dataset(Earth3).to_dataframe()
aEarth3 = dsEarth3.dropna()
Earth3Veg = './EARTH3VEG/SUM_y_126.nc'
dsEarth3Veg = xr.open_dataset(Earth3Veg).to_dataframe()
aEarth3Veg = dsEarth3Veg.dropna()
GFDL = './GFDL/SUM_y_126.nc'
dsGFDL = xr.open_dataset(GFDL).to_dataframe()
aGFDL = dsGFDL.dropna()
INM4 = './INM4/SUM_y_126.nc'
dsINM4 = xr.open_dataset(INM4).to_dataframe()
aINM4 = dsINM4.dropna()
INM5 = './INM5/SUM_y_126.nc'
dsINM5 = xr.open_dataset(INM5).to_dataframe()
aINM5 = dsINM5.dropna()
MPILR = './MPILR/SUM_y_126.nc'
dsMPILR = xr.open_dataset(MPILR).to_dataframe()
aMPILR = dsMPILR.dropna()

ACCESS_CM2 = './ACCESS_CM2/SUM_y_245.nc'
dsACCESS_CM2 = xr.open_dataset(ACCESS_CM2).to_dataframe()
bACCESS_CM2 = dsACCESS_CM2.dropna()
ACCESS_ESM1 = './ACCESS_ESM1/SUM_y_245.nc'
dsACCESS_ESM1 = xr.open_dataset(ACCESS_ESM1).to_dataframe()
bACCESS_ESM1 = dsACCESS_ESM1.dropna()
Can_ESM5 = './CAN-ESM5/SUM_y_245.nc'
dsCan_ESM5 = xr.open_dataset(Can_ESM5).to_dataframe()
bCan_ESM5 = dsCan_ESM5.dropna()
CMCC_ESM2 = './CMCC/SUM_y_245.nc'
dsCMCC_ESM2 = xr.open_dataset(CMCC_ESM2).to_dataframe()
bCMCC_ESM2 = dsCMCC_ESM2.dropna()
Earth3 = './EARTH3/SUM_y_245.nc'
dsEarth3 = xr.open_dataset(Earth3).to_dataframe()
bEarth3 = dsEarth3.dropna()
Earth3Veg = './EARTH3VEG/SUM_y_245.nc'
dsEarth3Veg = xr.open_dataset(Earth3Veg).to_dataframe()
bEarth3Veg = dsEarth3Veg.dropna()
GFDL = './GFDL/SUM_y_245.nc'
dsGFDL = xr.open_dataset(GFDL).to_dataframe()
bGFDL = dsGFDL.dropna()
INM4 = './INM4/SUM_y_245.nc'
dsINM4 = xr.open_dataset(INM4).to_dataframe()
bINM4 = dsINM4.dropna()
INM5 = './INM5/SUM_y_245.nc'
dsINM5 = xr.open_dataset(INM5).to_dataframe()
bINM5 = dsINM5.dropna()
MPILR = './MPILR/SUM_y_245.nc'
dsMPILR = xr.open_dataset(MPILR).to_dataframe()
bMPILR = dsMPILR.dropna()

ACCESS_CM2 = './ACCESS_CM2/SUM_y_370.nc'
dsACCESS_CM2 = xr.open_dataset(ACCESS_CM2).to_dataframe()
cACCESS_CM2 = dsACCESS_CM2.dropna()
ACCESS_ESM1 = './ACCESS_ESM1/SUM_y_370.nc'
dsACCESS_ESM1 = xr.open_dataset(ACCESS_ESM1).to_dataframe()
cACCESS_ESM1 = dsACCESS_ESM1.dropna()
Can_ESM5 = './CAN-ESM5/SUM_y_370.nc'
dsCan_ESM5 = xr.open_dataset(Can_ESM5).to_dataframe()
cCan_ESM5 = dsCan_ESM5.dropna()
CMCC_ESM2 = './CMCC/SUM_y_370.nc'
dsCMCC_ESM2 = xr.open_dataset(CMCC_ESM2).to_dataframe()
cCMCC_ESM2 = dsCMCC_ESM2.dropna()
Earth3 = './EARTH3/SUM_y_370.nc'
dsEarth3 = xr.open_dataset(Earth3).to_dataframe()
cEarth3 = dsEarth3.dropna()
Earth3Veg = './EARTH3VEG/SUM_y_370.nc'
dsEarth3Veg = xr.open_dataset(Earth3Veg).to_dataframe()
cEarth3Veg = dsEarth3Veg.dropna()
GFDL = './GFDL/SUM_y_370.nc'
dsGFDL = xr.open_dataset(GFDL).to_dataframe()
cGFDL = dsGFDL.dropna()
INM4 = './INM4/SUM_y_370.nc'
dsINM4 = xr.open_dataset(INM4).to_dataframe()
cINM4 = dsINM4.dropna()
INM5 = './INM5/SUM_y_370.nc'
dsINM5 = xr.open_dataset(INM5).to_dataframe()
cINM5 = dsINM5.dropna()
MPILR = './MPILR/SUM_y_370.nc'
dsMPILR = xr.open_dataset(MPILR).to_dataframe()
cMPILR = dsMPILR.dropna()

ACCESS_CM2 = './ACCESS_CM2/SUM_y_585.nc'
dsACCESS_CM2 = xr.open_dataset(ACCESS_CM2).to_dataframe()
dACCESS_CM2 = dsACCESS_CM2.dropna()
ACCESS_ESM1 = './ACCESS_ESM1/SUM_y_585.nc'
dsACCESS_ESM1 = xr.open_dataset(ACCESS_ESM1).to_dataframe()
dACCESS_ESM1 = dsACCESS_ESM1.dropna()
Can_ESM5 = './CAN-ESM5/SUM_y_585.nc'
dsCan_ESM5 = xr.open_dataset(Can_ESM5).to_dataframe()
dCan_ESM5 = dsCan_ESM5.dropna()
CMCC_ESM2 = './CMCC/SUM_y_585.nc'
dsCMCC_ESM2 = xr.open_dataset(CMCC_ESM2).to_dataframe()
dCMCC_ESM2 = dsCMCC_ESM2.dropna()
Earth3 = './EARTH3/SUM_y_585.nc'
dsEarth3 = xr.open_dataset(Earth3).to_dataframe()
dEarth3 = dsEarth3.dropna()
Earth3Veg = './EARTH3VEG/SUM_y_585.nc'
dsEarth3Veg = xr.open_dataset(Earth3Veg).to_dataframe()
dEarth3Veg = dsEarth3Veg.dropna()
GFDL = './GFDL/SUM_y_585.nc'
dsGFDL = xr.open_dataset(GFDL).to_dataframe()
dGFDL = dsGFDL.dropna()
INM4 = './INM4/SUM_y_585.nc'
dsINM4 = xr.open_dataset(INM4).to_dataframe()
dINM4 = dsINM4.dropna()
INM5 = './INM5/SUM_y_585.nc'
dsINM5 = xr.open_dataset(INM5).to_dataframe()
dINM5 = dsINM5.dropna()
MPILR = './MPILR/SUM_y_585.nc'
dsMPILR = xr.open_dataset(MPILR).to_dataframe()
dMPILR = dsMPILR.dropna()

ACCESS_CM2 = './ACCESS_CM2/SUM_y_cur.nc'
dsACCESS_CM2 = xr.open_dataset(ACCESS_CM2).to_dataframe()
ACCESS_CM2 = dsACCESS_CM2.dropna()
ACCESS_ESM1 = './ACCESS_ESM1/SUM_y_cur.nc'
dsACCESS_ESM1 = xr.open_dataset(ACCESS_ESM1).to_dataframe()
ACCESS_ESM1 = dsACCESS_ESM1.dropna()
Can_ESM5 = './CAN-ESM5/SUM_y_cur.nc'
dsCan_ESM5 = xr.open_dataset(Can_ESM5).to_dataframe()
Can_ESM5 = dsCan_ESM5.dropna()
CMCC_ESM2 = './CMCC/SUM_y_cur.nc'
dsCMCC_ESM2 = xr.open_dataset(CMCC_ESM2).to_dataframe()
CMCC_ESM2 = dsCMCC_ESM2.dropna()
Earth3 = './EARTH3/SUM_y_cur.nc'
dsEarth3 = xr.open_dataset(Earth3).to_dataframe()
Earth3 = dsEarth3.dropna()
Earth3Veg = './EARTH3VEG/SUM_y_cur.nc'
dsEarth3Veg = xr.open_dataset(Earth3Veg).to_dataframe()
Earth3Veg = dsEarth3Veg.dropna()
GFDL = './GFDL/SUM_y_cur.nc'
dsGFDL = xr.open_dataset(GFDL).to_dataframe()
GFDL = dsGFDL.dropna()
INM4 = './INM4/SUM_y_cur.nc'
dsINM4 = xr.open_dataset(INM4).to_dataframe()
INM4 = dsINM4.dropna()
INM5 = '.INM5/SUM_y_cur.nc'
dsINM5 = xr.open_dataset(INM5).to_dataframe()
INM5 = dsINM5.dropna()
MPILR = './MPILR/SUM_y_cur.nc'
dsMPILR = xr.open_dataset(MPILR).to_dataframe()
MPILR = dsMPILR.dropna()



data1 = [ACCESS_CM2['HWAH'],
	aACCESS_CM2['HWAH'],
	bACCESS_CM2['HWAH'],
	cACCESS_CM2['HWAH'],
	dACCESS_CM2['HWAH']]
data2 = [ACCESS_ESM1['HWAH'],
	aACCESS_ESM1['HWAH'],
	bACCESS_ESM1['HWAH'],
	cACCESS_ESM1['HWAH'],
	dACCESS_ESM1['HWAH']]
data3 = [Can_ESM5['HWAH'],
	aCan_ESM5['HWAH'],
	bCan_ESM5['HWAH'],
	cCan_ESM5['HWAH'],
	dCan_ESM5['HWAH']]
data4 = [CMCC_ESM2['HWAH'],
	aCMCC_ESM2['HWAH'],
	bCMCC_ESM2['HWAH'],
	cCMCC_ESM2['HWAH'],
	dCMCC_ESM2['HWAH']]
data5 = [Earth3['HWAH'],
	aEarth3['HWAH'],
	bEarth3['HWAH'],
	cEarth3['HWAH'],
	dEarth3['HWAH']]
data6 = [Earth3Veg['HWAH'],
	aEarth3Veg['HWAH'],
	bEarth3Veg['HWAH'],
	cEarth3Veg['HWAH'],
	dEarth3Veg['HWAH']]
data7 = [GFDL['HWAH'],
	aGFDL['HWAH'],
	bGFDL['HWAH'],
	cGFDL['HWAH'],
	dGFDL['HWAH']]
data8 = [INM4['HWAH'],
	aINM4['HWAH'],
	bINM4['HWAH'],
	cINM4['HWAH'],
	dINM4['HWAH']]
data9 = [INM5['HWAH'],
	aINM5['HWAH'],
	bINM5['HWAH'],
	cINM5['HWAH'],
	dINM5['HWAH']]
data10 = [MPILR['HWAH'],
	aMPILR['HWAH'],
	bMPILR['HWAH'],
	cMPILR['HWAH'],
	dMPILR['HWAH']]

data_groups = [data1,data2,data3,data4,data5,data6,data7,data8,data9,data10]

colors = ["#6e83ef",
"#5661c2",
"#441f5d",
"#713595",
"#965cc3",
"#c382e6",
"#d673ca",
"#c028a9",
"#e944ca",
"#e831a0"]
labels_list=['Current','SSP1-2.6','SSP2-4.5','SSP3-7.0','SSP5-8.5']
legend_labels = ['ACCESS-CM2', 'ACCESS-ESM1-5', 'Can-ESM5', 'CMCC-ESM2', 'EC-Earth3',
     'EC-Earth3-Veg-LR', 'GFDL-ESM4', 'INM-CM4-8', 'INM-CM5-0', 'MPI-ESM1-2-LR']
width       = 1/len(labels_list)
xlocations  = [ x*((1+ len(data_groups))*width) for x in range(len(data1)) ]
symbol      = 'r+'
legend_dict=dict(zip(legend_labels,colors))
patchList = [mpatches.Patch(color=color, label=label) for label, color in legend_dict.items()]

figure = plt.figure(figsize =(10, 5))
ax = figure.add_subplot(111)
colors = ["#6e83ef",
"#5661c2",
"#441f5d",
"#713595",
"#965cc3",
"#c382e6",
"#d673ca",
"#c028a9",
"#e944ca",
"#e831a0"]
space = len(data_groups)/2
offset = len(data_groups)/2
group_positions = []
for num, dg in enumerate(data_groups):
    _off = (0 - space + (0.5+num))
    print(_off)
    group_positions.append([x+_off*(width+0.01) for x in xlocations])


for dg, pos, color in zip(data_groups, group_positions, colors):
    bp = ax.boxplot(x=dg, patch_artist = True,notch ='True',positions=pos,widths=width, showfliers=False)
    for patch in bp['boxes']:
        patch.set_facecolor(color)
    for whisker in bp['whiskers']:
        whisker.set(color ='#8E008B',linewidth = 1.4,linestyle =":")
    for cap in bp['caps']:
        cap.set(color ='#8E008B',linewidth = 2.1)
    for median in bp['medians']:
        median.set(color ='blue',linewidth = 3)


ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
plt.xlabel('Climate Models')
plt.ylabel('Yield (kg/ha)')
ax.set_xticks( xlocations )
ax.set_xticklabels( labels_list, rotation=0 )
sns.set_theme(style="ticks", palette=["black", "black"])
sns.despine()
plt.savefig('./Boxplot_ClimateModelsCURRENT.png',dpi=400)
plt.close()
#ax.legend(handles=patchList,fontsize='small', ncols = 5, loc='lower center', bbox_to_anchor=(0.5, 0.5), frameon=False)
