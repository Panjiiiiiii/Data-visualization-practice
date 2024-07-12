import  seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import  os

penguins = sns.load_dataset("penguins")

sns.barplot(data=penguins, x="species", y="body_mass_g", hue="sex", errorbar=None)
plt.show()

sns.scatterplot(data=penguins, x="body_mass_g", y="flipper_length_mm", hue="species", style="species")
plt.show()

#BTC-USD cluster bar
download_folder = os.path.expanduser("~/Downloads")
file_path = os.path.join(download_folder, "BTC-USD.csv")
df = pd.read_csv(file_path, delimiter=",")
df['Date'] = pd.to_datetime(df['Date'])
df_boxplot = df[["Open", "High", "Low", "Close", "Adj Close"]]
sns.boxplot(data=df_boxplot, palette="rocket")
plt.ylabel('Price', size=15)
plt.show()