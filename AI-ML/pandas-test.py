import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./test_titanic.csv')

# df.dropna(inplace = True)

df.dropna(axis=0)

df.dropna(axis=1)

if "Cabin" in df.columns:
    df.drop(columns=["Cabin"], inplace=True)

df["Fare"] = df["Fare"].round(2)

df["Ticket"] = df["Ticket"].astype(str).str.extract(r"(\d+)") #extract string from an integer using regex concept

df.drop_duplicates(inplace = True)

df.dropna(how='all')

# print(df.to_string())

plt.plot(df["Ticket"] , df["Fare"] , marker=" o " , linestyle = "-" , color="b" )

plt.xlabel('Ticket')
plt.ylabel('Fare')
plt.title('Ticket')
df.plot()

plt.show()