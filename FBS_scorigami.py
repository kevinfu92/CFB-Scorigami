from matplotlib import pyplot
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
df = pd.read_csv('historical_scorigami_scores.csv')
import plotly.graph_objects as go

# create empty lists for scorigami (0-100 points)
total_score = []
for i in range(81):
    for j in range(81):
        if i >= j:
            total_score.append([i, j])

for i in range(len(df)):
    if [df.loc[i, 'win_score'], df.loc[i, 'lost_score']] in total_score:
        total_score.remove([df.loc[i, 'win_score'], df.loc[i, 'lost_score']])

score_left_win =[]
score_left_lost = []
for i in total_score:
    score_left_win.append(i[0])
    score_left_lost.append(i[1])
# Create tag for plotly
df['tag'] = df['away_team'] + " (" + df.apply(lambda x: str(x.away_score), axis=1) + ") @ " + \
    df['home_team'] + " (" + df.apply(lambda x: str(x.home_score), axis=1) + ") on " +\
    df.apply(lambda x: x.date[0:10], axis=1)

# Create year column to identify new scorigami
df['year'] = df.apply(lambda x: int(x.date[:4]), axis=1)
year = 2021
df_year = df[df.year == year]



# plotly charts
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=df['win_score'], y=df['lost_score'], mode='markers', name='Scores occurred',
        hovertext=df['tag']
    )
)

fig.add_trace(
    go.Scatter(
        x=score_left_win, y=score_left_lost, mode='markers', name='Scorigami Scores'
    )
)

fig.update_layout(
    title='FBS Scorigami', xaxis_title = 'Winning Team Score', yaxis_title='Losing Team Score'
)

fig.add_trace(
    go.Scatter(
        x=df_year['win_score'], y=df_year['lost_score'], mode='markers', name=str(year) + ' scorigami',
        hovertext=df_year['tag']
    )
)



fig.show()

