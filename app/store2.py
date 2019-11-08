store_menu = {
    "Yong Tau Foo": ["Bee Hoon", "Kuay Teow", "Laska"],
    "Chicken Rice": ["Steamed Chicken Rice", "Roasted Chicken Rice"],
    "Hand-made Noodles": ["Sliced Fish Soup", "Ban Mian", "Tom Yam Seafood Noodles"],
    "Cantonese Roast Duck": ["Specialty Duck Rice", "Duck Noodles", "Roasted Pork Rice"],
    "Western Food": ["Chicken Chop", "Chicken Cutlet", "Fish and Chips"],
    "Salad": ["Chicken Salad", "Fish Salad", "Salmon Salad"],
    "Starbuck's Coffee": ["Americano", "Latte", "Cappucino"]}


def get_menu(store_name, time, mode):             # return list of menu available at the time
    if mode == 1:
        x = store_menu[store_name]
        return x
    elif store_name in store_menu.keys():
        if 0 <= time[3] <= 11:              # Morning menu
            x = store_menu[store_name][0], store_menu[store_name][1]
            return x
        elif 11 <= time[3] <= 24:            # Afternoon menu
            x = store_menu[store_name]
            return x


if __name__ == '__main__':
    store_name = "Hand-made Noodles"
    time = (2019, 11, 8, 10, 00)  # yyyy,mm,dd,hh,mm  Testing code
    print(get_menu(store_name, time, 0))
