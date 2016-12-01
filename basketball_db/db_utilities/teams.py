
def get_team_shortnames():
    TEAMS =\
        ['ATL','BOS','BRK','CHI','CHA','CHO',\
        'CLE','DAL','DEN','DET','GSW','HOU',\
        'IND','LAC','LAL','MEM','MIA','MIL',\
        'MIN','NOP','NYK','OKC','ORL','PHI',\
        'PHO','POR','SAC','SAS','TOR','UTA','WAS']
    return TEAMS
def get_team_longnames():
    LONG_TEAMS=['Atlanta Hawks','Boston Celtics','Brooklyn Nets','Charlotte Hornets',
            'Chicago Bulls','Cleveland Cavaliers','Dallas Mavericks','Denver Nuggets',
            'Detroit Pistons','Golden State Warriors','Houston Rockets',
            'Indiana Pacers','Los Angeles Clippers','Los Angeles Lakers',
            'Memphis Grizzlies','Miami Heat','Milwaukee Bucks',
            'Minnesota Timberwolves','New Orleans Pelicans','New York Knicks',
            'Oklahoma City Thunder','Orlando Magic','Philadelphia 76ers',
            'Phoenix Suns','Portland Trail Blazers','Sacramento Kings',
            'San Antonio Spurs','Toronto Raptors','Utah Jazz','Washington Wizards']
    return LONG_TEAMS

def convert_team(team_name):
    TEAMS = get_team_shortnames()
    LONG_TEAMS = get_team_longnames()
    if len(team_name)>3:
	for ii in range(len(TEAMS)):
            if LONG_TEAMS[ii]==team_name:
		return TEAMS[ii]
    if len(team_name)==3:
	for ii in range(len(TEAMS)):
            if TEAM[ii]==team_name:
		return LONG_TEAMS[ii]
