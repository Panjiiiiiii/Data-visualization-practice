import matplotlib.pyplot as plt
import seaborn as sns

human_height = [170.3, 168.7, 186.5, 190.5]
human_weight = [68.5, 63.4, 78.8, 85.3]

#plt scatterplot
plt.scatter(x=human_height, y=human_weight)
plt.show()

#sns scatterplot
sns.scatterplot(x=human_height, y=human_weight)
plt.show()

#sns regplott
sns.regplot(x=human_height, y=human_weight)
plt.show()