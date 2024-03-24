import pandas as pd
import numpy as np
# from tracker.models import Match

matches = pd.read_csv("./tourneytracker/data/test_tourney.csv")
matches = matches.replace({np.nan: None})

for index, match in matches.iterrows():
    print(match)

print("end")