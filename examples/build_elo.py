
import numpy as np
import pandas as pd
from basketball_db import db_utilities
from court import (bball_court_half, bball_court_three, bball_court_blocks, bball_shot_points)

# set up some useful variables
HOME='/Users/mcoughlin/Code/Sports'
BASEDIR = '%s/bball_files/' % HOME

TEAMS=db_utilities.get_team_shortnames()

data = {}

for TEAM in TEAMS:
   data[TEAM] = {}
   data[TEAM]["ELO"] = 1400.0
   data[TEAM]["SCHEDULES"] = {}
   for YEAR in [2008,2009,2010,2011,2012,2013,2014,2015,2016]:
       try:
           #db_utilities.save_team_season(TEAM,YEAR,BASEDIR)
           #db_utilities.save_team_season(TEAM,YEAR,BASEDIR,games=[1])
           pass
       except AttributeError:
           print TEAM,YEAR
           print 'Missed game'

       try:
           schedule_dataframe = db_utilities.get_schedule(TEAM, YEAR, basedir=BASEDIR)
           data[TEAM]["SCHEDULES"][YEAR] = schedule_dataframe 
       except:
           continue

dates = []
for TEAM in data.iterkeys():
    for YEAR in data[TEAM]["SCHEDULES"].iterkeys():
        dates.append(data[TEAM]["SCHEDULES"][YEAR]["date"])
dates = np.sort(pd.concat(dates).unique())

for date in dates:
    for TEAM in data.iterkeys():
        for YEAR in data[TEAM]["SCHEDULES"].iterkeys():
            idx = np.where(data[TEAM]["SCHEDULES"][YEAR]["date"] == date)[0]
            if len(idx) == 0: continue
            game = data[TEAM]["SCHEDULES"][YEAR].loc[idx]
