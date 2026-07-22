import pandas as pd
import numpy as np


df = pd.read_csv('coffee_data.csv')

print("--- STEP 1: DETECTING OUTLIERS WITH IQR ---")


q1 = df['Cups_Sold'].quantile(0.25)
q3 = df['Cups_Sold'].quantile(0.75)
iqr = q3 - q1


lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)

print(f"Cups Sold Boundaries: Lower = {lower_bound}, upper = {upper_bound}")


outliers = df[(df['Cups_Sold'] < lower_bound) | (df['Cups_Sold'] > upper_bound)]
print("\nDetected Outlier Rows:")
print(outliers)

print("\n--- STEP 2: WINSORIZATION (CAPPING OUTLIERS)---")

df['Cups_Sold_Cleaned'] = df['Cups_Sold'].clip(lower=lower_bound, upper=upper_bound)

print(df[['Day', 'Cups_Sold', 'Cups_Sold_Cleaned']])


df.to_csv('coffee_step1.csv',index=False)