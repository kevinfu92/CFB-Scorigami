import pandas as pd
import plotly.express as px


df = pd.read_csv('historical_all_FBS_scores.csv')

all_scores = {}
for i in range(len(df)):
    score = (df.loc[i, 'win_score'], df.loc[i, 'lost_score'])
    if score not in all_scores:
        all_scores[score] = 1
    else:
        all_scores[score] += 1
win_score = []
lose_score = []
frequency = []
for score, value in all_scores.items():
    win_score.append(score[0])
    lose_score.append(score[1])
    frequency.append(value)

data_dict = {"win_score": win_score, "lose_score": lose_score, "frequency": frequency}

score_df = pd.DataFrame(data_dict)
fig = px.scatter(score_df, x="win_score", y="lose_score",
	         size="frequency", size_max=50)
fig.show()
