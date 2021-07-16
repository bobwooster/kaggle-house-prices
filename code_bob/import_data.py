import sys
import pandas as pd
print(sys.executable)
print(sys.version)

# load data
train_df = pd.read_csv('../data/train.csv')
test_df = pd.read_csv('../data/train.csv')

# print the first five lines
print(train_df.head())
