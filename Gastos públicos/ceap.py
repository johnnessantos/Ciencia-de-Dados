import pandas as pd
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt
%matplotlib inline

df = pd.read_csv('Ano-2017.csv', sep= ';')

print(df.columns.values)

'''
name = data['txNomeParlamentar'].unique()

print(name)
'''




plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()