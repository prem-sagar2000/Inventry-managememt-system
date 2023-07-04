print('********* Inventory Management System *********')
print(' ')
mainMenu = input('Enter 0 for Main Menu : ')
productList = []
menuOptions = ''
def Menu():
    print('- Enter 1 for adding a product ')
    print('- Enter 2 for viewing the products')
    print('- Enter 3 for removing the product')
    print('- Enter 4 for user add/remove view')
    print('- Enter 5 for user details view')
    
    
if (mainMenu == '0'):
    Menu()
    menuOptions = input('Enter desired number to Continue : ')
    if menuOptions == '1':
        productList.append(input('Enter the name of product to add : '))
        print('Product Added')
    elif menuOptions == '2':
        print(productList)
    elif menuOptions == '3':
        productList.pop()
    elif menuOptions == '4':
        print(productList)
    elif menuOptions == '5':  
        print('Nothing')
    else:
        print('nothing of nested if')
else:
    print('nothing for main menu')
    
    





#console based application in which:
#- product add
#- product view
#- product remove
#- user add remove view
#- user details view