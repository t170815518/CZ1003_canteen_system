store_menu = {
    "store_1" : ["Item A", "Item B", "Item C"],
    "store_2" : ["Item D", "Item E", "Item F"],
    "store_3" : ["Item G", "Item H", "Item I"]
}

store_OH = {
    "store_1" : ["7am-10pm", "9am-6pm", "9am-5pm"],
    "store_2" : ["7am-11pm", "9am-9pm", "9am-5pm"],
    "store_3" : ["7am-9pm", "9am-7pm", "9am-6pm"],
}


def check_menu():  
    while True:
        try:
            user_input_menu = int(input("Which store's menu would you like to check? (Enter: 1,2 or 3) : "))
            break
        except:
            print("Valid integer: 1 - 3 ")
            continue
    
    if user_input_menu == 1:
        print(store_menu["store_1"])
    elif user_input_menu == 2:
        print(store_menu["store_2"])
    elif user_input_menu == 3:
        print(store_menu["store_3"])
    else:
        print("Valid integer: 1 - 3 ") 
        check_menu()

def check_OH():
    while True:
        try:
            user_input_OH = int(input("Which store's operating hours would you like to check? (Enter 1,2 or 3) : "))
            break
        except:
            print("Valid integer: 1 - 3 ")
            continue

    if user_input_OH == 1:
        print(store_OH["store_1"])
    if user_input_OH == 2:
        print(store_OH["store_2"])
    if user_input_OH == 3:
        print(store_OH["store_3"])
    else:
        print("Valid integer: 1 - 3 ") 
        check_menu()

def start():
    while True:
        try:
            print("Welcome! Would you like to check: ", "(1) Menu", "(2) Operating Hours", "Valid integer 1 - 2", sep='\n')
            user_input_start = int(input("Choice: "))
            break
        except:
            print("Valid integer: 1 - 2 ")
            continue
    if user_input_start == 1:
        check_menu()
    elif user_input_start == 2:
        check_OH()
    else:
        print("Valid integer: 1 - 2 ")
        start()

    
start()


