import pandas as pd

#https://stackoverflow.com/questions/45708626/read-data-in-excel-column-into-python-list
df = pd.read_excel('regress_data.xlsx')
x_data_list = df['x'].tolist()
y_data_list = df['y'].tolist()

print(x_data_list)
print(y_data_list)