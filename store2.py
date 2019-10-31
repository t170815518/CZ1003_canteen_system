store_menu = {
    "Yong Tau Foo" : ["Bee Hoon", "Kuay Teow", "Laska"],
    "Chicken Rice" : ["Steamed Chicken Rice", "Roasted Chicken Rice"],
    "Hand-made Noodles" : ["Sliced Fish Soup", "Ban Mian", "Tom Yam Seafood Noodles"],
    "Cantonese Roast Duck" : ["Specialty Duck Rice", "Duck Noodles", "Roasted Pork Rice"],
    "Western Food" : ["Chicken Chop", "Chicken Cutlet", "Fish and Chips"],
    "Salad" : ["Chicken Salad", "Fish Salad", "Salmon Salad"],
    "Starbuck's Coffee" : ["Americano", "Latte", "Cappucino"] }

#store_name = "Western Food"
#time = (2019,11,10,5,29) #yyyy,mm,dd,hh,mm

def get_menu(store_name, time): #return list of menu available at the time
    if store_name in store_menu.keys():
        if 6 <time[3] < 11:
            x = store_menu[store_name][0]
            print(x)
        elif 21 >= time[3] >= 11:
            x = store_menu[store_name]
            print(x)
        else:
            print("invalid")
            return 0
    else:
        print("invalid")
        return 0


#get_menu(store_name, time)
