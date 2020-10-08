import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')
titanic.head()

# Exercises
#
# ** Recreate the plots below using the titanic dataframe. There are very few hints since most of the plots can be done
# with just one or two lines of code and a hint would basically give away the solution. Keep careful attention
# to the x and y labels for hints.**

sns.jointplot(x = 'fare', y = 'age', data = titanic)
plt.show()

sns.displot(titanic['fare'], kde = False, bins = 30, color='red')
plt.show()

sns.boxplot(x='class', y='age', data=titanic)
plt.show()

sns.swarmplot(x='class', y='age', data=titanic)
plt.show()

sns.countplot(x='sex', data=titanic)
plt.show()

sns.heatmap(titanic.corr(), cmap='coolwarm')
plt.title('titanic corr')
plt.show()

g = sns.FacetGrid(data=titanic,col='sex')
g.map(plt.hist,'age')
plt.show()

