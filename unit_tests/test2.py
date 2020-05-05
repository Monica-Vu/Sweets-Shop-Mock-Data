dict_1 = {'item': [1, 2], 'item2': [3, 2]}
dict_2 = {'item3': [5, 2], 'item6': [2, 6]}
dict_3 = {'item4': [3, 2], 'item5': [2, 1]}

context = {**dict_1, **dict_2, **dict_3}

print(context)