# Visualization assignment : Plots leveraging 4 attributes
# H Hurchand

import pandas as pd
import matplotlib.pyplot as plt
import os

f = pd.read_csv('housing.data',sep='\s+',header=None)
df = pd.DataFrame(f)
df.columns =['CRIM','ZN','INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT','MEDV']
print(df)
os.makedirs('plots/2d', exist_ok=True)

plt.style.use("ggplot")
list1 = ['CRIM','LSTAT','MEDV','PTRATIO']

for col1 in list1:
    for col2 in list1:
        x = set([col1,col2])
        y = set(list1) - x
        if col1 != col2:
            m = list(y)
            col3 = m[0]
            col4 = m[1]

            fig, axes = plt.subplots(1, 1, figsize=(4, 4))
            fig.suptitle(f'{col1} to {col2} (color is {col3}, size is {col4})')
            axes.scatter(df[col1], df[col2], label=f'{col1} to {col2}', c=df[col3], s=df[col4], marker='s',
                 alpha=0.4, edgecolors='black', cmap='YlGn')
            axes.set_xlabel(col1)
            axes.set_ylabel(col2)
            axes.legend()
            plt.savefig(f'plots/2d/boston_{col1}_{col2}_{col3}_{col4}_scatter.png', dpi=300)
            plt.close(fig)

plt.close()