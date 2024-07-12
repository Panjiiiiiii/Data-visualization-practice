import matplotlib.pyplot as plt
import  numpy as np
import seaborn as sns

x = np.random.normal(15,5,250)

#histogram plt
plt.hist(x=x, bins=15)
plt.show()

#histogram sns
sns.histplot(x=x, bins=15, kde=True)
plt.show()