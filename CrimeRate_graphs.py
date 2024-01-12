import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv("integrated.csv")
#df["Deaths - Interpersonal violence - Sex: Both - Age: All Ages (Rate/100000)"].groupby([df["Year"]]).describe().to_csv("Crime_Rate_summaries_year.csv")
#df['Deaths - Interpersonal violence - Sex: Both - Age: All Ages (Rate/100000)'].groupby([df["region_code"],df["Year"]]).describe().to_csv("Crime_Rate_summaries_year_region.csv")

g = sns.barplot(y = "region_code", x = 'Deaths - Interpersonal violence - Sex: Both - Age: All Ages (Rate/100000)', data = df, hue = "Year",errorbar = None)
g.set_title("Crime Rate by Region and Year")
plt.ylabel("Regions")
plt.xlabel("Death from Interpersonal Violence per 100,000")
fig = g.get_figure()
# to run the first graph, uncomment line 16 and comment line 18 to 24
#plt.show()

fig.clf()
new_df = df[['Deaths - Interpersonal violence - Sex: Both - Age: All Ages (Rate/100000)', "region_code", "GDP/capita (USD)", "Year"]].copy()
new_df.query("Year == 2010", inplace = True)
g = sns.scatterplot(data = new_df, x = 'Deaths - Interpersonal violence - Sex: Both - Age: All Ages (Rate/100000)', y = "GDP/capita (USD)", hue = "region_code", s = 230, alpha = 0.3)
g.set_title("Crime Rate vs GDP in 2010")
plt.xlabel("Death from Interpersonal Violence per 100,000")
plt.show()