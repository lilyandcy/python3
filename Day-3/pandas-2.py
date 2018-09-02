import pandas as pd

df = pd.DataFrame([10, 20, 30, 40], columns = ['Numbers'], index= ['a', 'b', 'c', 'd'])

#add a new column called 'floats' directly
df['floats'] = (1.5, 2.5, 3.5, 4.5)

#add a new column called 'names' by index
df['names'] = pd.DataFrame(['Dan', 'Cox', 'Ale', 'Bob'], index= ['d', 'c', 'b', 'a'])

#add a new object to df
df = df.append(pd.DataFrame({'Numbers':66, 'floats':5.5, 'names':'Yor'}, index=['y',]))

print(df)



