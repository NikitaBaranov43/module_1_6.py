my_dict = {"Fedor": 1988 ,'Pasha': 1992 ,'Ilya': 1997 , 'Kirill': 2003}
print(my_dict)
print(my_dict['Pasha'])
my_dict['Viktor'] = 1975
print(my_dict['Viktor'])
my_dict.update({"Valeria": 2004, 'Karina': 2005})
G = my_dict.pop('Fedor')
print(G)
print(my_dict)



My_set = {1, 2, 3, "Python" , 1 , 2, 3 , 'Python'}
print(My_set)
My_set.add(44)
My_set.add('Privet')
My_set.remove(1)
print(My_set)
