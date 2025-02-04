import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

# Create a data set for analysis
x, y = make_regression(n_samples=500, n_features=1, noise=25, random_state=0)
y = y**2

# Split the data set into testing and training data
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)

# Plot the data
sns.set_style("darkgrid")
sns.regplot(x_test, y_test, fit_reg=False)

# Remove ticks from the plot
plt.xticks([])
plt.yticks([])

plt.tight_layout()
plt.show()
