store_menu = { "Yong Tau Foo" : {"morning" : "Bee Hoon, Kuay Teow", "afternoon" : "Laska", "monday" : "Satay", "wednesday" : ""},
    "Chicken Rice" : {"morning" : "Steamed Chicken Rice", "afternoon" : "Roasted Chicken Rice", "monday" : "" , "wednesday" : "Specialty Chicken Rice Set" },
    "Hand-made Noodles" : {"morning" : "Sliced Fish Soup, Ban Mian" , "afternoon" : "Tom Yam Seafood Noodles", "monday" : "" , "wednesday" : ""},
    "Cantonese Roast Duck" : {"morning" : "Specialty Duck Rice, Duck Noodles", "afternoon" : "Roasted Pork Rice", "monday" : "" , "wednesday" : ""},
    "Western Food" : {"morning" : "Chicken Chop, Fish and Chips", "afternoon" : "Fish and Chips", "monday" : "" , "wednesday" : ""},
    "Salad" : {"morning": "Chicken Salad, Garden Salad", "afternoon" : "Salmon Salad", "monday" : "" , "wednesday" : ""},
    "Starbuck's Coffee" : {"morning" : "Americano, Latte, Cappucino" , "afternoon" :  "", "monday" : "" , "wednesday" : ""} }



def get_menu(store_name, time):                     #return list of menu available at the time
    if 1 <= time[5] <=5 and store_name == "Starbuck's Coffee":
        if 7 <= time[3] <= 10:
                x = store_menu[store_name]["morning"]
                return x
        elif 11 <= time[3] <= 22:
                x = store_menu[store_name]["morning"], store_menu[store_name]["afternoon"]
                return x
    elif 1 <= time[5] <= 5:                                         #Weekdays
        if time[5] == 1:                                            #Monday Special Menu
            if 7 <= time[3] <= 10:
                x = store_menu[store_name]["morning"], store_menu[store_name]["monday"]
                return x
            elif 11 <= time[3] <= 21:
                x = store_menu[store_name]["morning"], store_menu[store_name]["afternoon"], store_menu[store_name]["monday"]
                return x    
        elif time[5] == 3:                                          #Wednesday Special Menu
            if 7 <= time[3] <= 10:
                x = store_menu[store_name]["morning"], store_menu[store_name]["wednesday"]
                return x
            elif 11 <= time[3] <= 21:
                x = store_menu[store_name]["morning"], store_menu[store_name]["afternoon"], store_menu[store_name]["wednesday"]
                return x    
        else:                                                       #Other weekdays
            if 7 <= time[3] <= 10:
                x = store_menu[store_name]["morning"]
                return x
            elif 11 <= time[3] <= 21:
                x = store_menu[store_name]["morning"], store_menu[store_name]["afternoon"]
                return x
    elif 6 <= time[5] <= 7 and store_name == "Starbuck's Coffee":
        if 7 <= time[3] <= 10:
            x = store_menu[store_name]["morning"]
            return x
        elif 11 <= time[3] <= 17:
            x = store_menu[store_name]["morning"], store_menu[store_name]["afternoon"]
            return x
    elif time[5] == 6:                                              #Saturday
        if 7 <= time[3] <= 10:
            x = store_menu[store_name]["morning"]
            return x
        elif 11 <= time[3] <= 15:
            x = store_menu[store_name]["morning"], store_menu[store_name]["afternoon"]
            return x
    else:                                                          #Sunday
        pass
    

    
if __name__ == '__main__':
    print("test")
    store_name = "Chicken Rice"
    time = (2019, 11, 7, 17, 29, 1)  # yyyy,mm,dd,hh,mm,day
    print(get_menu(store_name, time))
