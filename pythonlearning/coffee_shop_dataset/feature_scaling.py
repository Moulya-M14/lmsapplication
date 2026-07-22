import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler


df = pd.read_csv('coffee_step2.csv')

print("---STEP 5: MIN-MAX NORMALIZATION (Scale to 0-1) ---")
min_max_scaler = MinMaxScaler()

cups_scaled = min_max_scaler.fit_transform(df[['Cups_Sold_Cleaner']])
df['Cups_MinMax'] = cups_scaled

print("--- STEP 6: Z-SCORE STANDARIZATION (Mean=0, stdDev=1)")

Standard_scaler = StandardScaler()
temp_scaled = Standard_scaler.fit_transform
(df[['Temperature_Cleaned']])
df['Temp_standardized'] = temp_scaled

print(df[['Day', 'Cups_Sold_Cleaned', 'Cups_MinMax',
          'Temperature_Cleaned', 'Temp_Standardized']])


df.to_csv('coffee_step3.csv', index=False)