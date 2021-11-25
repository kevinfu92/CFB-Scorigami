# CFB-Scorigami
This project pulls all scores participated by at least one current FBS school and compile a CFB scorigami

This project uses api from "https://github.com/CFBD/cfbd-python". The goal of this project is to pull all score combination from current FBS school, and determine whether there is a so-called "scorigami" every week. 

scorigami: https://en.wikipedia.org/wiki/Scorigami


## Pull Data
To pull all score combinations (duplicates not included), "scorigami_data_pull.py" can be run and data will be stored at "historical_scorigami_scores.csv"
To pull all score combinations (duplicates included), "all_score_data_pull.py" can be run and data will be stored at "historical_all_FBS_scores.csv"

## Use Pulled Data to Check for Scorigami
To check whether there is a scorigami, run "scorigami_check.py" and change the week/year to most recent one. It will tell you whether or not there is a scorigami and which game it was!!<br>
To check the number of times each score combination occurred, run "FBS_score_frequency.py"\n
To see the "map" of each score combination occurred before (and when it first occurred), scorigami from most recent year (2021 as of now), and potential score combinations for scorigami, run "FBS_scorigami.py"\n
