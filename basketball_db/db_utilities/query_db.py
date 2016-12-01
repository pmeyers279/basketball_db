import pandas as pd
from .utils import *
from teams import *
from datetime import datetime, timedelta
import glob


def query_db(team, date_start, date_end, basedir='./'):
    """
    query database between dates

    Parameters
    ----------
    team:  `str`
        3-letter team code
    date : `str` or `datetime.datetime` object
        date you want to load. Either string with
        YYYYMMDD format or datetime object

    Returns
    -------
    file_list : `list`
        list of files for games for that team between those dates
    """
    if isinstance(date_start, str):
        date_start = datetime.strptime(date_start, '%Y%m%d')
    elif date_start is None:
        print 'Start date not set...setting it to yesterday'
        date_start = datetime.yesterday
    if isinstance(date_end, str):
        date_end = datetime.strptime(date_end, '%Y%m%d')
    elif date_end is None:
        print 'End date not set...setting it to today'
        date_end = datetime.today
    date_inc = date_start
    files = []
    while date_inc <= date_end:
        path = date2path(date_inc, basedir=basedir)
        match_str = '%s/*%s*' % (path, team)
        games = glob.glob(match_str)
        if len(games)==0:
            date_inc += timedelta(days=1)
            continue
        if len(games) > 1:
            err_mess = """You seem to have a team playing multiple games on the
            same day"""
            raise ValueError(err_mess)
        files.append(games[0])
        date_inc += timedelta(days=1)
    return files

def get_schedule(TEAM, YEAR, basedir='./'):
    """
    Get schedule for a team for a given year

    Parameters
    ----------
    TEAM : TODO
    YEAR : TODO

    Returns
    -------
    TODO

    """
    scheds = []
    schedule_file = get_schedule_name(TEAM, int(YEAR), basedir)
    scheds.append(pd.read_hdf(schedule_file,'schedule'))
    schedule = pd.concat(scheds)
    # remove headers
    schedule = schedule[schedule.pts!='Tm']
    opp_names = [convert_team(t) for t in schedule['opp_name']]
    df = pd.DataFrame()
    df['pts'] = pd.to_numeric(schedule['pts'])
    df['opp_pts'] = pd.to_numeric(schedule['opp_pts'])
    df['win'] = schedule['game_result']=='W'
    df['location'] = schedule['game_location']=='H'
    df['opp_name'] = opp_names
    df['spread'] = df['pts'] - df['opp_pts']
    dates = [datetime.strptime(schedule['date_game'][idx],'%a, %b %d, %Y') for idx in schedule.index]
    df['date'] = dates
    return df

