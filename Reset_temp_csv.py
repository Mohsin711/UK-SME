import pandas as pd

file_path='100_chuncks_with_index\part-1.csv'
df=pd.read_csv(file_path)
df.to_csv('temp.csv', index=False)