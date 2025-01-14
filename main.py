import os 
from utils import options

def black_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    list_names = ['Custom Control', 'Picking', 'Payment of Public Service and Administration', 'Suppliers', 'Contact', 'Solutionary']
    print('='*50)
    print('='*13, '   Routes of Access   ', '='*13)
    print('='*50)
    op = options(list_names=list_names)
    print('='*50)
    print(len(op), '*'*50)
    return op

def handle_selection(choice, op):
    if choice == 'exit'  or choice == 'e':
        return 'exit'    
    try:
        choice = int(choice)
        for i in range(len(op)):
            if choice == i+1:
                print(f'Option selected: {op[i]}')
            else:
                print('You were write unexpected option')
    
    except ValueError:
        print('Write the correct option')
        

def main():
    op = display_menu()

    while True:
        ch_1 = input('Write one option or if you want to leave, please write "exit": ')
        choice = handle_selection(choice= ch_1, op=op)

        if choice == 'exit':
            break

if __name__ == "__main__":
    main()