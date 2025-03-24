import pandas as pd

# Replace with the actual path to your CSV file
file_path = "GOOGLE.csv"

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

df = df[["Open" , "High" , "Low" , "Close" , "Volume",]]
df['high_low'] = (df['High'] - df['Low']) / df['Close'] * 100.0
df['pct_change'] = (df['Close'] - df['Open']) / df['Open'] * 100.0

df = df[['Close' , 'high_low' , 'pct_change' , 'Volume']]

print(df.head())
