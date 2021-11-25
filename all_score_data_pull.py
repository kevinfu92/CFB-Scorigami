from __future__ import print_function
import config
import cfbd
from cfbd.rest import ApiException
import pandas as pd

# Doc at "https://github.com/CFBD/cfbd-python"


# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = config.api_key
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.GamesApi(cfbd.ApiClient(configuration))
year = 1869 # int | Year/season filter for games
week = 1 # int | Week filter (optional)
season_type = 'regular' # str | Season type filter (regular or postseason) (optional) (default to regular)
team = 'team_example' # str | Team (optional)
home = 'home_example' # str | Home team filter (optional)
away = 'away_example' # str | Away team filter (optional)
conference = 'B1G' # str | Conference abbreviation filter (optional)
id = 56 # int | id filter for querying a single game (optional)
FBS_teams = pd.read_csv('FBS_schools.csv')
# FBS_schools = ['Air Force', 'Akron', 'Alabama', 'Appalachian State', 'Arizona', 'Arizona State', 'Arkansas', 'Arkansas State', 'Army', 'Auburn', 'Ball State', 'Baylor', 'Boise State', 'Boston College', 'Bowling Green', 'Buffalo', 'BYU', 'California', 'Central Michigan', 'Charlotte', 'Cincinnati', 'Clemson', 'Coastal Carolina', 'Colorado', 'Colorado State', 'Connecticut', 'Duke', 'East Carolina', 'Eastern Michigan', 'Florida', 'Florida Atlantic', 'Florida International', 'Florida State', 'Fresno State', 'Georgia', 'Georgia Southern', 'Georgia State', 'Georgia Tech', "Hawai'i", 'Houston', 'Illinois', 'Indiana', 'Iowa', 'Iowa State', 'Kansas', 'Kansas State', 'Kent State', 'Kentucky', 'Liberty', 'Louisiana', 'Louisiana Monroe', 'Louisiana Tech', 'Louisville', 'LSU', 'Marshall', 'Maryland', 'Memphis', 'Miami', 'Miami (OH)', 'Michigan', 'Michigan State', 'Middle Tennessee', 'Minnesota', 'Mississippi State', 'Missouri', 'Navy', 'NC State', 'Nebraska', 'Nevada', 'New Mexico', 'New Mexico State', 'North Carolina', 'Northern Illinois', 'North Texas', 'Northwestern', 'Notre Dame', 'Ohio', 'Ohio State', 'Oklahoma', 'Oklahoma State', 'Old Dominion', 'Ole Miss', 'Oregon', 'Oregon State', 'Penn State', 'Pittsburgh', 'Purdue', 'Rice', 'Rutgers', 'San Diego State', 'San José State', 'SMU', 'South Alabama', 'South Carolina', 'Southern Mississippi', 'South Florida', 'Stanford', 'Syracuse', 'TCU', 'Temple', 'Tennessee', 'Texas', 'Texas A&M', 'Texas State', 'Texas Tech', 'Toledo', 'Troy', 'Tulane', 'Tulsa', 'UAB', 'UCF', 'UCLA', 'UMass', 'UNLV', 'USC', 'Utah', 'Utah State', 'UTEP', 'UT San Antonio', 'Vanderbilt', 'Virginia', 'Virginia Tech', 'Wake Forest', 'Washington', 'Washington State', 'Western Kentucky', 'Western Michigan', 'West Virginia', 'Wisconsin', 'Wyoming']

# Initialize data storage
scores = []
home_score = []
away_score = []
home_team = []
away_team = []
date = []

for year in range(1869,2021):
    try:
        # Games and results
        api_response = api_instance.get_games(year)
        # pprint(api_response)
    except ApiException as e:
        print("Exception when calling GamesApi->get_games: %s\n" % e)


    for i in api_response:
        if i.home_team in FBS_schools or i.away_team in FBS_schools:
            score_comb = {i.away_points, i.home_points}
            scores.append(score_comb)
            home_score.append(i.home_points)
            away_score.append(i.away_points)
            home_team.append(i.home_team)
            away_team.append(i.away_team)
            date.append(i.start_date)
    print(year)



data_dict = {'home_score': home_score, 'away_score': away_score, 'home_team': home_team, 'away_team': away_team, 'date': date}
df = pd.DataFrame(data_dict)

# create new columns for winning/losing scores for plot
df['win_score'] = df[['home_score', 'away_score']].max(axis=1)
df['lost_score'] = df[['home_score', 'away_score']].min(axis=1)

# Export data frame
df.to_csv('historical_all_FBS_scores.csv', index=False)
