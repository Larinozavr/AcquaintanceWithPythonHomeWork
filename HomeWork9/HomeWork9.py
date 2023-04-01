import pandas as pd
data = pd.read_csv('california_housing_train.csv')

# выбрать только строки с population от 0 до 500
filtered_data = data[(data['population'] >= 0) & (data['population'] <= 500)]

# вычислить среднюю стоимость для отфильтрованных строк
mean_price = filtered_data['median_house_value'].mean()

print(f'Средняя стоимость дома, где число людей от 0 до 500: {mean_price}')

min_population = data['population'].min()
# отфильтровать строки по минимальному значению population
filtered_data = data[data['population'] == min_population]
# найти максимальное значение households для отфильтрованных строк
max_households = filtered_data['households'].max()
print(
    f'Максимальное значение households в зоне минимального значения population: {max_households}')