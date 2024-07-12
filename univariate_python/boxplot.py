import matplotlib.pyplot as plt
import  numpy as np
import seaborn as sns

x = np.random.normal(15,5,250)

#boxplot sns
sns.boxplot(x)
plt.show()