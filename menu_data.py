import pickle

menus = {
    "Yong Tau Foo": {"morning": "Bee Hoon, Kuay Teow", "afternoon": "Laska", "monday": "Satay", "wednesday": ""},
    "Chicken Rice": {"morning": "Steamed Chicken Rice", "afternoon": "Roasted Chicken Rice", "monday": "",
                     "wednesday": "Specialty Chicken Rice Set"},
    "Hand-made Noodles": {"morning": "Sliced Fish Soup, Ban Mian", "afternoon": "Tom Yam Seafood Noodles", "monday": "",
                          "wednesday": ""},
    "Cantonese Roast Duck": {"morning": "Specialty Duck Rice, Duck Noodles", "afternoon": "Roasted Pork Rice",
                             "monday": "", "wednesday": ""},
    "Western Food": {"morning": "Chicken Chop, Fish and Chips", "afternoon": "Fish and Chips", "monday": "",
                     "wednesday": ""},
    "Salad": {"morning": "Chicken Salad, Garden Salad", "afternoon": "Salmon Salad", "monday": "", "wednesday": ""},
    "Starbuck's Coffee": {"morning": "Americano, Latte, Cappucino", "afternoon": "", "monday": "", "wednesday": ""}}

with open('menu.txt', 'wb') as f:
    pickle(menus, f)
