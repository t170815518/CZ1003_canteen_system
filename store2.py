store_menu = { "Yong Tau Foo" : {"morning" : "Bee Hoon, Kuay Teow", "afternoon" : "Laska", "monday" : "Satay", "wednesday" : ""},
    "Chicken Rice" : {"morning" : "Steamed Chicken Rice", "afternoon" : "Roasted Chicken Rice", "monday" : "" , "wednesday" : "Specialty Chicken Rice Set" },
    "Hand-made Noodles" : {"morning" : "Sliced Fish Soup, Ban Mian" , "afternoon" : "Tom Yam Seafood Noodles", "monday" : "" , "wednesday" : ""},
    "Cantonese Roast Duck" : {"morning" : "Specialty Duck Rice, Duck Noodles", "afternoon" : "Roasted Pork Rice", "monday" : "" , "wednesday" : ""},
    "Western Food" : {"morning" : "Chicken Chop, Fish and Chips", "afternoon" : "Fish and Chips", "monday" : "" , "wednesday" : ""},
    "Salad" : {"morning": "Chicken Salad, Garden Salad", "afternoon" : "Salmon Salad", "monday" : "" , "wednesday" : ""},
    "Starbuck's Coffee" : {"morning" : "Americano, Latte, Cappucino" , "afternoon" :  "", "monday" : "" , "wednesday" : ""} }

#store_name = "Chicken Rice"                          
#time = (2019,11,7,11,29,1)                             #yyyy,mm,dd,hh,mm,day

def get_menu(store_name, time):                         #return list of menu available at the time
    if store_name in store_menu:
        if 6 <= time[3] <= 10 and time[5] == 1:         #Morning menu
            x = store_menu[store_name]["morning"], store_menu[store_name]["monday"]
            return x
        elif 6 <= time[3] <= 10:
            x = store_menu[store_name]["morning"]
            return x

        elif 11 <= time[3] <=21 and time[5] == 3:       #Afternoon menu
            x = store_menu[store_name]["morning"], store_menu[store_name]["afternoon"], store_menu[store_name]["wednesday"]
            return x
        elif 11 <= time[3] <=21:
            x = store_menu[store_name]["morning"], store_menu[store_name]["afternoon"]
            return x
        else:                                           #Not within operating hours
            print("Store is not open.")
            return 0
    
    else:
        print("Invalid")
        return 0


#print(get_menu(store_name, time))
