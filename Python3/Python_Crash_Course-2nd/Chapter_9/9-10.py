# 9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module.
## Restaurant.py



# Make a separate file that imports Restaurant. Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.

from Restaurant import Restaurant

mcbrowns = Restaurant('McBrown\'s','Hamburger')
mcbrowns.desc_restaurant()