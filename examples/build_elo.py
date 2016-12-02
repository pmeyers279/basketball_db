
from basketball_db import db_utilities
from court import (bball_court_half, bball_court_three, bball_court_blocks, bball_shot_points)

# set up some useful variables
HOME='/Users/mcoughlin/Code/Sports'
BASEDIR = '%s/bball_files/' % HOME

TEAMS=db_utilities.get_team_shortnames()

schedules = {}

for TEAM in TEAMS:
   schedules[TEAM] = {}
   for YEAR in [2008,2009,2010,2011,2012,2013,2014,2015,2016]:
       try:
           #db_utilities.save_team_season(TEAM,YEAR,BASEDIR)
           db_utilities.save_team_season(TEAM,YEAR,BASEDIR,games=[1])
           pass
       except AttributeError:
           print TEAM,YEAR
           print 'Missed game'

       try:
           schedule_dataframe = db_utilities.get_schedule(TEAM, YEAR, basedir=BASEDIR)
           schedules[TEAM][YEAR] = schedule_dataframe 
       except:
           continue

print schedules
