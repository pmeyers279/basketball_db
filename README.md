# basketball_db

[![Build Status](https://travis-ci.org/pmeyers279/basketball_db.svg?branch=master)](https://travis-ci.org/pmeyers279/basketball_db)

[![Coverage Status](https://coveralls.io/repos/github/pmeyers279/basketball_db/badge.svg)](https://coveralls.io/github/pmeyers279/basketball_db)

[![Code Health](https://landscape.io/github/pmeyers279/basketball_db/master/landscape.svg?style=flat)](https://landscape.io/github/pmeyers279/basketball_db/master)


package to query basketball-reference.com and save data.

**NOTE**: This package is still under very heavy development, and things are liable to change on a regular basis. At some point there might be a stable release, but for now we're just trying to get as much done as we can. 
**NOTE**: We call this "basketball db" where "db" refers to "database"...we're not creating a relational database here (at least not right now). It's a well-organized directory structure and file-naming scheme. Which is sometimes just as good or better :).
**NOTE**: We're not software developers we're physicists. Bear with us.

## Installation

### Requirements

* `numpy`
* `scipy`
* `pandas`
* `bs4`
* `matplotlib`

### Instructions

1. Clone the repo
2. cd to repo top level directory
3. run `pip install .` or `python setup.py install`

## Save all games for one team for 2015/2016 season

```
>>> from basketball_db import db_utilities
>>> db_utilities.save_team_season('MIN',2016,basedir='./')
```

This saves games in

`%(basedir)/%(year)/%(month)/%(day)/%(TEAM1)-AT-%(TEAM2).hdf5`

and before th first game is downloaded, it actually saves the team's schedule from their basketball-reference schedule page in:

`%(basedir)/SCHEDULES/%(TEAM)-%(YEAR)

where %(YEAR) is the second year in whatever season you're looking at (i.e. Minnesota, 2015/2016 would be saved in "MIN-2016").

Please run this before trying the examples. If you run this command in the examples folder it will give you the data necessary to run the example.
## Load data

It saves pandas dataframes for `home_box_score` and `away_box_score`, `home_shot_chart`, `away_shot_cart`

You can read this in with:
```
>>> import pandas as pd
>>> fname = './2015/10/28/MIN-AT-LAL.hdf5'
>>> away_shot_chart = pd.read_hdf(fname,'away_shot_chart')
>>> print away_shot_chart
```

Or, now you can do it with the under-development ShotChart class.

```
>>> from basketball_db.shotchart import ShotChart
>>> fnames = db_utilities.query_db('MIN','20151028','20151029')
>>> home_shot_chart, away_shot_chart = ShotChart.load_game(fnames[0])
>>> plot = home_shot_chart.plot()
>>> plot.show()
```

## Examples

`python save_team.py --team MIN --YMDStart 20151101 --YMDEnd 20151201 --inifile bball.ini`

## Run tests

1. cd to repo top level
2. run `python setup.py test`

