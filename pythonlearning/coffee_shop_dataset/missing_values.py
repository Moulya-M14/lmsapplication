import pandas as pd


df = pd.read_csv('coffee_step1.csv')

print("--- STEP 3: IDENTIFYING MISSING DATA---")
print(df.isnull().sum())

print("\n--- STEP 4: MEDIAN IMPUTATION---")

cups_median = df['Cups_Sold_Cleaned'].median()
temp_median = df['Temperature_F'].median()

print(f" Calculated Medians -> Cups: {cups_median}, Temp: {temp_median}")


df['Cups_Sold_Cleaned'] = df['Cups_Sold_Cleaned'].fillna(cups_median)
df['Temperature_Cleaned'] = df['Temperature_F'].fillna(temp_median)

print("\nDataset after handling outliers and missing values:")
print(df[['Day' , 'Cups_Sold_Cleaned', 'Temperature_Cleaned']])


df.to_csv('coffee_step2.csv', index=False)