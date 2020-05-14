import numpy as np
import matplotlib.pyplot as plt
import pandas
from mpl_toolkits.mplot3d import Axes3D
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import pandas as pd



data = pd.read_csv(r"C:\Users\Suleman Farooqi\Downloads\Adops & Data Scientist Sample Data - Q2 Regression.csv", header=None)
data.columns = ['f','g', 'h']


# Plot the data
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_trisurf(data['f'], data['g'], data['h'])
ax.view_init(20, -120)
ax.set_xlabel('f')
ax.set_ylabel('g')
ax.set_zlabel('h')



# Fit the model
model = ols("h ~ f + g", data).fit()

# Print the summary
print(model.summary())

print("\nRetrieving manually the parameter estimates:")
print(model._results.params)


# Peform analysis of variance on fitted linear model
anova_results = anova_lm(model)
print('\nANOVA results')
print(anova_results)



