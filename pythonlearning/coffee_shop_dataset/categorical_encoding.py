import pandas as pd
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv('coffee_step3.csv')
print("--- STEP 7: LABEL ENCODING---")
df['Promo_Type'] = df['Promo_Type'].fillna('Unknown')


label_enc = LabelEncoder()
df['Promo_LabelEncoder'] = label_enc.fit_transform(df['Promo_Type'])


print("Label Encoding Mapping:")
for index, class_label in enumerate(label_enc.classes_):
    print(f" {class_label} -> {index}")

print("\n--- STEP 8: ONE-HOT ENCODING---:")

df_one_hot = pd.get_dummies(df['Promo_Type'],prefix='Promo')

                    


df_one_hot = df_one_hot.astype(int)


final_dataset = pd.concat([df, df_one_hot], axis=1)

print("\nFinal Engineered Dataset Summary:")

available_columns = ['Day', 'Promo_Type', 'Promo_LabelEncoded'] + list(df_one_hot.columns)
 
print(final_dataset[available_colums])


final_dataset.to_csv('coffee_final_processed.csv', index=False)

print("\nSuccess! 'coffee_final_processed.csv'saved.")