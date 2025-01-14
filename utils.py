list_names = ['Custom Control', 'Picking', 'Payment of Public Service and Administration', 'Suppliers', 'Contact', 'Solutionary']

def options(list_names):
    options=[f'{i+1}. {list_names[i]}' for i in range(len(list_names))]
    for option in options:
        print(option)
    return options

# print(type(options(list_names=list_names)))

# op = options(list_names=list_names)
# print(op)

