import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

cities = ('Malang', 'Jember', 'Jombang', 'Pasuruan', 'Surabaya', 'Mojokerto')
population = (800000, 500000, 450000, 120000, 1000000, 230000)

#Bar
plt.bar(x=cities, height=population)
plt.xticks(rotation=45)
plt.show()

#Bar_H
plt.barh(y=cities, width=population)
plt.show()

df = pd.DataFrame({
    'Cities': cities,
    'Population' : population
})
df.sort_values(by='Population', inplace=True)

plt.barh(y=df['Cities'], width=df['Population'])
plt.xlabel("Population")
plt.title("City at East Java")
plt.show()

#sns barplot
sns.barplot(y=df['Cities'], width=df['Population'], orient="v", color='green')
plt.xlabel("Population")
plt.title("City at East Java")
plt.show()