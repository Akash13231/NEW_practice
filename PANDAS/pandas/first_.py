# from dataclasses import replace
# from sys import prefix
#
# import pandas as pd
# from numpy.f2py.crackfortran import kindselector
# from numpy.f2py.func2subr import var2fixfortran
from operator import index

x = [5, 6, 7, 8, 9, 10]
# var = pd.Series(x, index=['a','b','c','d','e','f'],dtype='float', name='first data')
# print(var)


strings = ["apple", "banana", "cherry", "date", "potato", "mango"]
# var = pd.Series(strings,index=[i for i in range(1, len(strings)+1)])
# print(var)


# var1 = pd.Series(5, index=[1,2,3,4,5,6,7,8,9])
# #print(var1)
# var2 = pd.Series(8, index=[1,2,3,4,5])
# #print(var1)
# print(var1 + var2)

# var = pd.DataFrame(strings, index=[i for i in range(1, len(strings)+1)])
# print(var)


# #Accecc data from DataFrame using column name
# xyz = {'name':["apple", "banana", "cherry", "grapes", "potato", "mango"], 'price':[100, 124, 170, 200, 90, 105]}
#
# var1 = pd.DataFrame(xyz, index=[i for i in range(1,len(xyz['name'])+1)])
# var2 = pd.DataFrame(xyz, columns=['name'], index=[i for i in range(1,len(xyz['name'])+1)])
# print(var1)
# print(var2)


# print(pd.Series([i for i in range(20)]))


# #Arithmatic and Logical operations on DataFrame
# xyz = {'A':[11,12,13,14,15,16,17], 'B':[1,2,3,4,5,6,7]}
# xyz1 = pd.DataFrame(xyz, index=[i for i in range(1,len(xyz['A'])+1)])
# print(xyz1)
# xyz1['C'] = xyz1['A'] + xyz1['B']
# xyz1['D'] = xyz1['A'] - xyz1['B']
# xyz1['E'] = xyz1['A'] * xyz1['B']
# #print(xyz1)
# xyz1['even'] = xyz1['E'] % 2 == 0
# print(xyz1)



# #Insert and delet data from DataFrame
# xyz = {'A':[11,12,13,14,15,16,17], 'B':[1,2,3,4,5,6,7]}
# xyz1 = {'C':[21,22,23,24,25,26,27]}
# var = pd.DataFrame(xyz, index=[i for i in range(1,len(xyz['A'])+1)])
#
# var.insert(2,'C',xyz1['C'])
# print(var)
#
# var.pop('B')
# print(var)
#
# del var['A']
# print(var)





# # Work with CSV files
                # write in CSV
# xyz = {'name':["apple", "banana", "cherry", "grapes", "potato", "mango"], 'price':[100, 124, 170, 200, 90, 105]}
# var = pd.DataFrame(xyz)
# var.to_csv('Test_csv_file1.csv',index=False,header=['NAME','PRICE'])





                # read CSV

# var = pd.read_csv("C:\\Users\\abhosage\\PycharmProjects\\Python_Pandas\\PANDAS\\pandas\\data.csv",usecols=['Duration'],skiprows=[5])
# print(var.to_string())            #it will print only data from Duration column

# var = pd.read_csv("data - Copy.csv",index_col='Duration', header=None, names=['Duration','Pulse','Maxpulse','Calories'])
# print(var.to_string())          # if file not having any headers it will take names list as a headers of data frame


# var = pd.read_csv("C:\\Users\\abhosage\\PycharmProjects\\Python_Pandas\\PANDAS\\pandas\\data.csv")
# print((var.fillna(0000)).to_string())
# print(var.index)
# print(var.describe())
# print(var[4:11])
# new_list = var['Duration'].tolist()
# new = var.to_numpy()
# print(new)
# var.loc[5,'Pulse'] = 100000    # it will change the 5th row and Pulse column data to 10000
# print(var[2:7])     # it wiil print row 2 to row 6 data using slicing method


#print(var.loc[[2,20],['Maxpulse','Calories']])  # It will print row 2 and row 20 data respect to column name


#print((var.iloc[:,[1,2]]).to_string())






#   dropna and fillna
#var = pd.read_csv("C:\\Users\\abhosage\\PycharmProjects\\Python_Pandas\\PANDAS\\pandas\\Test_csv_file1.csv")

#print(var.fillna({'NAME':'kiwi','PRICE':64,'Rank':3,'CITY':'murum'}))
#print(var.replace('pune','satara'))
#print(var.replace(100,1000000, inplace=True))
#print(var.fillna(method='ffill'))





# Duplicate data
# var = pd.read_csv("C:\\Users\\abhosage\\PycharmProjects\\Python_Pandas\\PANDAS\\pandas\\Test_csv_file1.csv")
# #print(var.duplicated())
#
# print(var.drop_duplicates(inplace=True))








# Merging and concat


# var1 = pd.DataFrame({'A':[11,12,13,14,15,16,17], 'B':[1,2,3,4,5,6,7]})
# var2 = pd.DataFrame({'C':[21,22,23,24,25,26,27], 'B':[1,3,4,6,7,8,9]})
#
# print(pd.merge(var1, var2))


#print(var.interpolate())




#Concat
# var1 = pd.Series([1,2,3,4,5])
# var2 = pd.Series([11,12,13,14,15])






# var = pd.DataFrame({'name':['a','b','c','a','d','b','c','a','d','a','c','b'],
#                     'S_1':[1,2,3,1,3,4,1,3,1,4,3,1],
#                     'S_2':[11,12,11,13,14,12,11,13,14,12,11,13]})
#
# varnew = var.groupby('name')
# print(varnew)
# for name,subject in varnew:
#     print(name)
#     print(subject)
#     print()
# #
# li = list(varnew)
# print(li)






# join dataframes
# var1 = pd.DataFrame({'A':[11,12,13,14,15,16,17], 'B':[1,2,3,4,5,6,7]})
# var2 = pd.DataFrame({'C':[21,22,23,24,25,26,27], 'D':[10,20,30,40,50,60,70]})






# Append
# Importing pandas as pd
# import pandas as pd
# import matplotlib.pyplot as plt
#
# df1 = pd.DataFrame({"a":[1, 2, 3, 4], "b":[5, 6, 7, 8]})
# df2 = pd.DataFrame({"a":[1, 2, 3], "c":[5, 6, 7]})
#
# df3 = df1._append(df2, ignore_index=True)
# df3.plot(kind = 'scatter', x = 'a', y = 'b')
#
# plt.show()
# var = pd.read_csv("C:\\Users\\abhosage\\PycharmProjects\\Python_Pandas\\PANDAS\\pandas\\data.csv")
#
# var.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
#
# plt.show()


# import pandas as pd
#
# # Example DataFrames
# df1 = pd.DataFrame({
#     'ID': [1, 2, 3],
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35]
# })
#
# df2 = pd.DataFrame({
#     'ID': [1, 2, 4],
#     'City': ['New York', 'Los Angeles', 'Chicago'],
#     'Salary': [70000, 80000, 65000]
# })
#
# # Merge on the common column 'ID'
# merged_df = pd.merge(df1, df2, on='ID')
#
# print(merged_df)




import pandas as pd

data = {
    "A": ["TeamA", "TeamB", "TeamB", "TeamC", "TeamA"],
    "B": [5, 40, 40, 30, 50],
    "C": [True, False, False, False, True]
}

df = pd.DataFrame(data)
df2 =df.drop_duplicates()
print(df2)