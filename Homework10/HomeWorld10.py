
import pandas as pd
import random
# | Задание 44 |
# | --- |
# | В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# Create a sample DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
# Get unique values and create new columns with binary values
unique_vals = data['whoAmI'].unique()
for val in unique_vals:
    data[val] = (data['whoAmI'] == val).astype(int)
# Drop the original column
data = data.drop('whoAmI', axis=1)
print(data)