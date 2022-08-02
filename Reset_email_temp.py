import pandas as pd

file_path='Data-sent\Mohsin_data_p2.csv'
df=pd.read_csv(file_path)
df.to_csv('temp_email.csv', index=False)