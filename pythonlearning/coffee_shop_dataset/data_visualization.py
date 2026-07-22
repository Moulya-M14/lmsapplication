import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('coffee_final_processed.csv')


sns.set_theme(style="whitegrid")


fig, axes = plt.subplots(1, 3, figsize=(18, 5))


sns.lineplot(ax=axes[0], data=df, x='Day', y='Cups_Sold_Cleaned', marker='o', color='indigo', linewidth=2.5)
axes[0].set_title('Line Plot: Daily coffee Sales Trend', fontsize=14)
axes[0].set_ylabel('Cups Sold (cleaned)')


sns.scatterplot(ax=axes[1],data=df, x='Temperature_Cleaned', y='Cups_Sold_Cleaned', s=100, color='teal')
axes[1].set_title('Scatter plot: Sales vs Temperature', fontsize=14)

sns.histplot(ax=axes[2], data=df, x='Cups_sold_cleaned',bins=5, kde=True, color='darkorange' )
axes[2].set_title('Histogram: Distribution of' 'Sales Volume', fontsize=14)

plt.tight_layout()

print("Displaying visualizations... close the plot window to finish script. ")
plt.show()