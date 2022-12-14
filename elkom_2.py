# -*- coding: utf-8 -*-
"""Elkom 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DX8QjihTIYSlV6E0osRHiYrXEdzeJocm
"""

import pandas as pd
from google.colab import files
uploaded = files.upload()

data_quina = pd.read_csv('titanic.csv')
print(data_quina)

data1 = data_quina[['Name', 'Sex', 'Age', 'Pclass', 'Fare']]
sex = data1.groupby('Sex')['Name'].nunique()
print('Jumlah sex: \n', sex)

data2 = data_quina[['Name', 'Sex', 'Age', 'Pclass', 'Fare']]
notsurvivedpassanger = data2['Sex'].loc[data_quina['Survived'] == 0]
print('Penumpang yang tidak survived:\n', notsurvivedpassanger.value_counts())
survivedpassanger = data2['Sex'].loc[data_quina['Survived'] == 1]
print('\nPenumpang yang survived:\n', survivedpassanger.value_counts())