import pandas as pd
import numpy as np
import matplotlib.pyplot as mp


table = pd.read_csv('Attitude_data2.csv')
# print(table)


table['diff_roll'] = table['des_roll'] - table['roll']
table['diff_pitch'] = table['des_pitch'] - table['pitch']
table['diff_yaw'] = table['des_yaw'] - table['yaw']

for i in range(1,len(table['diff_roll'])):
    if abs(table['diff_roll'][i]) >=2:
     table['value_roll'] = -1
    else :
        table['value_roll']=1
i=i+1
# print(table['value_roll'])


for i in range(1,len(table['diff_pitch'])):
    if abs(table['diff_pitch'][i]) >=10:
     table['value_pitch'] = -1
    else :
        table['value_pitch']=1
i=i+1
# print(table['value_pitch'])


for i in range(1,len(table['diff_yaw'])):
    if abs(table['diff_yaw'][i]) >=50:
     table['value_yaw'] = -1
    else :
        table['value_yaw']=1
i=i+1# make a list of all dataframes
# print(table)
table.to_csv('Attitude_para_crash.csv', index=False, header=True)
#create subplot figure with having two side by side plots
fig, axes = mp.subplots(nrows=3,ncols=1,figsize=(12,6))
# plot first pandas frame in subplot style
table['diff_roll'].plot(ax = axes[0],subplots=True,title='Difference in Roll,Pitch and Yaw Values') 
# plot second pandas frame in subplot style
table['diff_pitch'].plot(ax = axes[1],subplots=True)
table['diff_yaw'].plot(ax = axes[2],subplots=True)
# mp.show()

# Finding the mode of the parameters

mode_roll = table['value_roll'].mode()
mode_pitch = table['value_pitch'].mode()
mode_yaw = table['value_yaw'].mode()

print(mode_roll)
print(mode_pitch)
print(mode_yaw)