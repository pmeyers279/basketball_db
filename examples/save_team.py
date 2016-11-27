import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from basketball_db import create_db
from basketball_db import utils
import pandas as pd
from court import bball_court_half

# need 3-letter code for team...Will add a list of these
TEAM = 'MIN'
# Second year in the season...i.e. 2016 for 2015/2016 season
YEAR = 2016
# which games from that season do you want to save? (optional)
GAMES = [1]
# run the code
create_db.save_team_season(TEAM, YEAR, games=GAMES)

###############################
# THINGS THAT AREN'T SIMPLE YET
###############################

# load the data (need to add a function for this...but it will look like this)a
filename = './2015/10/28/MIN-AT-LAL.hdf5'

# get t-wolves shot chart
shots = pd.read_hdf(filename,'away_shot_chart')
print shots

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

