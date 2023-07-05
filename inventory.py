import smtplib


print('\n \n ********* Product Inventory Console Based Application *********')

products = []
EMAIL = 'premsagramani7@gmail.com'
PASSWORD = 'prem1234'
MENU = """
    1. Add Product
    2. View Products
    3. Remove Product
    4. User Add/Remove/Product-Details View
"""
USER_MENU = """
    1. Add Product
    2. Remove Product
    3. View Products
"""
SUBJECT = "Request for issuing me transcript"
BODY = "This is the body of the text message"
SENDER = "prem.sagar@arbisoft.com"
RECIPIENT = "premsagramani7@gmail.com"
APP_PASSWORD = "apxucxuwivjszdon"
msg = []

def send_email():
    msg.append(SUBJECT)    # Assign value subject to index 0
    msg.append(SENDER)     # Assign value sender to index 1
    msg.append(RECIPIENT)  # Assign value recipient to index 2
    msg.append(BODY)       # Assign value body to index 3
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(SENDER, APP_PASSWORD)
       smtp_server.sendmail(SENDER, RECIPIENT, ''.join(msg), BODY)
       
    print("Product added successfully and email sent to", RECIPIENT)
    
    
def addProduct():
        product_name = input('Enter the name of product to add : ')
        products.append(product_name)
        print('Added', product_name)
    
    
def removeProduct():
    if len(products) > 0:
        removed_product = products.pop()
        print('Removed',removed_product)
    else:
        print('List is empty')
        
        
def userFunctionalities():
    user_email = input('Enter your email : ')
    user_password = input('Enter you password : ')
    
    if(user_email == EMAIL and user_password == PASSWORD):
        print('\n User Logged In Successfully ')
        user_menu_options = ''
        while user_menu_options < '4':
            print('\n -- User View -- ')
            print(USER_MENU)
            user_menu_options = input('Enter 0 to go back to the user menu or choose an option: ')
            if user_menu_options == '0':
                continue
            elif user_menu_options == '1':
                addProduct()
                send_email()
            elif user_menu_options == '2':
                removeProduct()
            elif user_menu_options == '3':
                print(products)
            else:
                print('Invalid Option! Please try again')
                
    else:
        print('Credentials are incorrect')      
    
    
def showMainMenu():
    menuOptions = ''
    while menuOptions < '5':
        print('\n -----     Main Menu     ----- ')
        print(MENU)
        menuOptions = input('Enter 0 to go back to the main menu or choose an option: ')
        if menuOptions == '0':
            continue
        elif menuOptions == '1':
            addProduct()  
        elif menuOptions == '2':
            print(products)   
        elif menuOptions == '3':
            removeProduct()    
        elif menuOptions == '4':
            userFunctionalities()       
        else:
            print('Invalid Option! Please try again')
            

showMainMenu()
    





