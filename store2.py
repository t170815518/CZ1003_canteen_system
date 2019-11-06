store_menu = {
    "Yong Tau Foo" : ["Bee Hoon", "Kuay Teow", "Laska"],
    "Chicken Rice" : ["Steamed Chicken Rice", "Roasted Chicken Rice"],
    "Hand-made Noodles" : ["Sliced Fish Soup", "Ban Mian", "Tom Yam Seafood Noodles"],
    "Cantonese Roast Duck" : ["Specialty Duck Rice", "Duck Noodles", "Roasted Pork Rice"],
    "Western Food" : ["Chicken Chop", "Chicken Cutlet", "Fish and Chips"],
    "Salad" : ["Chicken Salad", "Fish Salad", "Salmon Salad"],
    "Starbuck's Coffee" : ["Americano", "Latte", "Cappucino"] }

#store_name = "Starbuck's Coffee"           Testing code
#time = (2019,11,7,9,29) #yyyy,mm,dd,hh,mm  Testing code

def get_menu(store_name, time):             #return list of menu available at the time
    if store_name in store_menu.keys():
        if 6 <= time[3] <= 10:              #Morning menu
            x = store_menu[store_name][0], store_menu[store_name][1]
            return x

        elif 11 <= time[3] <=21:            #Afternoon menu
            x = store_menu[store_name]
            return x

        else:                               #Not within operating hours
            print("Store is not open.")
            return 0
    else:
        print("Invalid")
        return 0


#print(get_menu(store_name, time))          #Testing code
