from store import store_menu
from store import store_OH
from datetime import datetime


x = open("database.txt", "r")
y = x.readlines()
for line in y:
  words = line.split()
  print(words)

  
    
