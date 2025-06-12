import pandas as pd
import numpy as np
from matplotlib import pyplot as pl
import seaborn as sns #to format the figures
import warnings
warnings.filterwarnings("ignore")
import HydroErr as he
import math

L340P_o22 = {'CH': 1.19,
           'AD': 40,
           'GO': 41.4,
           'PM': 91,
           'Yi': 4004}
L340P_s22 = {'CH': 1.19,
           'AD': 40,
           'GO': 44.2,
           'PM': 95,
           'Yi': 4097}

L340_22 = pd.DataFrame(data=[L340P_o22,L340P_s22], index=['Observed','Simulated'])
L340_22_t = L340_22.T


L340P_o23 = {'CH': 1.29,
           'AD': 43,
           'GO': 40.1,
           'PM': 84,
           'Yi': 2963}
L340P_s23 = {'CH': 0.91,
           'AD': 49,
           'GO': 32.08,
           'PM': 97,
           'Yi': 2903}

L340_23 = pd.DataFrame(data=[L340P_o23,L340P_s23], index=['Observed','Simulated'])
L340_23_t = L340_23.T

a=he.nrmse_mean(L340_22_t['Simulated'],L340_22_t['Observed'])
b=he.r_squared(L340_22_t['Simulated'],L340_22_t['Observed'])
c=he.d(L340_22_t['Simulated'],L340_22_t['Observed'])
print(round(a,6),round(b,8),round(c,6))

a=he.nrmse_mean(L340_23_t['Simulated'],L340_23_t['Observed'])
b=he.r_squared(L340_23_t['Simulated'],L340_23_t['Observed'])
c=he.d(L340_23_t['Simulated'],L340_23_t['Observed'])
print(round(a,6),round(b,6),round(c,6))

pl.figure(figsize=(10,3))
pl.subplot(1,2,1)
sns.lineplot(data=L340_22_t[['Observed', 'Simulated']])
pl.yscale("log")
pl.title('L340PC Calibration')
pl.legend().remove()
pl.text(2, 10, 'nRMSE = 0.049', fontsize = 10)
pl.text(2, 6, 'R$^2$ = 0.99', fontsize = 10)
pl.text(2, 4, 'd = 0.99', fontsize = 10)

pl.subplot(1,2,2)
sns.lineplot(data=L340_23_t[['Observed', 'Simulated']])
pl.yscale("log")
pl.title('L340PC Validation')
pl.legend().remove()
pl.text(2, 10, 'nRMSE = 0.044', fontsize = 10)
pl.text(2, 6, 'R$^2$ = 0.99', fontsize = 10)
pl.text(2, 4, 'd = 0.99', fontsize = 10)
sns.set_theme(style="ticks", palette=["black", "black"])
sns.despine()

pl.savefig('CaliVali340.png', dpi=400, transparent=False)
pl.show()
