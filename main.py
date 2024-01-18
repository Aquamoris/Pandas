import pandas as pd

df = pd.read_csv("bdf92d44747096a5.csv", delimiter=",")

# 1 часть задания

df = df.dropna()
df = df.fillna(0.0)

indexDrop = df[ (df['ЧастотаПродаж'] < 0) |(df['Цена'] < 0) |(df['ДлинаЕд'] < 0) |(df['ШиринаЕд'] < 0) |(df['ВысотаЕд'] < 0) |(df['НаСкладе'] < 0) ].index

df = df.drop(indexDrop)

print('Всего данных:', df.shape[0])
print('Всего признаков:', df.shape[1] - 1)

# 2 часть задания

df = df.rename(columns={"Остаток":"ВсегоТовара","Количество":"НаВитрине"})

average= df.groupby(['КодКатегории'])["Цена"].mean()
df = df.join(average, on='КодКатегории', rsuffix='_x')

df = df.rename(columns={"Цена_x":"Средняя_Цена"})

df["Разница"] = round(df["Цена"]- df["Средняя_Цена"])