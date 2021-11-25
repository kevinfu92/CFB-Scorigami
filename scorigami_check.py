from __future__ import print_function
import time
import config
import cfbd
from cfbd.rest import ApiException
from pprint import pprint
from matplotlib import pyplot
import pandas as pd


df = pd.read_csv('historical_scorigami_scores.csv')
FBS_teams = pd.read_csv('FBS_schools.csv')
# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = config.api_key
configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.GamesApi(cfbd.ApiClient(configuration))
year = 2021 # int | Year/season filter for games
week = 13 # int | Week filter (optional)
season_type = 'regular' # str | Season type filter (regular or postseason) (optional) (default to regular)
team = 'team_example' # str | Team (optional)
home = 'home_example' # str | Home team filter (optional)
away = 'away_example' # str | Away team filter (optional)
conference = 'B1G' # str | Conference abbreviation filter (optional)
id = 56 # int | id filter for querying a single game (optional)
FBS_schools = list(FBS_teams.Name.values)

try:
    # Games and results
    api_response = api_instance.get_games(year, week=week)
    # pprint(api_response)
except ApiException as e:
    print("Exception when calling GamesApi->get_games: %s\n" % e)


df['score_comb'] = df.apply(lambda x: str(x.win_score), axis=1) + ":" + df.apply(lambda x: str(x.lost_score), axis=1)

scorigami = False
for i in api_response:
    if i.home_team in FBS_schools or i.away_team in FBS_schools:
        if i.home_points is not None:
            win_score = str(max(i.home_points, i.away_points))
            lose_score = str(min(i.home_points, i.away_points))
            if (win_score + ":" + lose_score) not in df.score_comb.values:
                print('There is a scorigami!!!!')
                print(i.away_team + ' (' +str(i.away_points) + ") @ " + i.home_team + ' (' + str(i.home_points) + ')')
                scorigami = True
if scorigami == False:
    print('No scorigami for ' + str(year) + ' week ' + str(week))
