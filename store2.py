store_menu = { "Yong Tau Foo" : {"morning" : "Bee Hoon, Kuay Teow", "afternoon" : "Laska", "monday" : "Satay", "wednesday" : "", "sep" : ""},
    "Chicken Rice" : {"morning" : "Steamed Chicken Rice", "afternoon" : "Roasted Chicken Rice", "monday" : "" , "wednesday" : "Specialty Chicken Rice Set", "sep" : "" },
    "Hand-made Noodles" : {"morning" : "Sliced Fish Soup, Ban Mian" , "afternoon" : "Tom Yam Seafood Noodles", "monday" : "" , "wednesday" : "", "sep" : ""},
    "Cantonese Roast Duck" : {"morning" : "Specialty Duck Rice, Duck Noodles", "afternoon" : "Roasted Pork Rice", "monday" : "" , "wednesday" : "", "sep" : ""},
    "Western Food" : {"morning" : "Chicken Chop, Fish and Chips", "afternoon" : "Seafood Spaghetti", "monday" : "" , "wednesday" : "", "sep" : ""},
    "Salad" : {"morning": "Chicken Salad, Garden Salad", "afternoon" : "Salmon Salad", "monday" : "" , "wednesday" : "", "sep" : ""},
    "Starbuck's Coffee" : {"morning" : "Americano, Latte, Cappucino" , "afternoon" :  "", "monday" : "" , "wednesday" : "", "sep" : ""},
    "McDonald's" : {"morning" : "McMuffin, Big Breakfast, Hotcakes", "afternoon" : "McChicken, McSpicy, Fillet O' Fish", "monday" : "" , "wednesday" : "", "sep" : "" }}



def get_menu(store_name, TIME, mode):                     #return list of menu available at the time
    if mode == 1:                                         #Displays all items
        x = store_menu[store_name]["morning"], store_menu[store_name]["afternoon"], store_menu[store_name]["monday"], store_menu[store_name]["wednesday"]
        return x
    elif store_name == "McDonald's":
        if 1 <= TIME[5] <=6:
            if 7 <= TIME[3] <= 11:
                x = store_menu[store_name]["morning"], store_menu[store_name]["sep"]
                return x
            elif 12 <= TIME[3] <= 24:
                x = store_menu[store_name]["afternoon"], store_menu[store_name]["sep"]
                return x                
        elif TIME[5] == 0:
            if 10 <= TIME[3] <= 11:
                x = store_menu[store_name]["morning"], store_menu[store_name]["sep"]
                return x
            elif 12 <= TIME[3] <= 22:
                x = store_menu[store_name]["afternoon"], store_menu[store_name]["sep"]
                return x
    elif store_name == "Starbuck's Coffee":
        if 1 <= TIME[5] <= 5:
            if 7 <= TIME[3] <= 22:
                x = store_menu[store_name]["morning"], store_menu[store_name]["sep"]
                return x
            else:
                pass
        elif TIME[5] == 0 or TIME[5] == 6:
            if  7 <= TIME[3] <= 17:
                x = store_menu[store_name]["morning"], store_menu[store_name]["sep"]
                return x
            else:
                pass        
    elif 1 <= TIME[5] <= 5:                                         #Weekdays
        if TIME[5] == 1:                                            #Monday Special Menu
            if 7 <= TIME[3] <= 10:
                x = store_menu[store_name]["morning"], store_menu[store_name]["monday"]
                return x
            elif 11 <= TIME[3] <= 21:
                x = store_menu[store_name]["morning"], store_menu[store_name]["afternoon"], store_menu[store_name]["monday"]
                return x    
        elif TIME[5] == 3:                                          #Wednesday Special Menu
            if 7 <= TIME[3] <= 10:
                x = store_menu[store_name]["morning"], store_menu[store_name]["wednesday"]
                return x
            elif 11 <= TIME[3] <= 21:
                x = store_menu[store_name]["morning"], store_menu[store_name]["afternoon"], store_menu[store_name]["wednesday"]
                return x    
        else:                                                       #Other weekdays
            if 7 <= TIME[3] <= 10:
                x = store_menu[store_name]["morning"], store_menu[store_name]["sep"]
                return x
            elif 11 <= TIME[3] <= 21:
                x = store_menu[store_name]["morning"], store_menu[store_name]["afternoon"]
                return x
    elif TIME[5] == 6:                                              #Saturday
        if 7 <= TIME[3] <= 10:
            x = store_menu[store_name]["morning"], store_menu[store_name]["sep"]
            return x
        elif 11 <= TIME[3] <= 15:
            x = store_menu[store_name]["morning"], store_menu[store_name]["afternoon"]
            return x
    else:                                                          #Sunday, most stores closed
        pass
    

    
if __name__ == '__main__':
    print("test")
    mode = 0 # 0 for normal input, 1 for displaying all menus
    store_name = "Chicken Rice"
    TIME = (2019, 11, 7, 17, 29, 1)  # yyyy,mm,dd,hh,mm,day
    print(get_menu(store_name, TIME))
