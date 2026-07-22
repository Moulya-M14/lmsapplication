import pandas as pd
import numpy as np


data = {
    'Day':['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat' , 'Sun' , 'Mon2' ,'Tue2', 'Wed2',],
    'Cups_Sold' : [120, 135, np.nan, 140, 155, 950, 20, 130, 142, 138],
    'Temperature_F':[72, 68, 75, 71, 85, 42, 70, np.nan, 69, 73],
    'Promo_Type': ['None', 'Discount' , 'None' , 'BOGO' , 'Discount' , 'None' , 'None',
                   'BOGO' , 'None' , 'Discount']
}

df = pd.DataFrame(data)


df.to_csv('Coffee_data.csv' , index=False)
print("Base dataset 'cofee_data.csv' created successfully")
print(df)

