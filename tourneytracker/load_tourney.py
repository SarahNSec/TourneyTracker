import pandas as pd
import numpy as np

matches = pd.read_csv("test_tourney.csv")
matches = matches.replace({np.nan: None})

print("end")