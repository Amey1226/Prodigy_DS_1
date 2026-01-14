import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(
    "API_SP.POP.TOTL_DS2_en_csv_v2_34.csv",
    skiprows=4
)

print(df.head())


df_2020 = df[['Country Name', '2020']].dropna()

plt.figure(figsize=(8, 5))
plt.hist(df_2020['2020'], bins=20)

plt.title("Population Distribution Across Countries (2020)")
plt.xlabel("Population")
plt.ylabel("Number of Countries")

plt.show()


top10 = df_2020.sort_values(by='2020', ascending=False).head(10)

plt.figure(figsize=(10, 5))
sns.barplot(x='Country Name', y='2020', data=top10)

plt.title("Top 10 Most Populated Countries (2020)")
plt.xlabel("Country")
plt.ylabel("Population")
plt.xticks(rotation=45)

plt.show()
