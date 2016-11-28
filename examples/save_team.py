from basketball_db import create_db, query_db
from basketball_db import utils
from court import bball_court_half, bball_court_three

import numpy as np
import pandas as pd

from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib
from matplotlib.colors import LogNorm
matplotlib.use('agg')
import matplotlib.pyplot as plt

# need 3-letter code for team...Will add a list of these
TEAM = 'MIN'
# Second year in the season...i.e. 2016 for 2015/2016 season
YEAR = 2016
# which games from that season do you want to save? (optional)
GAMES = [1]
# run the code
#create_db.save_team_season(TEAM, YEAR, games=GAMES)
#create_db.save_team_season(TEAM, YEAR)

###############################
# THINGS THAT AREN'T SIMPLE YET
###############################

# load the data (need to add a function for this...but it will look like this)a
filename = './2015/10/28/MIN-AT-LAL.hdf5'

DATE1 = '20151028'
DATE2 = '20160413'
files = query_db.query_db(TEAM, date_start=DATE1, date_end=DATE2)

shots = []
for ii,filename in enumerate(files):
    filenameSplit = filename.split("/")[-1].replace(".hdf5","").split("-")
    if filenameSplit[2] == TEAM:
        isHome = True
    else:
        isHome = False
    if isHome:
        shot = pd.read_hdf(filename,'home_shot_chart')
    else:
        shot = pd.read_hdf(filename,'away_shot_chart')
    shots.append(shot)
shots = pd.concat(shots)

# plot the shot chart
plt.figure(figsize=(5,4.7))
ax = bball_court_half()
ax.scatter(50- shots['shot_xs'][shots['result']],
    shots['shot_ys'][shots['result']],c='g' )
ax.scatter(50- shots['shot_xs'][~shots['result']],
    shots['shot_ys'][~shots['result']],c='r' )
plt.savefig('test')
plt.close()

xedges = np.arange(50)
yedges = np.arange(50)
[X,Y] = np.meshgrid(xedges,yedges)

[Xpoints,Ypoints] = np.meshgrid((xedges[1:]+xedges[:-1])/2.0,(yedges[1:]+yedges[:-1])/2.0)
points = bball_court_three(Xpoints,Ypoints)

H_yes, xedges1, yedges1 = np.histogram2d(shots['shot_ys'][shots['result']],50-shots['shot_xs'][shots['result']], bins=(xedges, yedges))
H_no, xedges2, yedges2 = np.histogram2d(shots['shot_ys'][~shots['result']],50-shots['shot_xs'][~shots['result']], bins=(xedges, yedges))
H_total = H_yes + H_no
H_yes_perc = H_yes/H_total
H_no_perc = H_no/H_total

H_yes_perc[np.isnan(H_yes_perc)] = 0.0
H_no_perc[np.isnan(H_no_perc)] = 0.0

print "Percentage of shots made: %.5f%%"%(np.nansum(H_yes)/np.nansum(H_total))

# heatmap for the shot chart
plt.figure(figsize=(5.3,4.7))
ax = bball_court_half()
img = ax.pcolor(X,Y,H_yes_perc, cmap='RdBu_r', vmin=0,vmax=1)
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5.6%", pad=0.05)
plt.colorbar(img,label='Shot percentage',cax=cax)
plt.savefig('hist2d')
plt.close()

norm_arr = (H_yes_perc*points).reshape((points.size,1)).squeeze()
norm = np.mean(norm_arr[norm_arr>0])
std = np.std(norm_arr[norm_arr>0])
print norm
print std

# heat map based on points
plt.figure(figsize=(5.3,4.7))
ax = bball_court_half()
img = ax.pcolor(X,Y,H_yes_perc*points, cmap='Spectral_r', vmin=norm-0.5,
        vmax=norm+0.5)
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5.6%", pad=0.05)
plt.colorbar(img,label='Expected Points',cax=cax)
plt.savefig('points')
plt.close()
